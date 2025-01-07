from .database import db

class Ingredient:
    '''
    An ingredient name is unique and is the key to the database.
    The ingredient is stored in the database and can be retrieved by name.

    Base measures are always metric so the conversions only need to go one way. Plus metric is way better
    '''
    def __init__(self, name: str, qty:int=None, qtyUnit:str=None, size=None, initData:dict=None, db=db):
        self.db = db # This is the database connection, it is passed in so that the class can be tested

        ######################
        # These are the attributes that will be stored/recalled in the database
        # 
        # name is the common but unique name of the ingredient. 
        #   This is the db key for the ingredient table and must be unique
        #   For example flour must be defined as "ap flour" or an egg as "large egg"
        self.name             = name   

        #
        # displayName is the name that will be displayed to the user and can be anything. 
        # All-purpose flour,large free range egg, etc.    
        self.displayName      = ""    # name for display
        self.measurement      = ""    # gram, ml, each, etc.
        self.size             = ""    # for ingredients that have sizes ( large egg, small onion, etc.)
        self.rawStorage       = ""    # refrigerator, pantry, etc.
        self.processedStorage = ""    # refrigerator, pantry, etc.
        self.shelfLife        = 0     # in days
        self.notes            = ""    #
        self.tags             = ""    # tags for searching
        self.category         = ""    # protein, vegetable, etc.
        self.subcategory      = ""    # beef, tofu, leafy green, tuber, etc.
        self.kosher           = ""    # flesh, dairy, pareve, treif

        self.__set_attributes__(initData)

        # qty is local to this instantiation . 
        #   This allows a recipe to be created with a qty that is different from 
        #   the pantry qty. Qty can be modified by the recipe at will. 
        if qtyUnit:
            qty = self.convert(qty, fromUnit=qtyUnit)

        self.qty = qty 

    # Overrides
    def __str__(self):
        return f"{self.qty} {self.measurement if self.measurement != None else "" } {self.displayName if self.displayName != None else self.name}"
    
    def __repr__(self):
        return f"{self.measurement if self.measurement != None else "" } {self.name}"

    def __eq__(self, value):
        if type(value) == str:
            return self.name == value
        if type(value) == dict:
            return self.name == value.get("name", value.get("ingredient", None))
        if type(value) == Ingredient:
            return self.name == value.name

        return self.name == value
    

    # Init functions
    def __set_attributes__(self, initData: dict):
        if initData:
            # Check if the ingredient is in the database
            if self.db.query(f"SELECT * FROM ingredients WHERE name = '{self.name.lower()}'") != []:
                raise Exception(f"Ingredient {self.name} already found in the database")
            self.__post_init_to_db__(initData)
        else:
            self.__get_from_db__()

    def __post_init_to_db__(self, initData: dict):
        '''This function is called after the object is created to store the data in the database'''
        # Validate and set the class attributes first then store in the database
        self.displayName      = initData.get("displayName", self.name)
        self.measurement      = initData.get("measurement", None)      
        self.size             = initData.get("size", None)
        self.rawStorage       = initData.get("rawStorage", None)
        self.processedStorage = initData.get("processedStorage", None)
        self.shelfLife        = initData.get("shelfLife", 0)
        self.notes            = initData.get("notes", None)
        self.tags             = initData.get("tags", None)
        self.category         = initData.get("category", None)
        self.subcategory      = initData.get("subcategory", None)
        self.kosher           = initData.get("kosher", None)
        self.conversions      = initData.get("conversions", {})
        self.__add_to_db__()

    def __get_from_db__(self):
        '''Get the ingredient from the database'''
        size = f"AND size = '{self.size}'" if self.size else ""
        _dict = self.db.query(f"SELECT * FROM ingredients WHERE name = '{self.name.lower()}' {size}")
        if len(_dict) > 0:
            _dict = _dict[0]
            for k,v in _dict.items():
                setattr(self, k, v)
            self.conversions = self.__get_conversions__()
        else:
            raise Exception(f"Ingredient {self.name} not found in the database")

    # Methods
    def convert(self, qty=None, toUnit=None, fromUnit=None):
        '''Convert the qty to the toUnit from the fromUnit. 
           - If qty is not provided then the class qty is used
           - If toUnit is not provided then the class measurement is used
           - If fromUnit is not provided then the class measurement is used'''
        
        qty = qty if qty != None else self.qty
        if qty == None:
            raise Exception("No quantity to convert")

        # If converting from a unit the final calculation will vary
        convertingFrom = True if fromUnit else False

        # set the conversion measures based on the from and to units
        fromMeasure = self.db.query(f"SELECT * FROM measures WHERE abbreviation = '{fromUnit if fromUnit else self.measurement}'")
        if len(fromMeasure) == 0:
            raise Exception("Convert from unit not found in measures table")
        toMeasure = self.db.query(f"SELECT * FROM measures WHERE abbreviation = '{toUnit if toUnit else self.measurement}'")
        if len(toMeasure) == 0:
            raise Exception("Convert to unit not found in measures table")
        fromMeasure = fromMeasure[0]
        toMeasure = toMeasure[0]

        # If they are the same unit then return the qty
        if fromMeasure['name'] == toMeasure['name']:
            return qty

        # The from factor will be used in each case so get it here to save the visual clutter
        fromFactor = self.db.query(f"SELECT factor from conversions WHERE name = 'basic' AND fromMeasure = '{fromUnit if fromUnit else self.measurement}' ")[0]['factor']

        # If we are converting within the same type (mass/volume) then use the basic conversion factor
        if fromMeasure['type'] == toMeasure['type']:
            toFactor = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{ toMeasure['abbreviation']}'")[0]['factor']
            return qty * (fromFactor / toFactor)


        # If the conversions are not set then get them from the database
        if self.conversions == None:
            self.conversions = self.__get_conversions__()

        # If the fromUnit is in the conversions then use it
        if toUnit in self.conversions:
            if fromMeasure['system'] == 'imperial':
                fromFactor  = 1
            toFactor  = self.conversions[toUnit]

            return qty * (fromFactor / toFactor)
        else:
            # If the measures are different types then 
            # - set the factor with the known conversion to the base unit
            # - determine how many fromUnits are in the known unit
            # - adjust the factor by the above calculation
            for unit in self.conversions:
                unitMeasure = self.db.query(f"SELECT * FROM measures WHERE abbreviation = '{unit}'")[0]
                knownUnitName = unit
                if unitMeasure['type'] == toMeasure['type']:
                    break

            knownValue = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{ knownUnitName }'")[0]['factor']
            if convertingFrom:
                conversionValue = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{ toUnit if toUnit else self.measurement}' ")[0]['factor']
            else:
                conversionValue = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{ toUnit if toUnit else fromUnit }' ")[0]['factor']
            modifier = knownValue / conversionValue
            toFactor = self.conversions[knownUnitName] / modifier

            if convertingFrom:
                return qty * (fromFactor * toFactor)
   
            return qty * (fromFactor / toFactor)

    # Private methods
    def __add_to_db__(self) -> None:
        '''Store the ingredient in the database'''
        _dict = {**self.__dict__} # deep copy

        # Conversions are stored in a separate table and must be removed first
        if "conversions" in _dict:
            self.__store_conversions__(self.name, _dict.pop("conversions"))

        # Get field names from the database
        fields = [ x['name'] for x in self.db.get_table_fields("ingredients")]

        # Remove keys not in the database fields    
        for k in list(_dict.keys()):
            if k not in fields:
                _dict.pop(k)

        self.db.insert("ingredients", _dict)

    def __store_conversions__(self, name: str, conversions: dict) -> None:
        '''Store the conversions in the database
            - conversions are done against the base unit and measurement
        '''
        for unit, value in self.conversions.items():
            self.db.insert("conversions", {"name":self.name, "isServings":False, "fromMeasure":unit, "factor":value})

    def __get_conversions__(self) -> dict:
        '''Get the conversions from the database'''
        results = self.db.query(f"SELECT * FROM conversions WHERE name = '{self.name.lower()}'")
        if len(results) == 0:
            raise Exception("No conversions available for this ingredient")
        return {x["fromMeasure"]:x["factor"] for x in results}