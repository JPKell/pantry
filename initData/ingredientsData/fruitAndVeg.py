from constants import *

fruitAndVeg = {
      "mandarin orange" : { 
        "displayName":"mandarin orange",
        "unit":"each", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"fruits and vegetables", 
        "subcategory":"citrus", 
        "kosher":"pareve",
        "tags": "snack, fruit, salad",
        "knownConversions": {
            "g": 1/82,  
        }
    },
    
    "avocado": {
        "displayName":"avocado",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"vegetables",
        "kosher":"pareve",
        "tags": "snack, salad, sandwich",
        "knownConversions": {
            "g": 1/153,
        }
    },
    "onion": {
        "displayName":"onion",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"vegetables",
        "kosher":"pareve",
        "notes": "medium",
        "tags": "main, side, aromatic",
        "knownConversions": {
            "each": 170,
            "cup": 160,
        }
    },
    
    "carrot" : {
        "displayName":"carrot",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"root vegetables",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 128,
            "each": 61,
        }
    },
    "celery" : {
        "displayName":"celery",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"vegetables",
        "kosher":"pareve",
        "notes": "Each here refers to a single stalk not a bunch",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 127,
            "each": 50,
        }
    },
    "cabbage" : {
        "displayName":"cabbage",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"leafy greens",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 94,
        }
    },
    
    "garlic" : {
        "displayName":"garlic",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"herbs and spices",
        "subcategory":"fresh herbs",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/55,
            "clove": 1/(55/6), # 1 clove = 10g and average garlic bulb is 55g
        }
    },
    "leek" : {
        "displayName":"leek",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"onion",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/150,
            'cup': 150 / 89, # 1 cup = 89g and average leek is 150g
        }
    },
    "bell pepper" : {
        "displayName":"bell pepper",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"pepper",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/186,
        }
    },
    "jalapeno" : {
        "displayName":"jalapeno",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"pepper",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/20,
            "cup": 20/90, # 1 cup = 90g and average jalapeno is 20g
        }
    },  
    "stock scraps" : {
        "displayName":"stock scraps",
        "unit":"g",
        "rawStorage":"freezer",
        "processedStorage":"freezer",
        "shelfLife":365,
        "category":"home",
        "subcategory":"scraps",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 140,
        }
    },
    "plum tomato" : {
        "displayName":"plum tomato",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"tomato",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/123,
        }
    },
    
    "basil" : {
        "displayName":"basil",
        "unit":"g",
        "rawStorage":"refrigerator",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"herbs and spices",
        "subcategory":"fresh herbs",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 20,
        }
    },
    "lemon" : {
        "displayName":"lemon",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"citrus",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/85,
            "ml": 1/30,
        }
    },
    "cucumber" : {
        "displayName":"cucumber",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"vegetables",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/200,
            "cup": 200/133, # 1 cup = 133g and average cucumber is 200g
        }
    },
    "mango" : {
        "displayName":"mango",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"tropical",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/174,
        }
    },
    "lime" : {
        "displayName":"lime",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"citrus",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/48,
            "ml": 1/30,
        }
    },
    "ginger" : {
        "displayName":"ginger",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"herbs and spices",
        "subcategory":"fresh herbs",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 96,
        }
    },
    "lime" : {
        "displayName":"lime",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"citrus",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/60,
            "ml": 1/30,
        }
    },
    "russet potato" : {
        "displayName":"russet potato",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"root vegetables",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/454,
        }
    },
    "green onion" : {
        "displayName":"green onion",
        "unit":"each",
        "rawStorage":"refrigerator",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"onion",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/15,
            "cup": 15/100, # 1 cup = 100g and average green onion is 15g
            "bunch": 7,
        }
    },
    "tomato": {
        "displayName":"tomato",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"tomato",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/123,
            "cup": 123/180, # 1 cup = 180g and average tomato is 123g
        }
    },
    "shallot": {
        "displayName":"shallot",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"onion",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/24,
            "cup": 20/160, # 1 cup = 100g and average shallot is 20g
        }
    },
    "oregano": {
        "displayName":"oregano",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"herbs and spices",
        "subcategory":"fresh herbs",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 51,
        }
    },
    "corn": {
        "displayName":"corn",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"vegetables",
        "kosher":"pareve",
        "notes": "Corn on the cob, when measured or weighed is kernels only",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 3/4,
            "g": 1 / 155 * (3/4), # 1 cup = 155g and average corn cob is 3/4 cup

        }
    },
    "granny smith apple"    : {
        "displayName":"granny smith apple",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"fruit",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/182,
            "cup": 182/105, # 1 cup = 105g and average granny smith apple is 182g
        }
    },
    "red onion" : {
        "displayName":"red onion",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"onion",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/120,
            "cup": 120/160, # 1 cup = 160g and average red onion is 120g
        }
    },
    "eggplant" : {
        "displayName":"eggplant",
        "unit":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"vegetables",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/200,
            "cup": 200/82, # 1 cup = 82g and average eggplant is 200g
        }
    },
    "cayenne" : {
        "displayName":"cayenne",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"pepper",
        "kosher":"pareve",
        "note": "fresh",
        "tags": "main, side, snack, fresh",
        "knownConversions": {
            "cup": 105,
            "each": 4,
        }
    },
    
 }