from modules.database import Db

def initDb(db:Db):
    db.create_table("cooking_log",'''
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER,
        date      TEXT,
        scale     REAL
        ''')
    
    db.create_table("conversions",'''
        name        TEXT,
        fromMeasure TEXT,
        isServings  BOOLEAN,
        factor      REAL,
        PRIMARY KEY (name, fromMeasure, isServings)
        ''')   
    
    db.create_table("measures",'''
        abbreviation TEXT Primary KEY,
        name         TEXT,
        system       TEXT,  -- imperial or metric
        type         TEXT   -- volume or mass
        ''')
    
    db.create_table("ingredients",'''
        name             TEXT,
        displayName      TEXT,
        unit             TEXT,
        rawStorage       TEXT,
        processedStorage TEXT,
        shelfLife        INTEGER,
        notes            TEXT,
        tags             TEXT,
        category         TEXT,
        subcategory      TEXT,
        kosher           TEXT,
        PRIMARY KEY (name),
        FOREIGN KEY(unit) REFERENCES measures(abbreviation)
        ''')
    
    db.create_table("ingredient_alternatives",'''
        ingredient  TEXT,
        alternative TEXT,
        PRIMARY KEY (ingredient, alternative)
        ''')
    
    db.create_table("markets",'''
        name     TEXT,
        location TEXT,
        distance REAL,
        priority INTEGER,
        notes    TEXT,
        search   TEXT,
        PRIMARY KEY (name)
        ''')

    db.create_table("market_ingredients",'''
        market     TEXT,
        ingredient TEXT,
        price      REAL,
        priceUnit  TEXT,
        brand      TEXT,
        size       REAL,
        PRIMARY KEY (market, ingredient)
        ''')

    db.create_table("pantry",'''
        ingredient TEXT PRIMARY Key,
        qty        REAL
        ''')
    db.create_table("recipes",'''
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name         TEXT,
        preheat      TEXT,
        preheatTemp  REAL,
        preheatUnit  TEXT,
        prepareAhead TEXT,
        servings     REAL,
        servingUnit  TEXT,
        yields       REAL,
        yieldUnit    TEXT,
    
        category     TEXT,
        kosher       TEXT,                    
        notes        TEXT,
        subcategory  TEXT
    ''')

    db.create_table("recipe_times",'''
        recipe_id INTEGER,
        time      TEXT,
        step      TEXT,
        sort      INTEGER,
        PRIMARY KEY (recipe_id, sort)                             
        ''')

    db.create_table("recipe_ingredients",'''
        recipe_id   INTEGER,
        ingredient  TEXT,
        qty         REAL,
        prep        TEXT, 
        isRecipe    BOOLEAN,
        PRIMARY KEY (recipe_id, ingredient)
    ''')
    db.create_table("recipe_steps",'''
        recipe_id   INTEGER,
        step        INTEGER,
        description TEXT,
        PRIMARY KEY (recipe_id, step)
    ''')
    db.create_table("recipe_tags",'''
        recipe_id INTEGER,
        tag       TEXT,
        PRIMARY KEY (recipe_id, tag)
    ''')

    ## From here on out these are changes to the database required to support new features

    db.execute("ALTER TABLE recipe_ingredients ADD COLUMN recipePart TEXT")

    db.create_table("recipe_ingredients_bu",'''
            recipe_id   INTEGER,
            ingredient  TEXT,
            qty         REAL,
            prep        TEXT, 
            isRecipe    BOOLEAN,
            recipePart  TEXT,
            PRIMARY KEY (recipe_id, ingredient, recipePart)
        ''')

    db.execute("INSERT INTO recipe_ingredients_bu SELECT * FROM recipe_ingredients")
    db.execute("DROP TABLE recipe_ingredients")
    db.execute("ALTER TABLE recipe_ingredients_bu RENAME TO recipe_ingredients")

