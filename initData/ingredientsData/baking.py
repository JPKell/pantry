from constants import *

baking = {
        "ap flour": {
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
        "knownConversions": {
            "cup": 120,       
        }
    },
        "instant dry yeast": {
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
        "knownConversions": {
            "cup": 148.8,       
        }
    }, 
        "sugar": {
        "displayName":"sugar",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"sweetener", 
        "subcategory":"sugar", 
        "kosher":"pareve",
        "notes":"granulated sugar, keep dry",
        "tags": "baking, sweet, dessert",
        "knownConversions": {
            "cup": 200,       
        }
    },
        "honey": {
        "displayName":"honey",
        "measurement":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"sweetener", 
        "subcategory":"honey", 
        "kosher":"pareve",
        "tags": "sweet, baking, dessert",
        "knownConversions": {
            "g": 1 / (340/CUP), # 1 cup = 340g  
        }
    },
    
    "cocoa powder" : {
        "displayName":"cocoa powder",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"cocoa", 
        "kosher":"pareve",
        "tags": "baking, dessert, sweet",
        "knownConversions": {
            "tbsp": 5,      
        }
    },
    "rye flour" : {
        "displayName":"rye flour",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"flour", 
        "kosher":"pareve",
        "tags": "baking, bread, dense",
        "knownConversions": {
            "cup": 120,      
        }
    },
    "vital wheat gluten" : {
        "displayName":"vital wheat gluten",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"gluten", 
        "kosher":"pareve",
        "tags": "baking, bread, dense",
        "knownConversions": {
            "cup": 120,      
        }
    },
    
    "baking soda" : {
        "displayName":"baking soda",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"spice", 
        "subcategory":"soda", 
        "kosher":"pareve",
        "tags": "baking, cleaning",
        "knownConversions": {
            "cup": 176,      
        }
    },
    "baking powder" : {
        "displayName":"baking powder",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"spice", 
        "subcategory":"powder", 
        "kosher":"pareve",
        "tags": "baking, leavening",
        "knownConversions": {
            "cup": 192,      
        }
    },
    "vanilla extract" : {
        "displayName":"vanilla extract",
        "measurement":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"liquid", 
        "subcategory":"extract", 
        "kosher":"pareve",
        "tags": "baking, sweet, dessert",
        "knownConversions": {
            "g": 208/CUP,      
        }
    },
    "golden corn syrup" : {
        "displayName":"corn syrup",
        "measurement":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"sweetener", 
        "subcategory":"syrup", 
        "kosher":"pareve",
        "tags": "sweet, baking, dessert",
        "knownConversions": {
            "g": 328/CUP,      
        }
    },
    "brown sugar" : {
        "displayName":"brown sugar",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"sweetener", 
        "subcategory":"sugar", 
        "kosher":"pareve",
        "tags": "baking, sweet, dessert",
        "knownConversions": {
            "cup": 200,      
        }
    },
        "cornmeal": {
        "displayName":"cornmeal",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"grain",
        "subcategory":"corn",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 164,
        }
    },
    
    "chickpea flour": {
        "displayName":"chickpea flour",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"grain",
        "subcategory":"flour",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 92,
        }
    },
        "molasses": {
        "displayName":"molasses",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"sweetener",
        "subcategory":"syrup",
        "kosher":"pareve",
        "tags": "sweet, baking, dessert",
        "knownConversions": {
            "g": 328/CUP,
        }
    },
        "salted butter" : {
        "displayName":"salted butter",
        "measurement":"g",
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