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

mirepoix = Recipe("mirepoix")
print(mirepoix.name, mirepoix.yields, mirepoix.yieldUnit, mirepoix.servings, mirepoix.servingUnit, mirepoix.scale)

mirepoix = Recipe("mirepoix", yieldQty=800)
print(mirepoix.name, mirepoix.yields, mirepoix.yieldUnit, mirepoix.servings, mirepoix.servingUnit, mirepoix.scale)

mirepoix = Recipe("mirepoix", yieldQty=0.8, yieldUnit="kg")
print(mirepoix.name, mirepoix.yields, mirepoix.yieldUnit, mirepoix.servings, mirepoix.servingUnit, mirepoix.scale)

print(mirepoix.ingredient.servings, mirepoix.ingredient.servingUnit, mirepoix.ingredient.scale)