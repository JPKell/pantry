import unittest

from test.init_db import test_db
from constants import *
from modules.ingredients import Ingredient
from modules.recipe import Recipe


initData = {
        "preheat": "preheat oven",
        "preheatTemp": 425,
        "yields":1,
        "yieldUnit":"loaf",
        "yieldConversions": {
            "g": 1/100,
        },  
        "servings":10,
        "servingUnit":"slice",
        "servingConversions":{
            'g': 1/10
        },
        "category":"bread",
        "subcategory":"test",
        "kosher": "pareve",
        "tags": ["bread", "test"],
        "ingredients": [Ingredient("ap flour", 100, db=test_db), ],
        "steps": [
            "Step 1: Mix the ingredients",
            "Step 2: Let the dough rise",
            "Step 3: Shape the dough",
            "Step 4: Let the dough rise again",
            "Step 5: Bake the bread"
        ]
        }

test_db.execute("DELETE FROM recipes WHERE name = 'test bread'")

Recipe("test bread", 
    initData=initData,
    db=test_db
)

class TestRecipe(unittest.TestCase):

    def setUp(self):
        return super().setUp()
    
    def test_create_ingredient(self):
        # confirm it doesn't exist
        test_db.execute("DELETE FROM recipes WHERE name = 'test bread'")
        test_db.execute("DELETE FROM conversions WHERE name = 'test bread'")
        with self.assertRaises(Exception):
            Recipe("test bread", db=test_db)

        Recipe("test bread", 
            initData=initData,
            db=test_db
        )

        # confirm it exists
        bread = Recipe("test bread", db=test_db)
        self.assertEqual(bread.name, "test bread")

        # Create duplicate ingredient
        with self.assertRaises(Exception):
            Recipe("test bread",initData=initData, db=test_db)

    ## Recipes can be converted 2 ways, yield and servings 
    def test_scale(self):
        bread = Recipe("test bread", db=test_db)
        bread.scale = 2
        self.assertEqual(bread.yields, 2)
        self.assertEqual(bread.servings, 20)
        flour = bread.ingredients[0]
        self.assertEqual(flour.qty, 200)

    def test_scale_by_yield_of_same_unit(self):
        bread = Recipe("test bread", yieldQty=5, db=test_db)
        self.assertEqual(bread.yields, 5)
        self.assertEqual(bread.servings, 50)
        flour = bread.ingredients[0]
        self.assertEqual(flour.qty, 500)

    def test_scale_by_yield_of_known_unit_same_type(self):
        bread = Recipe("test bread", yieldQty=300, yieldUnit='g', db=test_db)
        self.assertEqual(bread.yields, 3)
        self.assertEqual(bread.servings, 30)
        flour = bread.ingredients[0]
        self.assertEqual(flour.qty, 300)

    def test_scale_by_yield_of_different_unit_same_type(self):
        newDict = {**initData}
        newDict['yields'] = 100
        newDict['yieldUnit'] = 'g'  
        Recipe("gram bread", initData=newDict, db=test_db)
        bread = Recipe("gram bread", yieldQty=0.3, yieldUnit='kg', db=test_db)

        self.assertEqual(bread.yields, 300)
        self.assertEqual(bread.servings, 30)
        flour = bread.ingredients[0]
        self.assertEqual(flour.qty, 300)

    def test_scale_by_yield_of_known_unit_different_type(self):
        # The recipe does not have a ml conversion for yield
        with self.assertRaises(Exception):
            Recipe("test bread", yieldQty=300, yieldUnit='ml', db=test_db)

        newData = {**initData}
        newData['yieldConversions']['ml'] = 1/100
        Recipe("yield bread", initData=newData, db=test_db)
        newBread = Recipe("yield bread", yieldQty=300, yieldUnit='ml', db=test_db)

        self.assertEqual(newBread.yields, 3)
        self.assertEqual(newBread.servings, 30)
        flour = newBread.ingredients[0]
        self.assertEqual(flour.qty, 300)

        newBread = Recipe("yield bread", yieldQty=1, yieldUnit='cup', db=test_db)

        self.assertEqual(newBread.yields, CUP/100) #100ml per yield
        self.assertEqual(newBread.servings, CUP/10) # 10 servings per yield
        flour = newBread.ingredients[0]
        self.assertAlmostEqual(flour.qty, CUP) # Rounding errors

    def test_scale_by_serving_of_same_unit(self):
        bread = Recipe("test bread", servingQty=5, db=test_db)
        self.assertEqual(bread.yields, 0.5)
        self.assertEqual(bread.servings, 5)
        flour = bread.ingredients[0]
        self.assertEqual(flour.qty, 50)

    def test_scale_by_serving_of_known_unit_same_type(self):
        # Test recipe has 1 loaf yielding 10 slices at 10 g each
        bread = Recipe("test bread", servingQty=30, servingUnit='g', db=test_db)
        self.assertAlmostEqual(bread.yields, 0.3)
        self.assertAlmostEqual(bread.servings, 3)
        flour = bread.ingredients[0]
        self.assertAlmostEqual(flour.qty, 30)

    def test_scale_by_serving_of_different_unit_same_type(self):
        bread = Recipe("test bread", servingQty=0.3, servingUnit='kg', db=test_db)
        self.assertEqual(bread.yields, 3)
        self.assertEqual(bread.servings, 30)
        flour = bread.ingredients[0]
        self.assertEqual(flour.qty, 300)

    def test_scale_by_serving_of_known_unit_different_type(self):
        # The recipe does not have a ml conversion for yield
        with self.assertRaises(Exception):
            Recipe("test bread", servingQty=300, servingUnit='ml', db=test_db)

        newData = {**initData}
        newData['servingConversions']['ml'] = 1/10
        Recipe("serving bread", initData=newData, db=test_db)
        newBread = Recipe("serving bread", servingQty=300, servingUnit='ml', db=test_db)

        self.assertEqual(newBread.yields, 3)
        self.assertEqual(newBread.servings, 30)
        flour = newBread.ingredients[0]
        self.assertEqual(flour.qty, 300)

        newBread = Recipe("serving bread", servingQty=1, servingUnit='cup', db=test_db)

        self.assertAlmostEqual(newBread.yields, CUP/100) #100ml per yield
        self.assertAlmostEqual(newBread.servings, CUP/10) # 10 servings per yield
        flour = newBread.ingredients[0]
        self.assertAlmostEqual(flour.qty, CUP) # Rounding errors



if __name__ == '__main__':
    unittest.main()