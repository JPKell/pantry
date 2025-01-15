from .database import db

from .ingredients import Ingredient


class Recipe:
    def __init__(self, 
                name: str, 
                servingQty=None,    # How many servings the recipe should yield. Different than yield. 
                                    # eg 1 loaf is the yeild but 12 slices is the servingQty 
                servingUnit=None,   # each, cup, g, etc.
                yieldQty=None,      # How many loaves, cakes, etc. Many times this will mirror the servingQty
                                    # but not always. eg 1 batch of cookies yields 24 cookies but the servingQty
                                    # could be 1 cookie. 
                                    # While 1 sausage yields 1 sausage and the servingQty would be 1 sausage
                yieldUnit=None,    # loaf, cake, cup, g etc.
                initData=None,      # A dictionary of recipe data to initialize the recipe and write to the database
                scale=1,            # Scale the recipe by this factor
                db=db
                ): 
        self.db = db
        self._scale = scale
        self.name = name

        ######################
        # These attributes are stored in the database and will
        # be set from the database if initData is None
        self.id = -1
        self.ingredients  = []
        self.preheat      = ""
        self.preheatTemp  = 0
        self.preheatUnit  = ""
        self.prepareAhead = ""
        self.servings     = 0  # Servings is the number of servings per yield e.g. 8 slices, 12 slices
        self.servingUnit  = "" # e.g. slice, cup, bowl, 
        self.steps        = []
        self.times        = {}
        self.yields       = 0  # Yield is the total recipe yield e.g. 1 loaf, 1 cake, 1 batch
        self.yieldUnit    = ""

        ## Metadata
        self.category           = ""
        self.kosher             = ""
        self.notes              = ""
        self.servingConversions = {}
        self.subcategory        = ""
        self.tags               = []
        self.yieldConversions   = {} # Conversion factors for the yield units

        self.__set_attributes__(initData)

        # If servingQty is provided then scale the recipe to the servingQty
        if servingQty or yieldQty:
            self.__scale_recipe__(servingQty, servingUnit, yieldQty, yieldUnit)


    ## Init methods
    def __set_attributes__(self, initData: dict):
        if initData:
            self.__post_initData_to_db__(initData)
        else:
            self.__set_from_db__()

    @property
    def scale(self):
        return self._scale
    
    @scale.setter
    def scale(self, value):
        if value <= 0:
            raise ValueError("Scale must be greater than 0")
        self._scale = value
        # Init the ingredients or it will be multiplied by the scale again
        self.__set_from_db__()
        self.yields *= value
        self.servings *= value

        for ingredient in self.ingredients:
            if isinstance(ingredient, Recipe):
                ingredient.scale *= value
            else:
                ingredient.qty *= value
            

    ## Private methods
    def __post_initData_to_db__(self, initData: dict):
        '''This function is called after the object is created to store the data in the database'''
        # Validate and set the class attributes first then store in the database
        self.ingredients  = initData.get("ingredients", [])
        self.preheat      = initData.get("preheat", None)
        self.preheatTemp  = initData.get("preheatTemp", None)
        self.preheatUnit  = initData.get("preheatUnit", None)
        self.prepareAhead = initData.get("prepareAhead", None)
        self.servings     = initData.get("servings", 0)
        self.servingUnit  = initData.get("servingUnit", None)
        self.steps        = initData.get("steps", [])
        self.times        = initData.get("times", {})    
        self.yields       = initData.get("yields", 0)
        self.yieldUnit    = initData.get("yieldUnit", None)
        ## Metadata
        self.category    = initData.get("category", "")
        self.kosher      = initData.get("kosher", "")
        self.notes       = initData.get("notes", None)
        self.subcategory = initData.get("subcategory", "")
        self.tags        = initData.get("tags", [])
        self.servingConversions = initData.get("servingConversions", {})
        self.yieldConversions = initData.get("yieldConversions", {})
        self.__add_to_db__()

    def __add_to_db__(self):
        '''Add the recipe to the database'''
        _dict = {**self.__dict__}
        # Remove unwanted attributes
        fields = [ x['name'] for x in self.db.get_table_fields("recipes")]

        for key in list(_dict.keys()):
            if key not in fields:
                _dict.pop(key)
        _dict.pop("id")

        self.db.insert("recipes", _dict)

        # Id is autoincremented so we need to get it from the database after adding it
        self.id = self.db.query(f"SELECT id FROM recipes WHERE name = '{self.name.replace("'", "''")}'")[0]["id"]
        
        for ingredient in self.ingredients:
            # Ingredients can be either a Recipe or an Ingredient and need to retrive the data differently
            if isinstance(ingredient, Recipe):
                self.db.execute(f"INSERT INTO recipe_ingredients (recipe_id, ingredient, qty, isRecipe) VALUES ({self.id}, '{ingredient.name.replace("'", "''")}',  {ingredient.scale}, 1)")
            else:
                prep = "NULL"
                if ingredient.prep:
                    prep = f"'{ingredient.prep}'"
                self.db.execute(f"INSERT INTO recipe_ingredients (recipe_id, ingredient, prep, qty, isRecipe) VALUES ({self.id}, '{ingredient.name.replace("'", "''")}', {prep}, {ingredient.qty}, 0)")
        
        
        for i, step in enumerate(self.steps):
            self.db.execute(f"INSERT INTO recipe_steps (recipe_id, step, description) VALUES ({self.id}, {i+1}, '{step.replace("'", "''")}')")
        
        for tag in self.tags:
            self.db.execute(f"INSERT INTO recipe_tags (recipe_id, tag) VALUES ({self.id}, '{tag.replace("'", "''")}')")

        i = 0
        for name, times in self.times.items():
            i += 1
            self.db.execute(f"INSERT INTO recipe_times (recipe_id, time, step, step) VALUES ({self.id}, '{times}', '{name.replace("'", "''")}', {i})")

        if self.servingConversions:
            for key, value in self.servingConversions.items():
                self.db.execute(f"INSERT INTO conversions (name, fromMeasure, factor, isServings) VALUES ('{self.name}', '{key}', {value}, 1)")

        if self.yieldConversions:
            for key, value in self.yieldConversions.items():
                self.db.execute(f"INSERT INTO conversions (name, fromMeasure, factor, isServings) VALUES ('{self.name}', '{key}', {value}, 0)")
        
    def __set_from_db__(self):
        '''Get the recipe from the database'''
        _dict = self.db.query(f"SELECT * FROM recipes WHERE name = '{self.name.replace("'", "''")}'")
        if len(_dict) == 0:
            raise Exception(f"Recipe {self.name} not found in the database")

        _dict = _dict[0]
        for k,v in _dict.items():
            setattr(self, k, v)

        ingredients = self.db.query(f"SELECT * FROM recipe_ingredients WHERE recipe_id = {self.id}")
        self.ingredients = []
        if len(ingredients) == 0:
            raise Exception(f"Recipe {self.name} has no ingredients")
        for ingredient in ingredients:
            if ingredient["isRecipe"] == 1:
                recipe = Recipe(ingredient["ingredient"])
                recipe.scale = ingredient["qty"]
                self.ingredients.append(recipe)
            else:
                self.ingredients.append(Ingredient(ingredient["ingredient"], qty=ingredient["qty"], prep=ingredient["prep"]))

        steps = self.db.query(f"SELECT description FROM recipe_steps WHERE recipe_id = {self.id}")
        if len(steps) == 0:
            raise Exception(f"Recipe {self.name} has no steps")
        self.steps = [s["description"] for s in steps]
    
        tags = self.db.query(f"SELECT tag FROM recipe_tags WHERE recipe_id = {self.id}")
        if len(tags) > 0:
            self.tags = [t["tag"] for t in tags]

        times = self.db.query(f"SELECT * FROM recipe_times WHERE recipe_id = {self.id}")
        if len(times) > 0:
            self.times = {t["step"]: t["time"] for t in times}

        conversions = self.db.query(f"SELECT * FROM conversions WHERE name = '{self.name.replace("'", "''")}'")
        if len(conversions) > 0:
            for c in conversions:
                if c['isServings']:
                    self.servingConversions.update({c["fromMeasure"]: c["factor"]}) 
                else:
                    self.yieldConversions.update({c["fromMeasure"]: c["factor"]})
  
    def __scale_recipe__(self, servingQty=None, servingUnit=None, yieldQty=None, yieldUnits=None):
        '''Scale the recipe to the servingQty'''
        # After this block we can be assured we are working with only one area of scaling
        if servingQty and yieldQty:
            raise ValueError("Only provide servingQty or yieldQty, not both")
        if servingUnit and yieldUnits:
            raise ValueError("Only provide servingUnit or yieldUnits, not both")
        if servingQty and yieldUnits:
            raise ValueError("Cannot scale by servingQty and yieldUnits")
        if yieldQty and servingUnit:
            raise ValueError("Cannot scale by yieldQty and servingUnit")

        # Clear out the easy ones first
        # Assume that if no unit provided user is scaling by the default unit for the recipe
        if servingQty and not servingUnit: 
            self.scale = servingQty/self.servings
            return

        if yieldQty and not yieldUnits:
            self.scale = yieldQty/self.yields
            return
        
        # Get all the units and measures at the start
        toQty = servingQty if servingQty else yieldQty
        toUnit = servingUnit if servingUnit else yieldUnits
        fromQty = self.servings if servingQty else self.yields
        fromUnit = self.servingUnit if servingUnit else self.yieldUnit

        # Get more details on the measures
        toMeasure = self.db.queryOne(f"SELECT * FROM measures WHERE abbreviation = '{toUnit}'")
        fromMeasure = self.db.queryOne(f"SELECT * FROM measures WHERE abbreviation = '{fromUnit}'")

        if not toMeasure:
            raise ValueError(f"Convert to unit {toUnit} not found in the database")
        if not fromMeasure:
            raise ValueError(f"Convert from unit {fromUnit} not found in the database")
        
        # If the measures are the same then we can scale by the qty
        if toMeasure["name"] == fromMeasure["name"]:
            self.scale = toQty/fromQty
            return
        

        # If the measures are of the same type (mass/volume) then we can convert the measures
        # with basic conversion factors
        if toMeasure["type"] == fromMeasure["type"]:
            fromFactor = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{fromUnit}'")[0]['factor']
            toFactor = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{toUnit}'")[0]['factor']

            self.scale = toQty / fromQty * fromFactor * toFactor
            return 

        # If the measure exists in the conversions table then we can use that
        if servingQty and toUnit in self.servingConversions:
            self.scale = servingQty/self.servings * self.servingConversions[toUnit]
            return
        if yieldQty and yieldUnits in self.yieldConversions:
            
            self.scale = yieldQty/self.yields * self.yieldConversions[yieldUnits]
            return

        # If we get here then we need to convert the measures to a common measure
        # and then scale the recipe
        # Get the common measure
        if servingQty:
            conversions = self.servingConversions
        else:
            conversions = self.yieldConversions

        if not conversions:
            raise ValueError(f"No conversions found for {self.name}")

        foundMatchingType = False
        for unit in conversions:
            unitMeasure = self.db.query(f"SELECT * FROM measures WHERE abbreviation = '{unit}'")[0]
            knownUnitName = unit
            if unitMeasure['type'] == toMeasure['type']:
                foundMatchingType = True
                break
        if not foundMatchingType:
            raise ValueError(f"No matching conversion type (volume/mass) found for {self.name}")

        knownValue = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{ knownUnitName }'")[0]['factor']
        # if convertingFrom:
        conversionValue = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{ toUnit }' ")[0]['factor']
        # else:
        #     conversionValue = self.db.query(f"SELECT factor FROM conversions WHERE name = 'basic' AND fromMeasure = '{ toUnit if toUnit else fromUnit }' ")[0]['factor']
        modifier = knownValue / conversionValue
        toFactor = conversions[knownUnitName] / modifier

        # if convertingFrom:
        self.scale = toQty/fromQty * toFactor

