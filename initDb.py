from modules.database import Db

def initDb(db:Db):
    db.create_table("measures",'''
        name TEXT PRIMARY KEY,
        abbreviation TEXT,
        system TEXT,        -- imperial or metric
        type TEXT           -- volume or mass
        ''')
    
    db.create_table("conversions",'''
        name TEXT,
        fromMeasure TEXT,
        isServings BOOLEAN,
        factor REAL,
        PRIMARY KEY (name, fromMeasure, isServings)
        ''')   
    
    db.create_table("ingredients",'''
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
    
    db.create_table("ingredient_alternatives",'''
        ingredient TEXT,
        alternative TEXT,
        PRIMARY KEY (ingredient, alternative)
        ''')
    
    db.create_table("pantry",'''
        ingredient TEXT,
        size TEXT,
        qty REAL,
        PRIMARY KEY (ingredient, size)
        ''')
    db.create_table("recipes",'''
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        notes TEXT,
        preheat TEXT,
        preheatTemp REAL,
        yields REAL,
        yieldUnit TEXT,
        servings REAL,
        servingUnit TEXT,
        category TEXT,
        subcategory TEXT,
        kosher TEXT                    
    ''')
    db.create_table("recipe_ingredients",'''
        recipe_id INTEGER,
        ingredient TEXT,
        size TEXT,
        qty REAL,
        prep TEXT, 
        isRecipe BOOLEAN,
        PRIMARY KEY (recipe_id, ingredient, size)
    ''')
    db.create_table("recipe_steps",'''
        recipe_id INTEGER,
        step INTEGER,
        description TEXT,
        PRIMARY KEY (recipe_id, step)
    ''')
    db.create_table("recipe_tags",'''
        recipe_id INTEGER,
        tag TEXT,
        PRIMARY KEY (recipe_id, tag)
    ''')

    db.create_table("markets",'''
        name TEXT,
        location TEXT,
        distance REAL,
        priority INTEGER,
        notes TEXT,
        PRIMARY KEY (name)
        ''')

    db.create_table("market_ingredients",'''
        market TEXT,
        ingredient TEXT,
        price REAL,
        priceUnit TEXT,
        brand TEXT,
        size REAL,
        PRIMARY KEY (market, ingredient)
        ''')

    db.create_table("cooking_log",'''
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER,
        date TEXT,
        scale REAL
        ''')