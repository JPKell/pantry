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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
            "g": 1/55,
            "clove": 6 * (1/55)
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
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
        "conversions": {
            "g": 1/15,
            "cup": 15/100, # 1 cup = 100g and average green onion is 15g
            "bunch": 7,
        }
    },


    
 }