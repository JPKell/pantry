from constants import *

dairy = {
        "lg egg": {
        "displayName":"large egg",
        "unit":"each", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":30, 
        "category":"dairy", 
        "subcategory":"egg", 
        "kosher":"pareve",
        "tags": "baking, breakfast, protein",
        "knownConversions": {
            "g": 1/57,
            "ml": 1/44,      
        }
    },
    "cheddar cheese": {
        "displayName":"cheddar cheese",
        "unit":"g", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":7, 
        "category":"dairy", 
        "subcategory":"cheese", 
        "kosher":"dairy",
        "tags": "snack, sandwich, salad",
        "knownConversions": {
            "cup": 113,
        }
    },  
    "plain yogurt": {
        "displayName":"plain yogurt",
        "unit":"g", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":7, 
        "category":"dairy", 
        "subcategory":"yogurt", 
        "kosher":"dairy",
        "tags": "breakfast, snack, dessert",
        "knownConversions": {
            "cup": 225,
        }
    },
    "butter": {
        "displayName":"butter",
        "unit":"g", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":90, 
        "category":"dairy", 
        "subcategory":"butter", 
        "kosher":"dairy",
        "tags": "baking, cooking, spread",
        "knownConversions": {
            "cup": 227,
        }
    },
    "salted butter" : {
        "displayName":"salted butter",
        "unit":"g",
        "rawStorage":"refrigerator",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"dairy",
        "subcategory":"butter",
        "kosher":"pareve",
        "tags": "spread, cooking, baking",
        "knownConversions": {
            "cup": 227,
        }
    },


}