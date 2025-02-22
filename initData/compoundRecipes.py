from modules.ingredients import Ingredient
from modules.recipe import Recipe
from constants import *

# Create a bread recipe
compoundRecipes = {
    'challah' : {
        "preheat": "preheat oven",
        "preheatTemp": 350,
        "preheatUnit": "F",
        "yields":2,
        "yieldUnit":"loaf",
        "servings":20,
        "servingUnit":"slice",
        "category":"bread",
        "subcategory":"white",
        "notes":"Loaf sizes can vary, this recipe is for 2 small loaves",
        "tags": ["enriched bread", "egg bread", "shabbat"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("ap flour", 4, qtyUnit='cup'), 
            Ingredient("salt", 2, qtyUnit='tsp'), 
            Ingredient("water", 1, qtyUnit='cup'), 
            Ingredient("instant dry yeast", 2, qtyUnit='tsp'), 
            Ingredient("sugar", 0.25, qtyUnit='cup'), 
            Ingredient("lg egg", 2),
            Recipe("egg yolk", yieldQty=1), 
            Ingredient("olive oil", 0.25, qtyUnit='cup'),
            ],
        "steps": [
            "If you are concerned about your yeast or need to speed up the process, proof the yeast in the water with a pinch of sugar. Skip otherwise",
            "Combine the dry ingredients in a large bowl or bowl mixer bowl",
            "Combine the wet ingredients in a separate bowl reserving 1/4 of the water, reserve the egg white for the egg wash",
            "Add the wet ingredients to the dry ingredients and mix until a shaggy dough forms. Add the remaining water if the dough is too dry",
            "Will be a little tackier than a bread dough. Knead the dough until it is smooth and elastic. This can take 10-15 minutes by hand or 5-7 minutes in a mixer. ",
            "Place the dough in a greased bowl and cover with a towel. Let rise until doubled in size, about 1 - 1.5 hours",
            "Make the egg wash by adding a little water to the reserved egg white and beating with a small whisk or fork",
            "After dough has doubled, punch down the dough and divide by 2. Cut each half into 3 even pieces and roll into ropes. Braid the ropes and place in a greased loaf pan. Let rise until doubled in size, about 1 hour",
            "Brush with an egg wash and bake at 350 for 25-30 minutes or until the internal temperature reaches 190F or nice golden crust has formed and sounds hollow when you knock the bottom.",
            "Let cool for at least 30 minutes before slicing"
        ],
        "times": {"active": "10-15 minutes", "proof": "100-180 minutes", "bake": "25-30 minutes"},
    },
    "toast with butter" : {
        "yields":1,
        "yieldUnit":"slice",
        "servings":1,
        "servingUnit":"slice",
        "category":"breakfast",
        "subcategory":"toast",
        "tags": ["bread", "toast", "butter"],
        "kosher": "pareve",
        "ingredients": [
            Recipe("peasant bread", servingQty=1, servingUnit='slice'),
            Ingredient("salted butter", 2, qtyUnit='tsp'),
        ],
        "times": {"active": "1 minutes", "cook": "2-5 minutes"},
        "steps": [
            "Toast the bread",
            "Spread the butter while the toast is warm"
        ],
    },
    "toast with peanut butter" : {
        "yields":1,
        "yieldUnit":"slice",
        "servings":1,
        "servingUnit":"slice",
        "category":"breakfast",
        "subcategory":"toast",
        "tags": ["bread", "toast", "peanut butter"],
        "kosher": "pareve",
        "ingredients": [
            Recipe("peasant bread", servingQty=1, servingUnit='slice'),
            Ingredient("peanut butter", 1, qtyUnit='tbsp'),
        ],
        "times": {"active": "1 minutes", "cook": "2-5 minutes"},
        "steps": [
            "Toast the bread",
            "Spread the peanut butter on the toast"
        ],
    },
    "french toast" : {
        "preheat": 'stove top medium heat',
        "yields":2,
        "yieldUnit":"slice",
        "servings":2,
        "servingUnit":"slice",
        "category":"breakfast",
        "subcategory":"toast",
        "tags": ["bread", "french toast"],
        "kosher": "pareve",
        "ingredients": [
            Recipe("peasant bread", servingQty=2, servingUnit='slice'),
            Ingredient("lg egg", 2),
            Ingredient("water", 1, qtyUnit='tbsp'),
            Ingredient("grapeseed oil", 1, qtyUnit='tsp'),
            Ingredient("salt", 1, qtyUnit='tsp'), 
        ],
        "times": {"active": "10-15 minutes", "cook": "2-5 minutes"},
        "steps": [
            "Heat the oil in a pan over medium heat",
            "Whisk the egg, water, and salt in a bowl",
            "Soak the bread in the egg mixture",
            "Fry the bread until golden brown on both sides",
        ],
    },
    "fine vegetable stock" : {
        "preheat": 'stove top medium heat',
        "yields":3.84,
        "yieldUnit":"l",
        "servings":3840/CUP,
        "servingUnit":"cup",
        "category":"mise en place",
        "subcategory":"stock",
        "tags": ["stock", "vegetables"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("grapeseed oil", 60, qtyUnit='ml'),
            Recipe("mirepoix", servingQty=1.36, servingUnit='kg'), 
            Ingredient("garlic", 3, qtyUnit='each'),
            Ingredient("leek", 400, qtyUnit='g'),
            Ingredient("bell pepper", 400, qtyUnit='g'),
            Ingredient("jalapeno", 3),
            Ingredient("salt", 2, qtyUnit='tsp'),
            Ingredient("water", 4.8, qtyUnit='l'),
        ],
        "steps": [
            "Rough chop the vegetables",
            "Add the vegetables to a pot with the oil and saute until soft",
            "Add the water and salt",
            "Bring to a boil and simmer for 1-2 hours until the stock is flavorful or reduced by half",
            "Strain the stock and discard the vegetables",
        ],
        "times": {"active": "10 minutes", "cook": "1-2 hour"},
    },
    "lentil soup": {
        "preheat": 'stove top medium heat',
        "yields":1.92,
        "yieldUnit":"l",
        "servings":1920/CUP,
        "servingUnit":"cup",
        "category":"soup",
        "subcategory":"creamy",
        "tags": ["soup", "lentil"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("grapeseed oil", 30, qtyUnit='ml'),
            Ingredient("onion", 1, qtyUnit='each', prep="chopped"),
            Recipe("mirepoix", servingQty=227, servingUnit='g'),
            Ingredient("garlic", 4, qtyUnit='each', prep="chopped"),
            Ingredient("dried green lentils", 400, qtyUnit='g'),
            Recipe("vegetable stock", yieldQty=2.85, yieldUnit='l'),
            Recipe("lemon juice", yieldQty=30, yieldUnit='ml'),
            Ingredient("salt", 2, qtyUnit='tsp'),
        ],
        "steps": [
            "Chop the vegetables",
            "Add the vegetables to a pot with the oil and saute until soft",
            "Add the water, lentils, and salt",
            "Bring to a boil and simmer for around 1 hour",
            "Blend the soup",
        ],
        "times": {"active": "10 minutes", "cook": "50-70 minutes"},
    },
    "mango chutney": {
        "yields": 430,
        "yieldUnit":"ml",
        "servings":430/TBSP,
        "servingUnit":"tbsp",
        "category":"sauces",
        "subcategory":"dipping",
        "tags": ["sauces", "chutney", "mango"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("mango", 2, qtyUnit='each'),
            Recipe("lime juice", yieldQty=30, yieldUnit='ml'),
            Ingredient("cilantro", 2, qtyUnit='g'),
            Ingredient("onion", 1, qtyUnit='each'),
            Ingredient("ginger", 30, qtyUnit='g'),
            Ingredient("jalapeno", 4, qtyUnit='each'),
            Ingredient("salt", 1, qtyUnit='tsp'),
        ],
        "steps": [
            "Dice the mango, onion, ginger, and jalapeno",
            "Add all the ingredients and let rest in a refrigerator for up to 2 hour",
            "Adjust seasoning as necessary",
        ],
        "times": {"active": "10 minutes", "rest": "2 hours"},
    },
    "potato latke": {
        "preheat": 'stove top medium heat',
        "yields": 10,
        "yieldUnit":"each",
        "servings":10,
        "servingUnit":"each",
        "category":"vegetables",
        "subcategory":"potato",
        "tags": ["jewish", "pancake", "potato"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("russet potato", 1.36, qtyUnit='kg'),
            Ingredient("onion", 454, qtyUnit='g'),
            Recipe("lemon juice", servingQty=30, servingUnit='ml'),
            Ingredient("lg egg", 2),
            Ingredient("ap flour", 28, qtyUnit='g'),
            Ingredient("matzo meal", 28, qtyUnit='g'),
            Ingredient("grapeseed oil", 120, qtyUnit='ml'),
        ],
        "steps": [
            "Grate the potato and onion and toss in lemon juice to prevent browning",
            "Squeeze out the excess liquid",
            "Transfer to a bowl and add the egg, flour, and matzo meal",
            "Form into patties",
            "Fry the patties in a pan until golden brown on both sides, this will have to be done in batches so you don't crowd the pan",
            "Season with salt and pepper to taste",
        ],
        "times": {"active": "10 minutes", "cook": "10-30 minutes"},
    },
    "boiled white beans" : {
        "preheat": 'stove top medium heat',
        "prepareAhead": "Soak the beans overnight",
        "yields":1,
        "yieldUnit":"each",
        "servings":10,
        "servingUnit":"each",
        "category":"vegetables",
        "subcategory":"bean",
        "tags": ["protein", "bean"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("dried navy beans", 454, qtyUnit='g'),
            Ingredient("vegetable oil", 30, qtyUnit='ml'),
            Ingredient("water", 1, qtyUnit='l'),
            Ingredient("onion", 113, qtyUnit='g', prep="diced"),
            Recipe("vegetable stock", yieldQty=1.92, yieldUnit='l'),
            Recipe("sachet of spices", 1),
        ],
        "steps": [
            "Soak the beans overnight",
            "Heat the oil in a pot over medium heat",
            "Add the onion and sweat until translucent",
            "Add the beans, stock, and sachet of spices",
            "Bring to a boil and simmer for around 1 hour",
            "Season with salt and pepper and simmer until beans are tender",
            "Remove the sachet of spices",
            "Beans can be strained and used immediately or stored in the liquid",
        ],
        "times": {"active": "10 minutes", "cook": "1 hour"},
    },
    "mixed bean salad" : {
        "yields": 10,
        "yieldUnit":"each",
        "servings":10,
        "servingUnit":"each",
        "prepareAhead": "Soak the beans overnight",
        "category":"salad",
        "subcategory":"bean",
        "tags": ["salad", "bean"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("dried black beans", 284, qtyUnit='g', prep="cooked"),
            Ingredient("dried pinto beans", 284, qtyUnit='g', prep="cooked"),
            Ingredient("dried chickpeas", 284, qtyUnit='g', prep="cooked"),
            Ingredient("dried red lentils", 142, qtyUnit='g', prep="cooked"),
            Ingredient("red onion", 170, qtyUnit='g', prep="diced"),
            Ingredient("parsley", 1, qtyUnit='each', prep="minced"),
            Ingredient("celery", 30, qtyUnit='g', prep="minced"),
            Recipe("balsamic vinaigrette", yieldQty=30, yieldUnit='ml'),
            Ingredient("salt", 1, qtyUnit='tsp'),
        ],
        "steps": [
            "Cook the beans and lentils until tender",
            "Drain the beans and lentils and let cool",
            "Dice the onion, parsley, and celery",
            "Mix all the ingredients and let marinade in a refrigerator for at least 24 hours",
            "Adjust seasoning as necessary",
        ],
        "times": {"active": "10 minutes", "rest": "24 hours"},
    },
    "guacamole" : {
        "yields":480,
        "yieldUnit":"ml",
        "servings":480/60, # 2 oz servings
        "servingUnit":"each",
        "category":"sauces",
        "subcategory":"spreads",
        "tags": ["sauces", "guacamole"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("avocado", 3),
            Ingredient("red onion", 64, qtyUnit='g', prep="small dice"),
            Ingredient("jalapeno", 7, qtyUnit='g', prep="seeded and minced"),
            Ingredient("cilantro", 3, qtyUnit='g', prep="chopped"),
            Ingredient("garlic", 1, qtyUnit='clove'),
            Recipe("lime juice", yieldQty=45, yieldUnit='ml'),
            Ingredient("salt", 5, qtyUnit='g'),
            Ingredient("black pepper", 1, qtyUnit='g'),
        ],
        "steps": [
            "Soak the onions in cold water for 20 minutes, drain and rinse, dry well",
            "Peel the avocado and cut roughly into a medium dice",
            "Add the jalapeno, garlic, lime juice, salt, pepper, and cilantro",
            "Mash the ingredients together until desired consistency",
            "Season with salt and pepper",
        ],
        "times": {"active": "10-20 minutes", "rest": "20 minutes"},
    },
    "hummus": {
        "prepareAhead": "Soak the chickpeas overnight",
        "yields": 960,
        "yieldUnit":"ml",
        "servings":960/60, # 2 oz servings
        "servingUnit":"each",
        "category":"sauces",
        "subcategory":"spreads",
        "tags": ["sauces", "hummus"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("dried chickpeas", 340, qtyUnit='g', prep="soaked overnight"),
            Recipe("lemon juice", yieldQty=150, yieldUnit='ml'),
            Ingredient("garlic", 3, qtyUnit='clove', prep="diced"),
            Ingredient("olive oil", 90, qtyUnit='ml'),
            Ingredient("tahini", 128, qtyUnit='g'),
            Ingredient("salt", 5, qtyUnit='g'),
        ],
        "steps": [
            "Boil the chickpeas in water until tender, 1-2 hours. Drain the chickpeas and reserve the cooking liquid",
            "In a food processor blend the chickpeas with 120 ml of the reserved cooking liquid until smooth paste",
            "Add the lemon juice, garlic, oil, tahini, and salt and process until well combined",
            "Adjust seasoning as necessary",
        ],
        "times": {"active": "10-15 minutes", "cook": "1-2 hours"},
    },
    "baba ghanoush": {
        "preheat": 'oven',
        "preheatTemp": 450,
        "yields": 480,
        "yieldUnit":"ml",
        "servings":480/60, # 2 oz servings
        "servingUnit":"each",
        "category":"sauces",
        "subcategory":"spreads",
        "tags": ["sauces", "baba ganoush"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("eggplant", 900, qtyUnit='g', prep="halved"),
            Ingredient("tahini", 85, qtyUnit='g'),
            Ingredient("garlic", 14, qtyUnit='g', prep="rough chop"),
            Recipe("lemon juice", yieldQty=90, yieldUnit='ml'),
            Ingredient("parsley", 43, qtyUnit='g', prep="chopped"),
            Ingredient("salt", 5, qtyUnit='g'),
        ],
        "steps": [
            "Slice the eggplant in half and roast cut side down in the oven at 450 F until skin is charred, around 1 to 1.5 hours",
            "Peel the eggplant and blend with the garlic, oil, tahini, lemon juice, and salt",
            "Blend until homogenous. If too thick, add water to thin",
            "When mixture is smooth, add the parsley and adjust seasoning as necessary",
        ],
    },
    "harissa": {
        "prepareAhead": "Soak the chilis in warm water for 30 minutes",
        "yields": 960,
        "yieldUnit":"ml",
        "servings":960/TBSP, # 2 oz servings
        "servingUnit":"tbsp",
        "category":"sauces",
        "subcategory":"condiment",
        "tags": ["sauces", "harissa"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("dried habanero", 16, qtyUnit='each'),
            Ingredient("cayenne", 1.8, qtyUnit='kg', prep="seeded"),
            Ingredient("sun-dried tomato", 3, qtyUnit='clove'),
            Ingredient("garlic", 43, qtyUnit='g'),
            Ingredient("ground tumeric", 43, qtyUnit='g'),
            Ingredient("cumin", 4, qtyUnit='g', prep="ground"),
            Ingredient("coriander", 4, qtyUnit='g', prep="ground"),
            Ingredient("caraway", 4, qtyUnit='g'),
            Recipe("lemon juice", yieldQty=10, yieldUnit='ml'),
            Ingredient("olive oil", 60, qtyUnit='ml'),
            Ingredient("salt", 5, qtyUnit='g'),
        ],
        "steps": [
            "Hydrate the chilis in warm water for 30 minutes",
            "When they are hydrated, remove the seeds and stems",
            "Toss the habaneros in a hot pan until the skin blackens and a little smoke rises, about 15 seconds per side",
            "Blend the chilis with the garlic, cumin, coriander, caraway, and salt",
            "Adjust the consistency with the lemon juice and olive oil",
            "Adjust seasoning as necessary",
        ],
        "times": {"active": "10 minutes", "rest": "30 minutes"},
    },
    "z'hug":{
        "yields": 480,
        "yieldUnit":"ml",
        "servings":480/TBSP, 
        "servingUnit":"tbsp",
        "category":"sauces",
        "subcategory":"condiment",
        "tags": ["sauces", "z'hug"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("jalapeno", 725, qtyUnit='g'),
            Ingredient("garlic", 25, qtyUnit='g'),
            Ingredient("cilantro", 100, qtyUnit='g'),
            Ingredient("parsley", 50, qtyUnit='g'),
            Ingredient("mint", 50, qtyUnit='g'),
            Ingredient("cumin", 4, qtyUnit='g', prep="toasted"),
            Ingredient("cardamom", 5, qtyUnit='g', prep="peeled, seeds toasted"),
            Ingredient("olive oil", 240, qtyUnit='ml'),
            Recipe("lemon juice", yieldQty=90, yieldUnit='ml'),
            Ingredient("salt", 5, qtyUnit='g'),
            Ingredient("black pepper", 4, qtyUnit='g', prep="ground"),
        ],
        "steps": [
            "Roast the japaleno in a hot pan until the skin blackens and a little smoke rises, about 15 seconds per side",
            "Blend the jalapeno, garlic, cilantro, parsley, mint, cumin, cardamom, salt, and pepper",
            "Slowly add the olive oil while continuing to blend",
            "Season with lemon juice, salt and pepper",
        ],
        "times": {"active": "10-15 minutes"},
    },
    "risotto": {
        "yields":10,
        "yieldUnit":"each",
        "servings":10,
        "servingUnit":"each",
        "category":"grain",
        "subcategory":"rice",
        "tags": ["grain", "rice", "risotto"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("onion", 57, qtyUnit='g', prep="minced"),
            Ingredient("butter", 57, qtyUnit='g'),
            Ingredient("arborio rice", 397, qtyUnit='g'),
            Recipe("vegetable stock", yieldQty=1.44, yieldUnit='l'),
        ],
        "steps": [
            "In a medium pot, add the oil and sweat the onions until translucent, 6-8 minutes",
            "Add the rice and toast until the rice is aromatic, about 1 minute",
            "Add the stock 1/3 at a time, stirring frequently until the stock is absorbed before adding more. Alternative to stirring, shaking the pot causes the rice to rub the starch off the grains and create a creamy texture",
            "Cook until the rice is tender and creamy, about 20 minutes",
            "Add the butter and cheese and stir until melted",
        ],
        "times": {"active": "20-25 minutes", "cook": "20-30 minutes"},
    },
    "rice and beans" : {
        "prepareAhead": "Soak the beans overnight",
        "yields":10,
        "yieldUnit":"each",
        "servings":10,
        "servingUnit":"each",
        "category":"mains",
        "subcategory":"beans",
        "tags": ["grain", "rice", "beans"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("dried kidney beans", 454, qtyUnit='g', prep="soaked"),
            Ingredient("grapeseed oil", 30, qtyUnit='ml'),
            Ingredient("nutritional yeast", 1, qtyUnit='tbsp'),
            Ingredient("garlic", 2, qtyUnit='clove', prep="minced"),
            Recipe("vegetable stock", yieldQty=1.44, yieldUnit='l'),
            Ingredient("white rice", 142, qtyUnit='g'),
            Ingredient("coconut milk", 240, qtyUnit='ml'),
            Ingredient("green onion", 45, qtyUnit='g'),
        ],
        "steps": [
            "In a medium pot, add the garlic and sweat until aroatmatic",
            "Add the stock, beans and oil",
            "Bring to a boil and then bring down to a simmer for 1 hour or until beans are tender",
            "Rinse the rice until the water runs clear, drain rice well before using",
            "Add the rice and coconut milk to the pot",
            "Cover and simmer until rice is tender, about 20 minutes, or until all the liquid is absorbed"
        ],
        "times": {"active": "10 minutes", "cook": "60-90 hour"},
    },
    "mushroom risotto": {
        "prepareAhead": "If using dried mushrooms, soak the mushrooms in water for 30-60 minutes",
        "yields":10,
        "yieldUnit":"each",
        "servings":10,
        "servingUnit":"each",
        "category":"grain",
        "subcategory":"rice",
        "tags": ["grain", "rice", "risotto"],
        "kosher": "pareve",
        "ingredients": [
            Ingredient("onion", 57, qtyUnit='g', prep="minced"),
            Ingredient("butter", 57, qtyUnit='g'),
            Ingredient("arborio rice", 397, qtyUnit='g'),
            Ingredient("dried wild mushrooms", 85, qtyUnit='g'),
            Recipe("vegetable stock", yieldQty=1.44, yieldUnit='l'),
        ],
        "steps": [
            "Soak the wildmushrooms in water for 30-60 minutes",
            "Drain the mushrooms and reserve the liquid",
            "Strain the liquid through a coffee filter to remove any grit and substitute it for the stock",
            "In a medium pot, add the oil and sweat the onions and mushrooms until the onions are translucent, 6-8 minutes",
            "Add the rice and toast until the rice is aromatic, about 1 minute",
            "Add the stock 1/3 at a time, stirring frequently until the stock is absorbed before adding more. Alternative to stirring, shaking the pot causes the rice to rub the starch off the grains and create a creamy texture",
            "Cook until the rice is tender and creamy, about 20-30 minutes",
            "Add the butter and cheese and stir until melted",
        ],
        "times": {"active": "20-25 minutes","soak":"30-60 minutes", "cook": "30-45 minutes"},
    },
    "mayonnaise" : {
        "yields":960,
        "yieldUnit":"ml",
        "servings":960/15,
        "servingUnit":"tbsp",
        "category":"sauces",
        "subcategory":"condiment",
        "tags": ["sauces", "mayonnaise"],
        "kosher": "pareve",
        "ingredients": [
            Recipe("egg yolk", yieldQty=75, yieldUnit='g'),
            Ingredient("water", 30, qtyUnit='ml'),
            Ingredient("white wine vinegar", 30, qtyUnit='ml'),
            Ingredient("dijon mustard", 10, qtyUnit='g'),
            Ingredient("sugar", 5, qtyUnit='g'),
            Ingredient("vegetable oil", 720, qtyUnit='ml'),
            Recipe("lemon juice", yieldQty=30, yieldUnit='ml'),
            Ingredient("salt", 5, qtyUnit='g'),
        ],
        "steps": [
            "Whisk together the egg yolk, water, vinegar, mustard, and sugar with a balloon whisk until slightly foamy",
            "Gradually whisk in the oil constantly whisking until the mixture is smooth and thick",
            "Season with lemon juice, salt, and pepper",
        ],
        "times": {"active": "5-10 minutes"},
    },
}