from modules.ingredients import Ingredient
from modules.pantry import Pantry
from modules.recipe import Recipe
from modules.chef import Chef

# Bread test will used to test the basic functions of Ingredients, Foodstuff, and Recipe
from initData.ingredientsData import initIngredients

# Create ingredients. This is the same for the pantry and the recipe
pantryList = [
    ("ap flour", 908), 
    ("salt", 20), 
    ("water", 640), 
    ("instant dry yeast", 8),
    ("sugar", 1000)
    ]


#############################################
## Create and stock the pantry
#############################################

pantry = Pantry()

for name, qty in pantryList:
    pantry.addFood(Ingredient(name, initData=initIngredients[name], qty=qty))

pantry.console()


#############################################
## Write the bread recipe
#############################################
ingredientList = [("ap flour", 454), ("salt", 10), ("water", 320), ("instant dry yeast", 4)]

breadRecipe = Recipe("bread", 
                     ingredients= [Ingredient(name, **initIngredients[name], qty=qty) for name, qty in ingredientList], 
                     preheat=425,
                     servings=1,
                     servingUnit="loaf",
                     steps=[
                         "If you are conserned about your yeast or need to speed up the process, proof the yeast in the water with a pinch of sugar. Skip otherwise", 
                         "Combine the dry ingredients in a large bowl or bowl mixer bowl", 
                         "Add 3/4 of the water and mix until a shaggy dough forms. If the dough is too dry, add more water. If the dough is too wet, add more flour", 
                         "Knead the dough until it is smooth and elastic. This can take 10-15 minutes by hand or 5-7 minutes in a mixer",
                         "Place the dough in a greased bowl and cover with a towel. Let rise until doubled in size, about 1 - 1.5 hours",
                         "Punch down the dough and shape into a loaf. Place in a greased loaf pan and let rise until doubled in size, about 1 hour",
                         "Bake at 425 for 25-30 minutes or until the internal temperature reaches 190F or nice golden crust has formed and sounds hollow when you knock the bottom.",
                         "Let cool for at least 30 minutes before slicing"])

breadRecipe.scale = 2


#############################################
## Create a chef and make the bread
#############################################

chef = Chef(pantry)

chef.makeRecipe(breadRecipe)
