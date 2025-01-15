from constants import *

cannedGoods = {
      "mango puree" : {
        "displayName":"mango puree",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"refrigerator", 
        "shelfLife":365, 
        "category":"fruit", 
        "subcategory":"puree", 
        "kosher":"pareve",
        "tags": "sweet, baking, dessert",
        "knownConversions": {
            "cup": 200,      
        }
    },
    "canned chickpeas": {
        "displayName":"canned chickpeas",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"canned",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 200,
        }
    },
    
    "canned peas": {
        "displayName":"canned peas",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruits and vegetables",
        "subcategory":"canned",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 250,
        }
    },
    "canned pineapple": {
        "displayName":"canned pinapple",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"tropical",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 236,
        }
    },
    
    "canned crushed tomatoes": {
        "displayName":"canned crushed tomatoes",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"tomato",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 236,
        }
    },
    "canned plum tomato": {
        "displayName":"canned plum tomato",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"tomato",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1 / (246 / CUP), # 1 cup = 246 g 
        }
    },
    "coconut milk": {
        "displayName":"coconut milk",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"nuts and seeds",
        "subcategory":"coconut",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 244/CUP, # 1 cup = 244 g
        }
    },
    "sun-dried tomato": {
        "displayName":"sun-dried tomato",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"tomato",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 54, 
        }
    },
 }