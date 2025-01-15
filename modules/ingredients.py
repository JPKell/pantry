from .database import db
from modules.converter import Converter

class Ingredient:
    '''
    An ingredient name is unique and is the key to the database.
    The ingredient is stored in the database and can be retrieved by name.

    Base measures are always metric so the conversions only need to go one way. Plus metric is way better
    '''
    def __init__(self, name: str, qty:int=None, qtyUnit:str=None, prep=None, initData:dict=None, db=db):
        self.db = db # This is the database connection, it is passed in so that the class can be tested
        self._converter = Converter()

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
        self.displayName:str      = None    # name for display
        self._unit:str            = None    # gram, ml, each, etc.
        self.rawStorage:str       = None    # refrigerator, pantry, etc.
        self.processedStorage:str = None    # refrigerator, pantry, etc.
        self.shelfLife:int        = None    # in days
        self.notes:str            = None    #
        self.tags:str             = None    # tags for searching
        self.category:str         = None    # protein, vegetable, etc.
        self.subcategory:str      = None    # beef, tofu, leafy green, tuber, etc.
        self.kosher:str           = None    # flesh, dairy, pareve, treif
        self.knownConversions     = {}    # conversions to base unit
        self.alternatives  = []    # list of alternative ingredients

        ######################
        # Instance attributes
        #   These are not stored in the database but are used for the instance 
        #   to carry details about the ingredients state
    
        self.purchasePrice = 0     # price paid of the ingredient
        self.prep        = ""    # how the ingredient is prepared. Used for recipes
        self.displayUnit = ""    # override the unit to display the qty in.

        self.__set_attributes__(initData)
        
        if qtyUnit != None: # there may be an inbound conversion to do before setting the qty 
            qty = self.convert(qty, fromUnit=qtyUnit)
        self._qty = qty 
        
        ## Added new, make sure to populate changes in __set_attributes__ and __get_from_db__



    # Overrides
    def __str__(self):
        return f"{self._qty}{self.unit if self.unit != None else "" } of {self.displayName if self.displayName != None else self.name}"
    
    def __repr__(self):
        return f"{self.unit if self.unit != None else "" } {self.name}"

    def __eq__(self, value):
        if type(value) == str:
            return self.name == value
        if type(value) == dict:
            return self.name == value.get("name", value.get("ingredient", None))
        if type(value) == Ingredient:
            return self.name == value.name

        return self.name == value
    
    @property
    def unit(self):
        '''converts before returning the measurement if displayUnit is set'''
        if self.displayUnit:
            return self.displayUnit
        return self._unit
    
    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def qty(self):
        '''converts before returning the qty if displayUnit is set'''
        if self.displayUnit:
            return self.convert(self._qty, toUnit=self.displayUnit)
        return self._qty
    
    @qty.setter
    def qty(self, value):
        self._qty = value



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

        if len(initData) > 0:
            for k,v in initData.items():
                setattr(self, k, v)
        # handle the class properties separately
        self._unit      = initData.get("unit", None)      

        self._converter.knownConversions = self.knownConversions
        self._converter.baseUnit = self.unit
        self.__add_to_db__()

    def __get_from_db__(self):
        '''Get the ingredient from the database'''
        _dict = self.db.queryOne(f"SELECT * FROM ingredients WHERE name = '{self.name.lower()}';")
        if len(_dict) > 0:
            for k,v in _dict.items():
                setattr(self, k, v)
            # handle the class properties separately
            self._unit = _dict.get("unit", None)

            alts = self.db.query(f"SELECT * FROM ingredient_alternatives WHERE ingredient = '{self.name.lower()}'")
            self.alternatives = [x['alternative'] for x in alts]
            self.knownConversions = self.__get_conversions__()
            self._converter.knownConversions = self.knownConversions
            self._converter.baseUnit = self.unit
        else:
            raise Exception(f"Ingredient {self.name} not found in the database")

    # Methods
    def convert(self, qty=None, toUnit=None, fromUnit=None):
        '''Convert the qty to the toUnit from the fromUnit. 
           - If qty is not provided then the class qty is used
           - If toUnit is not provided then the class measurement is used
           - If fromUnit is not provided then the class measurement is used'''
        if qty == None:
            qty = self._qty
        if qty == None:
            raise Exception("No qty provided")
        return self._converter.convert(qty, toUnit=toUnit, fromUnit=fromUnit)

    # Private methods
    def __add_to_db__(self) -> None:
        '''Store the ingredient in the database'''
        _dict = {**self.__dict__} # deep copy
        _dict['unit'] = self._unit

        # Conversions are stored in a separate table and must be removed first
        if "knownConversions" in _dict:
            self.__store_conversions__(self.name, _dict.pop("knownConversions"))

        if "alternatives" in _dict:
            for alt in _dict.pop("alternatives"):
                self.db.insert("ingredient_alternatives", {"ingredient":self.name, "alternative":alt})

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
        for unit, value in self.knownConversions.items():
            self.db.insert("conversions", {"name":self.name, "isServings":False, "fromMeasure":unit, "factor":value})

    def __get_conversions__(self) -> dict:
        '''Get the conversions from the database'''
        results = self.db.query(f"SELECT * FROM conversions WHERE name = '{self.name.lower()}'")

        if len(results) == 0:
            return {}
            # raise Exception("No conversions available for this ingredient")
        return {x["fromMeasure"]:x["factor"] for x in results}