''' 
This is an init file to create the initial database tables and populate them with basic data. 
This is a one-time operation. 
'''
import os
from modules.database import Db
from constants import *

# remove the test database if it exists
if os.path.exists("test/test.db"):
    os.remove("test/test.db")
test_db = Db("test/test.db")

######################
# Create the measures table
test_db.create_table("measures",'''
    name TEXT PRIMARY KEY,
    abbreviation TEXT,
    system TEXT,        -- imperial or metric
    type TEXT           -- volume or mass
    ''')

measures = [
    {"abbreviation": "tsp",   "name": "teaspoon",    "type":"volume","system": "imperial"},
    {"abbreviation": "tbsp",  "name": "tablespoon",  "type":"volume","system": "imperial"},
    {"abbreviation": "cup",   "name": "cup",         "type":"volume","system": "imperial"},
    {"abbreviation": "oz",    "name": "ounce",       "type":"mass",  "system": "imperial"},
    {"abbreviation": "lb",    "name": "pound",       "type":"mass",  "system": "imperial"},
    {"abbreviation": "mg",    "name": "miligram",    "type":"mass",  "system": "metric"},
    {"abbreviation": "g",     "name": "gram",        "type":"mass",  "system": "metric"},
    {"abbreviation": "kg",    "name": "kilogram",    "type":"mass",  "system": "metric"},
    {"abbreviation": "ml",    "name": "milliliter",  "type":"volume","system": "metric"},
    {"abbreviation": "l",     "name": "liter",       "type":"volume","system": "metric"},
    {"abbreviation": "qt",    "name": "quart",       "type":"volume","system": "imperial"},
    {"abbreviation": "gal",   "name": "gallon",      "type":"volume","system": "imperial"}, # US gallon
    {"abbreviation": "fl oz", "name": "fluid ounce", "type":"volume","system": "imperial"},
    {'abbreviation': 'each',  'name': 'each',        'type':'count', 'system': 'metric'},
    {"abbreviation": "slice", "name": "slice",       "type":"count", "system": "metric"},
    {"abbreviation": "loaf",  "name": "loaf",        "type":"count", "system": "metric"},
]

for measure in measures:
    test_db.insert("measures", measure)

######################
# Create the conversion table and populate with initial data

test_db.create_table("conversions",'''
    name TEXT,
    fromMeasure TEXT,
    isServings BOOLEAN,
    factor REAL,
    PRIMARY KEY (name, fromMeasure, isServings)
    ''')              

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
]

for conversion in basicConversions:
    test_db.insert("conversions", conversion)

######################
# Create ingredient tables and populate with initial data
test_db.create_table("ingredients",'''
    name TEXT,
    displayName TEXT,
    measurement TEXT,
    size TEXT,
    rawStorage TEXT,
    processedStorage TEXT,
    shelfLife INTEGER,
    notes TEXT,
    tags TEXT,
    category TEXT,
    subcategory TEXT,
    kosher TEXT,
    PRIMARY KEY (name, size)
    ''')

from modules.ingredients import Ingredient
data = {
        "displayName":"all-purpose flour",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature",
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"flour", 
        "kosher":"pareve",
        "notes":"keep dry",
        "tags": "baking, thickening, breading, coating, dredging, roux",
        "conversions": {
            "cup": 120,       
        }
    }

Ingredient('ap flour', initData=data, db=test_db)

data = {
        "displayName":"salt",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"spice", 
        "subcategory":"salt", 
        "kosher":"pareve",
        "tags": "seasoning, baking, curing, preserving, pickling, brining",
        "conversions": {
            "cup": 273,       
        }
    }
Ingredient('salt', initData=data, db=test_db)


data = {
        "displayName":"water",
        "measurement":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"liquid", 
        "subcategory":"water", 
        "kosher":"pareve",
        "tags": "beverage",
        "conversions": {
            "g": 1,       
        }
    }
Ingredient('water', initData=data, db=test_db)


data =  {
        "displayName":"instant dry yeast",
        "measurement":"g", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"yeast", 
        "kosher":"pareve",
        "notes":"quick-rise, keep dry and refrigerated",
        "tags": "bread, baking",
        "conversions": {
            "cup": 148.8,       
        }
    }
Ingredient('instant dry yeast', initData=data, db=test_db)

data = {
        "displayName":"large egg",
        "measurement":"each", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":30, 
        "category":"dairy", 
        "subcategory":"egg", 
        "kosher":"pareve",
        "tags": "baking, breakfast, protein",
        "conversions": {
            "g": 1/57,
            "ml": 1/44,      
        }
    }
Ingredient('lg egg', initData=data, db=test_db)
######################
# Create the pantry table
test_db.create_table("pantry",'''
    ingredient TEXT,
    size TEXT,
    qty REAL,
    PRIMARY KEY (ingredient, size)
    ''')

from modules.pantry import Pantry
pantry = Pantry(db=test_db)
pantry.addFood(Ingredient("ap flour", qty=12500, db=test_db))
pantry.addFood(Ingredient("salt", qty=10000, db=test_db))
pantry.addFood(Ingredient("water", qty=10000, db=test_db))
pantry.addFood(Ingredient("instant dry yeast", qty=1000, db=test_db))

######################
# Create the recipe table
from modules.recipe import Recipe

test_db.create_table("recipes",'''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    notes TEXT,
    preheat TEXT,
    preheatTemp REAL,
    yields REAL,
    yieldUnit TEXT,
    yieldConversion REAL,
    yieldConversionUnit TEXT,
    servings REAL,
    servingUnit TEXT,
    servingsConversion REAL,
    servingsConversionUnit TEXT,
    category TEXT,
    subcategory TEXT,
    kosher TEXT                    
''')
test_db.create_table("recipe_ingredients",'''
    recipe_id INTEGER,
    ingredient TEXT,
    size TEXT,
    qty REAL,
    isRecipe BOOLEAN,
    PRIMARY KEY (recipe_id, ingredient, size)
''')
test_db.create_table("recipe_steps",'''
    recipe_id INTEGER,
    step INTEGER,
    description TEXT,
    PRIMARY KEY (recipe_id, step)
''')
test_db.create_table("recipe_tags",'''
    recipe_id INTEGER,
    tag TEXT,
    PRIMARY KEY (recipe_id, tag)
''')



# Insert the basic recipes. 
# Basic recipies use only ingredients and not other recipes
data = {
        "preheat": "preheat oven",
        "preheatTemp": 425,
        "yields":1,
        "yieldUnit":"loaf",
        "yieldConversions": 
            {"loaf": 1, 
             "slice": 14
             },
        "servings":14,
        "servingUnit":"slice",
        "category":"bread",
        "subcategory":"lean white",
        "kosher": "pareve",
        "notes":"This is a basic white bread recipe",
        "tags": ["bread", "white bread", "lean bread", "french bread"],
        "ingredients": [Ingredient("ap flour", 454), Ingredient("salt", 10), Ingredient("water", 320), Ingredient("instant dry yeast", 4)],
        "steps": [
            "If you are conserned about your yeast or need to speed up the process, proof the yeast in the water with a pinch of sugar. Skip otherwise", 
            "Combine the dry ingredients in a large bowl or bowl mixer bowl", 
            "Add 3/4 of the water and mix until a shaggy dough forms. If the dough is too dry, add more water. If the dough is too wet, add more flour", 
            "Knead the dough until it is smooth and elastic. This can take 10-15 minutes by hand or 5-7 minutes in a mixer",
            "Place the dough in a greased bowl and cover with a towel. Let rise until doubled in size, about 1 - 1.5 hours",
            "Punch down the dough and shape into a loaf. Place in a greased loaf pan and let rise until doubled in size, about 1 hour",
            "Bake at 425 for 25-30 minutes or until the internal temperature reaches 190F or nice golden crust has formed and sounds hollow when you knock the bottom.",
            "Let cool for at least 30 minutes before slicing"
        ]
    }


Recipe("peasant bread", initData=data, db=test_db)

######################
# Create the market table
test_db.create_table("markets",'''
    name TEXT,
    location TEXT,
    distance REAL,
    priority INTEGER,
    notes TEXT,
    PRIMARY KEY (name)
    ''')

test_db.create_table("market_ingredients",'''
    market TEXT,
    ingredient TEXT,
    price REAL,
    priceUnit TEXT,
    brand TEXT,
    size REAL,
    PRIMARY KEY (market, ingredient)
    ''')



from modules.market import Market

data = {
        'location': "990 W King Edward Ave, Vancouver",
        'distance': 0.23,
        'notes' : "This is the closest market to my house.",
        'search': "https://voila.ca/search?q=",
        'ingredients' : {
            "ap flour": {'price': 10.00, 'priceUnit': 'kg', 'brand': 'Compliments', 'size': 1 },
            "instant dry yeast": {'price': 1.00, 'priceUnit': 'g', 'brand': 'Fleischmanns', 'size': 100 },
            "salt": {'price': 10, 'priceUnit': 'kg', 'brand': 'Rogers', 'size': 1 },
        }
    }

Market('test shop', initData=data, db=test_db)


######################
# Creating the cooking log table
test_db.create_table("cooking_log",'''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER,
    date TEXT,
    scale REAL
    ''')
