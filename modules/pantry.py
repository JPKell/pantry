from .ingredients import Ingredient 
from .database import db


class Pantry:
    _stored = []

    def __init__(self, db=db):
        self.db = db

    @property
    def stored(self):
        if len(self._stored) == 0:
            self.__load_from_db__()
        return self._stored
    
    ## init methods
    def __load_from_db__(self):
        _pantry = self.db.query("SELECT * FROM pantry")
        for item in _pantry: 
            self._stored.append(Ingredient(item['ingredient'], qty=item['qty']))

    def addFood(self, ingredient: Ingredient):
        # If a unit is added, check against the ingredient's measurement and preform conversion if necessary
        
        if ingredient in self.stored:
            storedIngredient = self.stored[self.stored.index(ingredient)]   
            storedIngredient.qty += ingredient._qty
            self.db.execute(f"UPDATE pantry SET qty = {storedIngredient.qty} WHERE ingredient = '{ingredient.name}'")
        else:
            self.stored.append(ingredient)
            self.__add_to_db__(ingredient)

            
    def removeFood(self, ingredient: Ingredient):
        if ingredient not in self.stored:
            raise ValueError(f"{ingredient} not found in stored ingredients")
            
        storedIngredient = self.stored[self.stored.index(ingredient)]
        storedIngredient.qty -= ingredient._qty

        
        if storedIngredient.qty <= 0:
            self.stored.pop(self.stored.index(ingredient))
            self.db.execute(f"DELETE FROM pantry WHERE ingredient = '{ingredient.name}'")
        else:
            self.db.execute(f"UPDATE pantry SET qty = {storedIngredient.qty} WHERE ingredient = '{ingredient.name}'")
        
    ## Private methods
    def __add_to_db__(self, ingredient: Ingredient) -> None:
        self.db.insert("pantry", {"ingredient":ingredient.name.replace("'", "''"), "qty":ingredient._qty})
