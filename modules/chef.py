from datetime import datetime

from .ingredients import Ingredient
from .pantry import Pantry
from .recipe import Recipe
from .market import Market
from .database import db

class Chef:
    def __init__(self, pantry: Pantry, db=db):
        self.db = db
        self.pantry = pantry
        self.markets = []
        self.__get_markets__()
        self.recipes = []
        self.__get_recipes__()

    ## Init functions
    def __get_markets__(self):
        self.markets = [Market(x['name']) for x in self.db.query("SELECT * FROM markets")]

    def __get_recipes__(self):  
        self.recipes = [Recipe(x['name']) for x in self.db.query("SELECT * FROM recipes")]

    def makeRecipe(self, recipe: Recipe):
        # Check for stock
        for ingredient in recipe.ingredients:
            if ingredient not in self.pantry.stored:
                raise ValueError(f"{ingredient} not found in pantry")
            
        # Check pantry for ingredients before removing them
        for ingredient in recipe.ingredients:
            supply = self.pantry.stored[self.pantry.stored.index(ingredient)]
            if ingredient.qty > supply.qty:
                raise ValueError(f"Insufficient {ingredient.name} in pantry")
        [self.pantry.removeFood(i) for i in recipe.ingredients]

        # Log the recipe
        self.db.execute(f"INSERT INTO cooking_log (recipe_id, date, scale) VALUES ({recipe.id}, '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', {recipe.scale})") 

    def menu(self):
        _dict = {}
        for recipe in self.recipes:
            _dict[recipe.name]  = {
                "totalPrice": self.totalRecipePrice(recipe),
                "detailedPrice": self.detailedRecipePrice(recipe),
                "servings": recipe.servings,
                "servingUnit": recipe.servingUnit,
                "servingPrice": round(self.totalRecipePrice(recipe) / recipe.servings, 3),
                "category": recipe.category,
                "subcategory": recipe.subcategory,
            }
        return _dict
                

    def findBestIngredientPrice(self, ingredient: Ingredient):
        lowestPrice = None
        for market in self.markets:
            marketPrice = market.getPrice(ingredient)
            if marketPrice != None and lowestPrice == None:
                lowestPrice = marketPrice
            elif marketPrice != None and lowestPrice["total"] > marketPrice["total"]:
                lowestPrice = marketPrice

        if lowestPrice == None:
            raise ValueError(f"No price found for {ingredient.name}")

        return lowestPrice

            
    def detailedRecipePrice(self, recipe: Recipe):
        totals = {}
        for ingredient in recipe.ingredients:
            if isinstance(ingredient, Recipe):
                recipePrice = self.detailedRecipePrice(ingredient)
                recipePrice = sum([ x['total'] for x in recipePrice.values()])
                totals.update({ingredient.name: {'total': recipePrice}})
            else:
                lowestPrice = self.findBestIngredientPrice(ingredient)
                totals.update({ingredient.name: lowestPrice})
        return totals
    
    def totalRecipePrice(self, recipe: Recipe):
        totals = self.detailedRecipePrice(recipe)
        return round(sum([x['total'] for x in totals.values()]), 2)

    def detailedPantryValue(self):
        totals = {}
        for ingredient in self.pantry.stored:
            lowestPrice = self.findBestIngredientPrice(ingredient)
            totals.update({ingredient.name: {"qty": ingredient.qty, "marketDict":  lowestPrice}})
        return totals

    def totalPantryValue(self):
        totals = self.detailedPantryValue()
        return round(sum([x['total'] for x in totals.values()]), 2)