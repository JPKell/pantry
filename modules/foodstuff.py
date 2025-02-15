''' 
Both Ingredients and Recipes can be used in meals and recipes. This superclass 
will keep the things which should be common between them, like qty, prep instructions
and other meta data
'''
from modules.database import Db
 

class Foodstuff:
    def __init__(self, db:Db, recipePart:str=None, prep:str=None, displayUnit:str=None):
        self.db = db    
        self.prep = prep
        self.recipePart = recipePart    
        self.displayUnit = displayUnit

