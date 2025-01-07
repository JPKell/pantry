import unittest

from test.init_db import test_db
from constants import *
from modules.ingredients import Ingredient


class TestIngredients(unittest.TestCase):

    def setUp(self):
        return super().setUp()
    
    def test_create_ingredient(self):
        # confirm it doesn't exist
        with self.assertRaises(Exception):
            Ingredient("test flour", db=test_db)

        # create it
        initData = {
            "displayName":"all-purpose flour",
            "measurement":"g", 
            "rawStorage":"room temperature", 
            "processedStorage":"room temperature",
            "shelfLife":365, 
            "category":"grain", 
            "subcategory":"flour", 
            "kosher":"pareve",
            "notes":"keep dry",
            "tags": "baking, thickening, breading, coating, dredging, roux",
            "conversions": {"cup": 120}
        }

        Ingredient("test flour", 
            initData=initData,
            db=test_db
        )

        # confirm it exists
        ap_flour = Ingredient("test flour", db=test_db)
        self.assertEqual(ap_flour.name, "test flour")

        # Create duplicate ingredient
        with self.assertRaises(Exception):
            Ingredient("test flour",initData=initData, db=test_db)

    ### There are 4 ingredients to test for conversion
    ## There are 2 systems, metric and imperial
    ## Each of these should be tested in the same type (mass to mass, mass to volume, volume to volume, volume to mass)
    # Base unit metric mass - Flour
    #   - mass to mass, mass to volume 
    # Base unit metric volume - Water
    #   - volume to volume, volume to mass 
    # Base unit imperial mass - Coffee
    #   - mass to mass, mass to volume
    # Base unit imperial volume

    def test_metric_mass_to_mass_conversions(self):
        # AP flour weighs 120g per cup and it's base unit is g 
        ap_flour = Ingredient("ap flour", db=test_db)

        # # test conversions within mass units
        self.assertEqual(ap_flour.convert(120, toUnit="g"), 120)
        self.assertEqual(ap_flour.convert(120, toUnit="kg"), 0.12)
        self.assertEqual(ap_flour.convert(1, toUnit="mg"), 1000)
        self.assertEqual(ap_flour.convert(LB, toUnit="lb"), 1)

        self.assertEqual(ap_flour.convert(1, fromUnit="g"), G)
        self.assertEqual(ap_flour.convert(1, fromUnit="kg"), KG)
        self.assertEqual(ap_flour.convert(1, fromUnit="mg"), MG)
        self.assertEqual(ap_flour.convert(1, fromUnit="lb"), LB)
        self.assertEqual(ap_flour.convert(1, fromUnit="oz"), OZ)

        self.assertEqual(ap_flour.convert(1000, fromUnit="mg", toUnit="kg"), 0.001)

    def test_metric_mass_to_volume_conversions(self):
        # AP flour weighs 120g per cup and it's base unit is g 
        ap_flour = Ingredient("ap flour", db=test_db)

        # test conversions between mass and volume units

        self.assertEqual(ap_flour.convert(120, toUnit="cup"), 1)
        self.assertAlmostEqual(ap_flour.convert(120, toUnit="tbsp"),CUP / TBSP)
        self.assertAlmostEqual(ap_flour.convert(120, toUnit="tsp"), CUP / TSP)

        self.assertAlmostEqual(ap_flour.convert(1, fromUnit="cup", toUnit='g'), 120)
        self.assertAlmostEqual(ap_flour.convert(1, fromUnit="cup"), 120)
        self.assertAlmostEqual(ap_flour.convert(1, fromUnit="tbsp"), 120 * TBSP / CUP)

    def test_metric_volume_to_volume_conversions(self):
        # Water weighs 1g per ml and it's base unit is ml. Nice easy conversions
        water = Ingredient("water", db=test_db)

        # # test conversions between volume units
        self.assertEqual(water.convert(100, toUnit="ml"), 100)
        self.assertEqual(water.convert(100, toUnit="l"), 0.1)
        self.assertEqual(water.convert(FL_OZ, toUnit="fl oz"), 1)
        self.assertEqual(water.convert(CUP, toUnit="cup"), 1)
        self.assertEqual(water.convert(TBSP, toUnit="tbsp"), 1)
        self.assertEqual(water.convert(TSP, toUnit="tsp"), 1)

        self.assertEqual(water.convert(1, fromUnit="ml"), ML)
        self.assertEqual(water.convert(1, fromUnit="l"), L)
        self.assertEqual(water.convert(1, fromUnit="fl oz"), FL_OZ)
        self.assertEqual(water.convert(1, fromUnit="cup"), CUP)
        self.assertEqual(water.convert(1, fromUnit="tbsp"), TBSP)

        self.assertAlmostEqual(water.convert(1000, fromUnit="ml", toUnit="l"), 1)
        self.assertAlmostEqual(water.convert(1, fromUnit="l", toUnit="fl oz"), 1000 / FL_OZ)

    def test_metric_volume_to_mass_conversions(self):
        water = Ingredient("water", db=test_db)

        # # test conversions between volume and mass units
        self.assertEqual(water.convert(100, toUnit="g"), 100)
        self.assertEqual(water.convert(100, toUnit="kg"), 0.1)
        self.assertEqual(water.convert(FL_OZ, toUnit="fl oz"), 1)
        self.assertEqual(water.convert(CUP, toUnit="g"), 236.588)
        self.assertEqual(water.convert(TBSP, toUnit="g"), 15)
        self.assertEqual(water.convert(TSP, toUnit="g"), 5)

        self.assertEqual(water.convert(1, fromUnit="g"), G)
        self.assertEqual(water.convert(1, fromUnit="kg"), KG)
        self.assertEqual(water.convert(1, fromUnit="oz"), OZ)
        self.assertEqual(water.convert(1, fromUnit="cup"), CUP)
        self.assertEqual(water.convert(1, fromUnit="tbsp"), TBSP)
        self.assertEqual(water.convert(1, fromUnit="tsp"), TSP)

        self.assertAlmostEqual(water.convert(1000, fromUnit="g", toUnit="kg"), 1)
        self.assertAlmostEqual(water.convert(1, fromUnit="kg", toUnit="oz"), 1000 / OZ)


    def test_each_to_mass(self):
        # Eggs are measured in each and it's base unit is each
        # weight of large egg is 57g and volume is 44ml
        egg = Ingredient("lg egg", db=test_db)

        # # test conversions between volume and mass units
        self.assertAlmostEqual(egg.convert(1, toUnit="g"), 57)
        self.assertAlmostEqual(egg.convert(1, toUnit="kg"), 0.057)
        self.assertAlmostEqual(egg.convert(1, toUnit="ml"), 44)
        self.assertAlmostEqual(egg.convert(1, toUnit="l"), 0.044)
        self.assertAlmostEqual(egg.convert(1, toUnit="fl oz"), 44 / FL_OZ )


if __name__ == '__main__':
    unittest.main()