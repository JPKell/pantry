from constants import *

baking = {
        "ap flour": {
        "displayName":"all-purpose flour",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature",
        "shelfLife":365, 
        "category":"baking", 
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
        "unit":"g", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":133, 
        "category":"baking", 
        "subcategory":"yeast", 
        "kosher":"pareve",
        "notes":"quick-rise, keep dry and refrigerated",
        "tags": "bread, baking",
        "knownConversions": {
            "cup": 148.8,       
        },
        "alternatives": ["active dry yeast", "quick-rise yeast", "fresh yeast"]
    },
    "active dry yeast": {
        "displayName":"active dry yeast",
        "unit":"g", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":133, 
        "category":"baking", 
        "subcategory":"yeast", 
        "kosher":"pareve",
        "notes":"keep dry and refrigerated",
        "tags": "bread, baking",
        "knownConversions": {
            "cup": 148.8,       
        },
        "alternatives": ["instant dry yeast", "quick-rise yeast", "fresh yeast"]
    },
    "quick-rise yeast": {
        "displayName":"quick-rise yeast",
        "unit":"g", 
        "rawStorage":"refrigerator", 
        "processedStorage":"refrigerator", 
        "shelfLife":133, 
        "category":"baking", 
        "subcategory":"yeast", 
        "kosher":"pareve",
        "notes":"keep dry and refrigerated",
        "tags": "bread, baking",
        "knownConversions": {
            "cup": 148.8,       
        },
        "alternatives": ["instant dry yeast", "active dry yeast", "fresh yeast"]
    }, 
    "fresh yeast": {
        "displayName":"fresh yeast",
        "unit":"g",
        "rawStorage":"refrigerator",
        "processedStorage":"refrigerator",
        "shelfLife":14,
        "category":"baking",
        "subcategory":"yeast",
        "kosher":"pareve",
        "notes":"keep dry and refrigerated, use twice as much by weight as dry yeast",
        "tags": "bread, baking",
        "alternatives": ["instant dry yeast", "active dry yeast", "quick-rise yeast"]
    },
    "sugar": {
        "displayName":"sugar",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":999, 
        "category":"baking", 
        "subcategory":"sweetener", 
        "kosher":"pareve",
        "notes":"granulated sugar, keep dry",
        "tags": "baking, sweet, dessert",
        "knownConversions": {
            "cup": 200,       
        }
    },
    "honey": {
        "displayName":"honey",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":999, 
        "category":"baking", 
        "subcategory":"sweetener", 
        "kosher":"pareve",
        "tags": "sweet, baking, dessert",
        "knownConversions": {
            "g": 340/CUP,
        }
    },
    
    "cocoa powder" : {
        "displayName":"cocoa powder",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"misc", 
        "kosher":"pareve",
        "tags": "baking, dessert, sweet",
        "knownConversions": {
            "tbsp": 5,      
        }
    },
    "rye flour" : {
        "displayName":"rye flour",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"flour", 
        "kosher":"pareve",
        "tags": "baking, bread, dense",
        "knownConversions": {
            "cup": 120,      
        }
    },
    "vital wheat gluten" : {
        "displayName":"vital wheat gluten",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"gluten", 
        "kosher":"pareve",
        "tags": "baking, bread, dense",
        "knownConversions": {
            "cup": 120,      
        }
    },
    
    "baking soda" : {
        "displayName":"baking soda",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"misc", 
        "kosher":"pareve",
        "tags": "baking, cleaning",
        "knownConversions": {
            "cup": 176,      
        }
    },
    "baking powder" : {
        "displayName":"baking powder",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"misc", 
        "kosher":"pareve",
        "tags": "baking, leavening",
        "knownConversions": {
            "cup": 192,      
        }
    },
    "vanilla extract" : {
        "displayName":"vanilla extract",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"liquid", 
        "kosher":"pareve",
        "tags": "baking, sweet, dessert",
        "knownConversions": {
            "g": 208/CUP,      
        }
    },
    "golden corn syrup" : {
        "displayName":"corn syrup",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"sweetener", 
        "kosher":"pareve",
        "tags": "sweet, baking, dessert",
        "knownConversions": {
            "g": 328/CUP,      
        }
    },
    "brown sugar" : {
        "displayName":"brown sugar",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"baking", 
        "subcategory":"sweetener", 
        "kosher":"pareve",
        "tags": "baking, sweet, dessert",
        "knownConversions": {
            "cup": 200,      
        }
    },
    "cornmeal": {
        "displayName":"cornmeal",
        "unit":"g",
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
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"legumes",
        "subcategory":"flour",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "cup": 92,
        }
    },
    "molasses": {
        "displayName":"molasses",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"baking",
        "subcategory":"sweetener",
        "kosher":"pareve",
        "tags": "sweet, baking, dessert",
        "knownConversions": {
            "g": 328/CUP,
        }
    },

}