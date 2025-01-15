from constants import *

wetGoods = {
    "water": {
        "displayName":"water",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"home", 
        "subcategory":"water", 
        "kosher":"pareve",
        "tags": "beverage",
        "knownConversions": {
            "g": 1,       
        }
    },
        "olive oil": {
        "displayName":"olive oil",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"liquid", 
        "subcategory":"oil", 
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {    
            "g": 216.65/CUP, # 1 cup = 216.65g      
        }
    },
        "instant coffee": {
        "displayName":"instant coffee",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"beverage", 
        "subcategory":"coffee", 
        "kosher":"pareve",
        "tags": "beverage",
        "knownConversions": {
            "ml": 1.8 / TSP,       
        }
    },
        "whole coffee bean": {
        "displayName":"whole coffee bean",
        "unit":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"beverage", 
        "subcategory":"coffee", 
        "kosher":"pareve",
        "tags": "beverage",
        "knownConversions": {
            "cup": 82,       # 1 cup = 82g therefore 82/453.592 = 0.18
        }
    },
        "balsamic vinegar": {
        "displayName":"balsamic vinegar",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"liquid", 
        "subcategory":"vinegar", 
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": (255/CUP), # 1 cup = 255       
        }
    },
        "apple cider vinegar": {
        "displayName":"apple cider vinegar",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"liquid", 
        "subcategory":"vinegar", 
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": (240/CUP),      
        }
    },
    "sesame oil" : {
        "displayName":"sesame oil",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"liquid", 
        "subcategory":"oil", 
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": (224/CUP),      
        }
    },
    "grapeseed oil" : {
        "displayName":"grape seed oil",
        "unit":"ml", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"liquid", 
        "subcategory":"oil", 
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": (218/CUP),      
        }
    },
    
    "fish sauce": {
        "displayName":"fish sauce",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"sauce",
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": 1.2,
        }
    },
        "tabasco": {
        "displayName":"tabasco",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"sauce",
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "cup": 225.6,
        }
    },
        "mayonnaise": {
        "displayName":"mayonnaise",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"condiment",
        "kosher":"pareve",
        "tags": "spread, sandwich, dip",
        "knownConversions": {
            "cup": 230,
        }
    },
            "yellow mustard" : {
        "displayName":"yellow mustard",
        "unit":"g",
        "rawStorage":"refrigerator",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"condiment",
        "kosher":"pareve",
        "tags": "spread, sandwich, dip",
        "knownConversions": {
            "cup": 250,
        }
    },
        "white wine vinegar" : {
        "displayName":"white wine vinegar",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"vinegar",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/240,
        }
    },
        "red wine vinegar" : {
        "displayName":"red wine vinegar",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"vinegar",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/240,
        }
    },
    "vegetable oil" : {
        "displayName":"vegetable oil",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"oil",
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": (218/CUP),      
        }
    },
    "soy sauce" : {
        "displayName":"soy sauce",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"sauce",
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": 255/CUP,
        }
    },
    "light soy sauce" : {
        "displayName":"light soy sauce",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"sauce",
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "knownConversions": {
            "g": 255/CUP,
        }
    },
    "apple cider": {
        "displayName":"apple cider",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"juice",
        "kosher":"pareve",
        "tags": "beverage",
        "knownConversions": {
            "g": 248/CUP,
        }
    },
    "maple syrup": {
        "displayName":"maple syrup",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"baking",
        "subcategory":"sweetener",
        "kosher":"pareve",
        "tags": "sweetener",
        "knownConversions": {
            "g": 240/CUP,
        }
    },
    "dijon mustard": {
        "displayName":"dijon mustard",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"condiment",
        "kosher":"pareve",
        "tags": "spread, sandwich, dip",
        "knownConversions": {
            "cup": 240,
        }
    },
    "tahini": {
        "displayName":"tahini",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"nuts and seeds",
        "subcategory":"sesame",
        "kosher":"pareve",
        "tags": "spread, sandwich, dip",
        "knownConversions": {
            "cup": 240/CUP,
        }
    },
    "rice vinegar": {
        "displayName":"rice vinegar",
        "unit":"ml",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"vinegar",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "g": 1/240,
        }
    },
    "better than bouillon": {
    
        "displayName":"better than bouillon",
        "unit":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"liquid",
        "subcategory":"stock",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "knownConversions": {
            "tsp": 6,
        }
    },  
}