from modules.ingredients import Ingredient
from modules.recipe import Recipe
from constants import *

# Create a bread recipe
doubleCompoundRecipes = {
    "challah french toast" : {
        "preheat": 'stove top medium heat',
        "yields":2,
        "yieldUnit":"slice",
        "servings":2,
        "servingUnit":"slice",
        "prepAhead": "dry the bread overnight or dry in over/toaster oven",
        "category":"breakfast",
        "subcategory":"toast",
        "tags": ["bread", "french toast", "challah"],
        "kosher": "pareve",
        "ingredients": [
            Recipe("challah", servingQty=2, servingUnit='slice'),
            Ingredient("lg egg", 2),
            Ingredient("water", 1, qtyUnit='tbsp'),
            Ingredient("grapeseed oil", 1, qtyUnit='tsp'),
            Ingredient("salt", 1, qtyUnit='tsp'), 
        ],
        "steps": [
            "Heat the oil in a pan over medium heat",
            "Whisk the egg, water, and salt in a bowl",
            "Soak the bread in the egg mixture",
            "Fry the bread until golden brown on both sides",
        ],
    },
}