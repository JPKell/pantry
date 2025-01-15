''' 
This is an init file to create the initial database tables and populate them with basic data. 
This is a one-time operation. 
'''
from modules.database import db 
from constants import *

from modules.ingredients import Ingredient
from modules.recipe import Recipe
from modules.pantry import Pantry
from modules.market import Market
from modules.chef import Chef
from modules.converter import Converter

pantry = Pantry()
chef = Chef(pantry)


initData = {
        "preheat": "preheat oven",
        "preheatTemp": 425,
        "yields":1,
        "yieldUnit":"loaf",
        "yieldConversions": {
            "g": 1/100,
        },  
        "servings":10,
        "servingUnit":"slice",
        "servingsConversion": {
            "g": 1/10,
        },
        "servingsConversionUnit":"g",
        "category":"bread",
        "subcategory":"test",
        "kosher": "pareve",
        "tags": ["bread", "test"],
        "ingredients": [Ingredient("ap flour", 100), ],
        "steps": [
            "Step 1: Mix the ingredients",
            "Step 2: Let the dough rise",
            "Step 3: Shape the dough",
            "Step 4: Let the dough rise again",
            "Step 5: Bake the bread"
        ]
        }
# Recipe("test bread", initData=initData)

# bb = Recipe("baba ghanoush", db=db)
# print(chef.totalRecipePrice(bb))
# for x, v in chef.detailedRecipePrice(bb).items():
#     print(x,v )

# from test.init_db import test_db
# r = Ingredient("ap flour", db=test_db)

# for k,v in r.__dict__.items():
#     print(k,v)

