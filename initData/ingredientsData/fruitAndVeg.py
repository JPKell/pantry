from constants import *

fruitAndVeg = {
      "mandarin orange" : { 
        "displayName":"mandarin orange",
        "measurement":"each", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"fruit", 
        "subcategory":"citrus", 
        "kosher":"pareve",
        "tags": "snack, fruit, salad",
        "knownConversions": {
            "g": 1/82,  
        }
    },
    
    "avocado": {
        "displayName":"avocado",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"avocado",
        "kosher":"pareve",
        "tags": "snack, salad, sandwich",
        "knownConversions": {
            "g": 1/153,
        }
    },
    "onion": {
        "displayName":"onion",
        "measurement":"g",
        "size": "medium",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"onion",
        "kosher":"pareve",
        "tags": "main, side, aromatic",
        "knownConversions": {
            "each": 170,
            "cup": 160,
        }
    },
    
    "carrot" : {
        "displayName":"carrot",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"root",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 128,
            "each": 61,
        }
    },
    "celery" : {
        "displayName":"celery",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"stalk",
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
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"leaf",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 94,
        }
    },
    
    "garlic" : {
        "displayName":"garlic",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"bulb",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/55,
            "clove": 55/6, # 1 clove = 10g and average garlic bulb is 55g
        }
    },
    "leek" : {
        "displayName":"leek",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"stalk",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/150,
            'cup': 150 / 89, # 1 cup = 89g and average leek is 150g
        }
    },
    "bell pepper" : {
        "displayName":"bell pepper",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"pepper",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/186,
        }
    },
    "jalapeno" : {
        "displayName":"jalapeno",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
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
        "measurement":"g",
        "rawStorage":"freezer",
        "processedStorage":"freezer",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"scraps",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 140,
        }
    },
    "plum tomato" : {
        "displayName":"plum tomato",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"tomato",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/123,
        }
    },
    
    "basil" : {
        "displayName":"basil",
        "measurement":"g",
        "rawStorage":"refrigerator",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"herb",
        "subcategory":"leaf",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 20,
        }
    },
    "lemon" : {
        "displayName":"lemon",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruit",
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
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"cucumber",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/200,
            "cup": 200/133, # 1 cup = 133g and average cucumber is 200g
        }
    },
    "mango" : {
        "displayName":"mango",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"tropical",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/174,
        }
    },
    "lime" : {
        "displayName":"lime",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruit",
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
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"root",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 96,
        }
    },
    "lime" : {
        "displayName":"lime",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruit",
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
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"potato",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/454,
        }
    },
    "green onion" : {
        "displayName":"green onion",
        "measurement":"each",
        "rawStorage":"refrigerator",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"vegetable",
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
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruit",
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
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
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
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"herb",
        "subcategory":"leaf",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 8,
        }
    },
    "corn": {
        "displayName":"corn",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"corn",
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
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"apple",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/182,
            "cup": 182/105, # 1 cup = 105g and average granny smith apple is 182g
        }
    },
    "red onion" : {
        "displayName":"red onion",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
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
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
        "subcategory":"eggplant",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/200,
            "cup": 200/82, # 1 cup = 82g and average eggplant is 200g
        }
    },
    "cayenne" : {
        "displayName":"cayenne",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"vegetable",
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