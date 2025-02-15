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
        "displayName":"lemon juice",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"refrigerator", 
        "shelfLife":90, 
        "category":"liquid", 
        "subcategory":"juice", 
        "kosher":"pareve",
        "tags": "",
        "knownConversions": {
            "g": 244/CUP,      
        }
    }
Ingredient("lemon juice", initData=initData)

# # Add a column to recipe_ingredients table called recipePart

initData = {
        "yields":450,
        "yieldUnit":"ml",
        "servings":4,
        "servingUnit":"each",
        "category":"protein",
        "subcategory":"tofu",
        "tags": ["sesame", "crispy", "baked"],      
        "kosher": "pareve",
        "ingredients": [
            Ingredient("canned chickpeas", 540, qtyUnit='ml'),
            Ingredient("lemon juice", 75, qtyUnit='ml'),
            Ingredient("tahini", 75, qtyUnit='ml', prep="stirred"),
            Ingredient("garlic", 2, qtyUnit='clove'),
            Ingredient("olive oil", 40, qtyUnit='ml'), 
            Ingredient("cumin", 0.5, qtyUnit='tsp'), 
            Ingredient("water", 50, qtyUnit='ml', prep="cold"), 
            Ingredient("salt", 1, qtyUnit='tsp', prep="or more to taste"), 
        ],
        "steps": [
            "In food processor combine tahini and lemon juice and process for 1 minute, scrape sides and bottom of bowl then process for 30 seconds more",
            "Add the olive oil, minced garlic, cumin, and salt to the whipped tahini and lemon juice. Process for 30 seconds, scrape sides and bottom of bowl then process another 30 seconds or until well blended",
            "Open, drain, and rinse chickpeas. Add half of the chickpeas to the food processor and process for 1 minute. Scrape sides and bottom of bowl, add remaining chickpeas and process for 1-2 minutes or until thick and smooth",
            "If hummus is too thick or still has tiny bits of chickpeas, with the food processor turned on, slowly add 2-3 tablespoons of water until you reach the perfect consistency",
        ],
        "times": {
            "active": "10-15 minutes",
            "cook": "30-35 minutes",
        }
    }

Recipe("crispy baked sesame tofu", initData=initData)

