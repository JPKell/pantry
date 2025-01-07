from constants import *

dryGoods = {
      "sesame seeds" : {
        "displayName":"sesame seeds",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"seed", 
        "subcategory":"sesame", 
        "kosher":"pareve",
        "tags": "cooking, salad, dressing",
        "conversions": {
            "cup": 134.4,      
        }
    },
        "peanut butter" : {
        "displayName":"peanut butter",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"nut", 
        "subcategory":"peanut", 
        "kosher":"pareve",
        "tags": "spread, sandwich, snack",
        "conversions": {
            "cup": 256,      
        }
    },
        "white rice" : {
        "displayName":"white rice",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"rice", 
        "kosher":"pareve",
        "tags": "side, main, asian, grain, jasmine",
        "conversions": {
            "cup": 200,      
        }
    },
    "popcorn kernels" : {
        "displayName":"popcorn kernels",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"popcorn", 
        "kosher":"pareve",
        "tags": "snack, side, grain",
        "conversions": {
            "cup": 200,      
        }
    },
        "panko" : {
        "displayName":"panko bread crumbs",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"bread", 
        "kosher":"pareve",
        "tags": "breading, coating, frying",
        "conversions": {
            "cup": 60,      
        }
    },
    
    "dates" : {
        "displayName":"dates",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"fruit", 
        "subcategory":"dried", 
        "kosher":"pareve",
        "tags": "snack, sweet, baking",
        "conversions": {
            "cup": 80,      
        }
    },
    
    "corn grits" : {
        "displayName":"corn grits",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"refrigerator", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"corn", 
        "kosher":"pareve",
        "tags": "side, main, grain",
        "conversions": {
            "cup": 160,      
        }
    },
    "rolled oats" : {
        "displayName":"rolled oats",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"refrigerator", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"oats", 
        "kosher":"pareve",
        "tags": "breakfast, snack, baking",
        "conversions": {
            "cup": 80,      
        }
    },
    
    "walnut pieces" : {
        "displayName":"walnut pieces",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"room temperature", 
        "shelfLife":365, 
        "category":"nut", 
        "subcategory":"walnut", 
        "kosher":"pareve",
        "tags": "snack, baking, salad",
        "conversions": {
            "cup": 112,      
        }
    },
    "dry spaghetti" : {
        "displayName":"dry spaghetti",
        "measurement":"g", 
        "rawStorage":"room temperature", 
        "processedStorage":"refrigerator", 
        "shelfLife":365, 
        "category":"grain", 
        "subcategory":"pasta", 
        "kosher":"pareve",
        "tags": "main, side, italian",
        "conversions": {
            "cup": 91,      
        }
    },
    "pumpkin seeds": {
        "displayName":"pumpkin seeds",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"seed",
        "subcategory":"pumpkin",
        "kosher":"pareve",
        "tags": "snack, salad, baking",
        "conversions": {
            "cup": 124,
        }
    },
    "raw almonds": {
        "displayName":"raw almonds",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"nut",
        "subcategory":"almond",
        "kosher":"pareve",
        "tags": "snack, salad, baking",
        "conversions": {
            "cup": 160,
        }
    },
    "arborio rice": {
        "displayName":"arborio rice",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"grain",
        "subcategory":"rice",
        "kosher":"pareve",
        "tags": "main, side, italian",
        "conversions": {
            "cup": 200,
        }
    },
    "sunflower seeds": {
        "displayName":"sunflower seeds",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"seed",
        "subcategory":"sunflower",
        "kosher":"pareve",
        "tags": "snack, salad, baking",
        "conversions": {
            "cup": 120,
        }
    },
    "dry pinto beans": {
        "displayName":"pinto beans",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"bean",
        "kosher":"pareve",
        "tags": "main, side, mexican",
        "conversions": {
            "cup": 140,
        }
    },
    "dry kidney beans": {
        "displayName":"kidney beans",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"bean",
        "kosher":"pareve",
        "tags": "main, side, chili",
        "conversions": {
            "cup": 140,
        }
    },
    "dry shitake mushrooms": {
        "displayName":"shitake mushrooms",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"fungus",
        "subcategory":"mushroom",
        "kosher":"pareve",
        "tags": "main, side, asian",
        "conversions": {
            "cup": 28,
        }
    },
    "dry red lentils": {
        "displayName":"red lentils",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"lentil",
        "kosher":"pareve",
        "tags": "main, side, indian",
        "conversions": {
            "cup": 200,
        }
    },
    "dry green lentils": {
        "displayName":"green lentils",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"lentil",
        "kosher":"pareve",
        "tags": "main, side, french",
        "conversions": {
            "cup": 200,
        }
    },
    "dry bean soup mix": {
        "displayName":"dry bean soup mix",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"soup",
        "kosher":"pareve",
        "tags": "main, side, soup",
        "conversions": {
            "cup": 200,
        }
    },
    "dry black eyed beans": {
        "displayName":"dry black eyed beans",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"bean",
        "kosher":"pareve",
        "tags": "main, side, soup",
        "conversions": {
            "cup": 200,
        }
    },
    "dry black beans": {
        "displayName":"dry black beans",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"bean",
        "kosher":"pareve",
        "tags": "main, side, soup",
        "conversions": {
            "cup": 150,
        }
    },
        "dried cherries": {
        "displayName":"dried cherries",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"fruit",
        "subcategory":"cherry",
        "kosher":"pareve",
        "tags": "snack, salad, baking",
        "conversions": {
            "cup": 140,
        }
    },
    

    "instant noodles": {
        "displayName":"instant noodles",
        "measurement":"each",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"grain",
        "subcategory":"noodle",
        "kosher":"pareve",
        "tags": "main, side, snack",
        "conversions": {
            "g": 120,
        }
    },
    "tortilla chips": {
        "displayName":"tortilla chip",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"grain",
        "subcategory":"chip",
        "kosher":"pareve",
        "tags": "snack, side, dip",
        "conversions": {
            "cup": 26,
        }
    },
    "matzo meal": {
        "displayName":"matzo meal",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"room temperature",
        "shelfLife":365,
        "category":"grain",
        "subcategory":"meal",
        "kosher":"pareve",
        "tags": "baking, coating, frying",
        "conversions": {
            "cup": 127,
        }
    },
    "dried chickpeas": {
        "displayName":"dried chickpeas",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"chickpea",
        "kosher":"pareve",
        "tags": "main, side, salad",
        "conversions": {
            "cup": 190,
        }
    },
    "dried fava beans": {
        "displayName":"dried fava beans",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"fava",
        "kosher":"pareve",
        "tags": "main, side, salad",
        "conversions": {
            "cup": 220,
        }
    },
    "dried navy beans": {
        "displayName":"dried navy beans",
        "measurement":"g",
        "rawStorage":"room temperature",
        "processedStorage":"refrigerator",
        "shelfLife":365,
        "category":"legume",
        "subcategory":"bean",
        "kosher":"pareve",
        "tags": "main, side, salad",
        "conversions": {
            "cup": 190,
        }
    },
 }