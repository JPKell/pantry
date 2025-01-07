''' 
This is an init file to create the initial database tables and populate them with basic data. 
This is a one-time operation. 
'''
from modules.database import db 
from constants import *

######################
# Initialize the database
from initDb import initDb
initDb(db)


measures = [
    {"abbreviation": "tsp",   "name": "teaspoon",    "type":"volume","system": "imperial"},
    {"abbreviation": "tbsp",  "name": "tablespoon",  "type":"volume","system": "imperial"},
    {"abbreviation": "cup",   "name": "cup",         "type":"volume","system": "imperial"},
    {"abbreviation": "oz",    "name": "ounce",       "type":"mass",  "system": "imperial"},
    {"abbreviation": "lb",    "name": "pound",       "type":"mass",  "system": "imperial"},
    {"abbreviation": "g",     "name": "gram",        "type":"mass",  "system": "metric"},
    {"abbreviation": "mg",    "name": "miligram",    "type":"mass",  "system": "metric"},
    {"abbreviation": "kg",    "name": "kilogram",    "type":"mass",  "system": "metric"},
    {"abbreviation": "ml",    "name": "milliliter",  "type":"volume","system": "metric"},
    {"abbreviation": "l",     "name": "liter",       "type":"volume","system": "metric"},
    {"abbreviation": "qt",    "name": "quart",       "type":"volume","system": "imperial"},
    {"abbreviation": "gal",   "name": "gallon",      "type":"volume","system": "imperial"}, # US gallon
    {"abbreviation": "fl oz", "name": "fluid ounce", "type":"volume","system": "imperial"},
    {'abbreviation': 'each',  'name': 'each',        'type':'count', 'system': 'metric'},
    {"abbreviation": "slice", "name": "slice",       "type":"count", "system": "metric"},
    {"abbreviation": "loaf",  "name": "loaf",        "type":"count", "system": "metric"},
    {"abbreviation": "clove", "name": "clove",       "type":"count", "system": "metric"},
    {"abbreviation": "whole", "name": "whole",       "type":"count", "system": "metric"},
    {"abbreviation": "bunch", "name": "bunch",       "type":"count", "system": "metric"},
    {"abbreviation": "stick", "name": "stick",       "type":"count", "system": "metric"},
    {"abbreviation": "sprig", "name": "sprig",       "type":"count", "system": "metric"},
]

print("--Inserting measures--")
for measure in measures:
    db.insert("measures", measure)

######################
# Conversion table populate with initial data
             

# Conversions are done based on their default unit of mesurement
# flour is measured in grams
#
# So the to meaure is known in the ingredient table and does not need to be stored here
#
# These basic conversions are used for conversions that are clean unit conversions
# ie. metric to imerial or vice versa. Base is always metric
basicConversions = [
    {"name": "basic","isServings": False , "fromMeasure": "lb", "factor": LB},
    {"name": "basic","isServings": False , "fromMeasure": "oz", "factor": OZ},
    {"name": "basic","isServings": False , "fromMeasure": "tsp", "factor": TSP},
    {"name": "basic","isServings": False , "fromMeasure": "tbsp", "factor": TBSP},
    {"name": "basic","isServings": False , "fromMeasure": "cup", "factor": CUP},
    {"name": "basic","isServings": False , "fromMeasure": "ml", "factor": ML},
    {"name": "basic","isServings": False , "fromMeasure": "l", "factor": L},
    {"name": "basic","isServings": False , "fromMeasure": "gal", "factor": GAL},
    {"name": "basic","isServings": False , "fromMeasure": "qt", "factor": QT},
    {"name": "basic","isServings": False , "fromMeasure": "fl oz", "factor": FL_OZ},
    {"name": "basic","isServings": False , "fromMeasure": "mg", "factor": MG},
    {"name": "basic","isServings": False , "fromMeasure": "g", "factor": G},
    {"name": "basic","isServings": False , "fromMeasure": "kg", "factor": KG},
    {"name": "basic","isServings": False , "fromMeasure": "each", "factor": 1},
    {"name": "basic","isServings": False , "fromMeasure": "slice", "factor": 1},
    {"name": "basic","isServings": False , "fromMeasure": "loaf", "factor": 1},
    {"name": "basic","isServings": False , "fromMeasure": "clove", "factor": 1},
    {"name": "basic","isServings": False , "fromMeasure": "whole", "factor": 1},
    {"name": "basic","isServings": False , "fromMeasure": "bunch", "factor": 1},
    {"name": "basic","isServings": False , "fromMeasure": "stick", "factor": 1},
    {"name": "basic","isServings": False , "fromMeasure": "sprig", "factor": 1},

]

print("--Inserting basic conversions--")
for conversion in basicConversions:
    db.insert("conversions", conversion)

######################
# Create ingredient tables and populate with initial data


from initData.ingredients import initIngredients
from modules.ingredients import Ingredient

print("--Inserting ingredients--")
for name, data in initIngredients.items():
    Ingredient(name, initData=data)

######################
# Create the pantry table
from modules.pantry import Pantry
pantry = Pantry()

# Add some initial data to the pantry
print("--Inserting pantry data--")
pantry.addFood(Ingredient("ap flour", qty=12.5, qtyUnit="kg"))
pantry.addFood(Ingredient('apple cider vinegar', qty=750, qtyUnit='ml'))
pantry.addFood(Ingredient('arborio rice', qty=400, qtyUnit='g'))
pantry.addFood(Ingredient('avocado', qty=2))
pantry.addFood(Ingredient('baking soda', qty=1, qtyUnit='tbsp'))
pantry.addFood(Ingredient('baking powder', qty=1, qtyUnit='tbsp'))
pantry.addFood(Ingredient('balsamic vinegar', qty=300, qtyUnit='ml'))
pantry.addFood(Ingredient('brown sugar', qty=650, qtyUnit='g'))
pantry.addFood(Ingredient('cabbage', qty=600, qtyUnit='g'))
pantry.addFood(Ingredient('canned crushed tomatoes', qty=796, qtyUnit='ml'))
pantry.addFood(Ingredient('canned peas', qty=389, qtyUnit='ml'))
pantry.addFood(Ingredient('canned pineapple', qty=398, qtyUnit='ml'))
pantry.addFood(Ingredient('carrot', qty=1360, qtyUnit='g'))
pantry.addFood(Ingredient('celery', qty=450, qtyUnit='g'))
pantry.addFood(Ingredient('chickpea flour', qty=375, qtyUnit='g'))
pantry.addFood(Ingredient('cocoa powder', qty=300, qtyUnit='g'))
pantry.addFood(Ingredient('corn grits', qty=340, qtyUnit='g'))
pantry.addFood(Ingredient('cornmeal', qty=250, qtyUnit='g'))
pantry.addFood(Ingredient('dried cherries', qty=75, qtyUnit='g'))
pantry.addFood(Ingredient('dates', qty=300, qtyUnit='g'))
pantry.addFood(Ingredient('dry bean soup mix', qty=290, qtyUnit='g'))
pantry.addFood(Ingredient('dry black beans', qty=910, qtyUnit='g'))
pantry.addFood(Ingredient('dry black eyed beans', qty=550, qtyUnit='g'))
pantry.addFood(Ingredient('dry green lentils', qty=720, qtyUnit='g'))
pantry.addFood(Ingredient('dry kidney beans', qty=900, qtyUnit='g'))
pantry.addFood(Ingredient('dry pinto beans', qty=900, qtyUnit='g'))
pantry.addFood(Ingredient('dry red lentils', qty=900, qtyUnit='g'))
pantry.addFood(Ingredient('dry shitake mushrooms', qty=115, qtyUnit='g'))
pantry.addFood(Ingredient('dry spaghetti', qty=500, qtyUnit='g'))
pantry.addFood(Ingredient('extra firm tofu', qty=350, qtyUnit='g'))
pantry.addFood(Ingredient('fish sauce', qty=150, qtyUnit='ml'))
pantry.addFood(Ingredient('golden corn syrup', qty=80, qtyUnit='ml'))
pantry.addFood(Ingredient('grapeseed oil', qty=1400, qtyUnit='ml'))
pantry.addFood(Ingredient('honey', qty=0.5, qtyUnit='kg'))
pantry.addFood(Ingredient('instant coffee', qty=200, qtyUnit='g'))
pantry.addFood(Ingredient("instant dry yeast", qty=300))
pantry.addFood(Ingredient('instant noodles', qty=2))
pantry.addFood(Ingredient("lg egg", qty=12))
pantry.addFood(Ingredient('maldon salt', qty=230, qtyUnit='g'))
pantry.addFood(Ingredient('mandarin orange', qty=30))
pantry.addFood(Ingredient('mango puree', qty=370, qtyUnit='g'))
pantry.addFood(Ingredient('mayonnaise', qty=300, qtyUnit='ml'))
pantry.addFood(Ingredient('molasses', qty=200, qtyUnit='g'))
pantry.addFood(Ingredient('nutritional yeast', qty=2, qtyUnit='cup'))
pantry.addFood(Ingredient("olive oil", qty=1000))
pantry.addFood(Ingredient('panko', qty=90, qtyUnit='g'))
pantry.addFood(Ingredient('peanut butter', qty=2, qtyUnit='kg'))
pantry.addFood(Ingredient('popcorn kernels', qty=2, qtyUnit='cup'))
pantry.addFood(Ingredient('pumpkin seeds', qty=140, qtyUnit='g'))
pantry.addFood(Ingredient('raw almonds', qty=1, qtyUnit='kg'))
pantry.addFood(Ingredient('rolled oats', qty=700, qtyUnit='g'))
pantry.addFood(Ingredient('rye flour', qty=1, qtyUnit='kg'))
pantry.addFood(Ingredient("salt", qty=1, qtyUnit="kg"))
pantry.addFood(Ingredient('sesame oil', qty=500, qtyUnit='ml'))
pantry.addFood(Ingredient('sesame seeds', qty=2, qtyUnit='cup'))
pantry.addFood(Ingredient("sugar", qty=2.5, qtyUnit="kg"))
pantry.addFood(Ingredient('sunflower seeds', qty=50, qtyUnit='g'))
pantry.addFood(Ingredient('tabasco', qty=350, qtyUnit='ml'))
pantry.addFood(Ingredient('tortilla chips', qty=180))
pantry.addFood(Ingredient('vital wheat gluten', qty=400, qtyUnit='g'))
pantry.addFood(Ingredient('vanilla extract', qty=30, qtyUnit='ml'))
pantry.addFood(Ingredient('walnut pieces', qty=1.2, qtyUnit='kg'))
pantry.addFood(Ingredient("water", qty=10000000))
pantry.addFood(Ingredient('white rice', qty=8, qtyUnit='kg'))
pantry.addFood(Ingredient('whole coffee bean', qty=2, qtyUnit='lb'))
pantry.addFood(Ingredient('yellow mustard', qty=340, qtyUnit='ml'))
pantry.addFood(Ingredient('onion', qty=1.5, qtyUnit='kg'))
pantry.addFood(Ingredient('cinnamon', qty=150, qtyUnit='g'))
pantry.addFood(Ingredient('mustard seed', qty=31, qtyUnit='g'))
pantry.addFood(Ingredient('black pepper', qty=60, qtyUnit='g'))
pantry.addFood(Ingredient('ground tumeric', qty=400, qtyUnit='g'))
pantry.addFood(Ingredient('mustard powder', qty=110, qtyUnit='g'))
pantry.addFood(Ingredient('garlic powder', qty=160, qtyUnit='g'))
pantry.addFood(Ingredient('onion powder', qty=40, qtyUnit='g'))
pantry.addFood(Ingredient('sumac', qty=65, qtyUnit='g'))
pantry.addFood(Ingredient('allspice', qty=80, qtyUnit='g'))
pantry.addFood(Ingredient('ground ginger', qty=45, qtyUnit='g'))
pantry.addFood(Ingredient('black pepper', qty=125, qtyUnit='g'))
pantry.addFood(Ingredient('coriander', qty=65, qtyUnit='g'))
pantry.addFood(Ingredient('fennel seed', qty=260, qtyUnit='g'))
pantry.addFood(Ingredient('bay leaf', qty=10, qtyUnit='g'))
pantry.addFood(Ingredient('caraway', qty=65, qtyUnit='g'))
pantry.addFood(Ingredient('italian seasoning', qty=10, qtyUnit='g'))
pantry.addFood(Ingredient('dried dill', qty=40, qtyUnit='g'))
pantry.addFood(Ingredient('dried lime leaves', qty=25, qtyUnit='g'))
pantry.addFood(Ingredient('chili powder', qty=76, qtyUnit='g'))
pantry.addFood(Ingredient('dried oregano', qty=28, qtyUnit='g'))
pantry.addFood(Ingredient('cayenne powder', qty=65, qtyUnit='g'))
pantry.addFood(Ingredient('cumin', qty=80, qtyUnit='g'))
pantry.addFood(Ingredient('cloves', qty=120, qtyUnit='g'))
pantry.addFood(Ingredient('cardamom', qty=38, qtyUnit='g'))
pantry.addFood(Ingredient('star anise', qty=25, qtyUnit='g'))
pantry.addFood(Ingredient('anise seed', qty=75, qtyUnit='g'))
pantry.addFood(Ingredient('celery seed', qty=50, qtyUnit='g'))
pantry.addFood(Ingredient('celery salt', qty=150, qtyUnit='g'))
pantry.addFood(Ingredient('dried basil', qty=50, qtyUnit='g'))
pantry.addFood(Ingredient('curry powder', qty=450, qtyUnit='g'))
pantry.addFood(Ingredient('nutmeg', qty=50, qtyUnit='g'))
pantry.addFood(Ingredient('dried rosemary', qty=5, qtyUnit='g'))
pantry.addFood(Ingredient('ground tumeric', qty=10, qtyUnit='g'))





######################
# Insert the basic recipes. 
print("--Inserting recipe data--")
from modules.recipe import Recipe
from initData.baseRecipes import recipes

# Basic recipies use only ingredients and not other recipes
for name, data in recipes.items():
    Recipe(name, initData=data)

# Insert the compound recipes
# import must be after the base recipes are inserted
from initData.compoundRecipes import compoundRecipes

for name, data in compoundRecipes.items():
    Recipe(name, initData=data)

######################
# Insert the markets
from modules.market import Market
from initData.markets import markets

print("--Inserting markets--")

for name, data in markets.items():
    market = Market(name, initData=data)

print("--Done adding to database--")
print()

######################
## Test that everything works 

from modules.chef import Chef
chef = Chef(pantry)

print(f"Total pantry value is ${chef.totalPantryValue():.2f}")
menu = chef.menu()

pv = chef.detailedPantryValue()
for ingredient, data in pv.items():
    print(f"{ingredient:20} ... ${data['total']:.2f}")


printDetails = False
print()
print("Menu pricing")
for recipe, details in menu.items():
    print(f"{recipe.capitalize()}")
    print(f"{"":20}${details['totalPrice']:.2f} for {int(details['servings'])} servings" )
    print(f"{"":20}${details['servingPrice']:.2f} per {details['servingUnit']}")
    if printDetails:
        for k,v in details['detailedPrice'].items():
            print(f"\t{k:20} ... ${v['total']:.2f}")
    print()

