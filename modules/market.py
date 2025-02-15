'''

Each ingredient is available at multiple markets, each with a different price.
There may be times you will pay more to get everything from one market, at other
times you may save money by shopping at multiple markets. So the market should 
be written to switch priorities. Less stops or lowest price.


It will read the vendor files from data/vendors and create a list of markets to check for prices

'''
from .database import db
from .ingredients import Ingredient

class Market:
    def __init__(self, name: str, initData:dict=None, db=db):
        self.db          = db
        self.name        = name
        self.location    = ""
        self.distance    = 0.0  
        self.notes       = ""
        self.priority    = 0    # 0 is the lowest priority
        self.ingredients = []
        self.search      = "" # The URL search string for the market
        self.__set_attributes__(initData)

    ## Overload operators
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, value):
        return self.name == value.name
    
    ## Init functions
    def __set_attributes__(self, initData: dict):
        if initData:
            self.__post_init_to_db__(initData)
        else:
            self.__get_from_db__()

    def __post_init_to_db__(self, initData: dict):
        '''This function is called after the object is created to store the data in the database'''
        # Validate and set the class attributes first then store in the database
        self.location    = initData.get("location", "")
        self.distance    = initData.get("distance", 0.0)
        self.notes       = initData.get("notes", "")
        self.priority    = initData.get("priority", 0)
        self.ingredients = initData.get("ingredients", [])
        self.search      = initData.get("search", "")
        self.__add_to_db__()

    def __get_from_db__(self):
        '''Get the market from the database'''
        _dict = self.db.query(f"SELECT * FROM markets WHERE name = '{self.name.lower()}'")
        if len(_dict) > 0:
            _dict = _dict[0]
            for k,v in _dict.items():
                setattr(self, k, v)
        else:
            raise Exception(f"Market {self.name} not found in the database")

    ## Public methods
    def getPrice(self, ingredient: Ingredient) -> dict:
        '''Get the price of the ingredient at the market'''
        _dict = self.db.queryOne(f"SELECT * FROM market_ingredients WHERE market = '{self.name.lower()}' AND ingredient = '{ingredient.name.lower()}'")
        if not _dict:
            return None
        
        factor = self.db.query(f"SELECT * FROM conversions WHERE name = 'basic' AND fromMeasure = '{ _dict['priceUnit'] }'")
        if not factor:
            raise ValueError(f"Conversion not found for {_dict['priceUnit']}")
        factor = factor[0]['factor']
        try:
            _dict['total'] = ingredient.convert(toUnit=_dict['priceUnit']) * (_dict['price'] / _dict['size'] )# / factor

            return _dict
        except:
            _dict['total'] = None
            return _dict


    ## Private methods
    def __add_to_db__(self):
        '''Add the market to the database'''
        _dict = {**self.__dict__}
        ingredients = _dict.pop("ingredients")
        fields = [ x['name'] for x in self.db.get_table_fields("markets")]
        for key in list(_dict.keys()):
            if key not in fields:
                _dict.pop(key)

        self.db.insert("markets", _dict)

        if len(ingredients) > 0:
            for name, data in ingredients.items():
                data['ingredient'] = name.replace("'", "''")
                data['market'] = self.name.replace("'", "''")
                

                self.db.insert("market_ingredients", data)

