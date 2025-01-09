import unittest 


from constants import *
from modules.converter import Converter


class TestConverter(unittest.TestCase):

    def test_set_base_units(self):
        converter = Converter()
        self.assertEqual(converter.baseUnit, None)

        converter.baseUnit = "c"
        self.assertEqual(converter.baseUnit, "c")
        self.assertEqual(converter._baseName, "celsius")
        self.assertEqual(converter._baseType, "temperature")
        self.assertEqual(converter._baseSystem, "metric")
        self.assertEqual(converter._baseFactor, 1)

        converter.baseUnit = None
        self.assertEqual(converter.baseUnit, None)
        self.assertEqual(converter._baseName, None)
        self.assertEqual(converter._baseType, None)
        self.assertEqual(converter._baseSystem, None)
        self.assertEqual(converter._baseFactor, None)

        converter.baseUnit = 'kg'
        self.assertEqual(converter.baseUnit, 'kg')
        self.assertEqual(converter._baseName, 'kilogram')
        self.assertEqual(converter._baseType, 'mass')
        self.assertEqual(converter._baseSystem, 'metric')
        self.assertEqual(converter._baseFactor, 1000)
        

class TestTemperatureConverter(unittest.TestCase):
    converter = Converter(baseUnit="c")

    def test_convert_bad_units(self):
        # Including both measures, temperature is base unit
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='c', toUnit='g')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g', toUnit='c')

        # Including both measures, temperature is NOT base unit
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='f', toUnit='g')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g', toUnit='f')

        # Including only one measure, temperature assumed base unit
        with self.assertRaises(ValueError):
            self.converter.convert(100, toUnit='g')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g')

    def test_convert_c_to_f(self):
        self.assertAlmostEqual(self.converter.convert(0, toUnit='f'), 32)
        self.assertAlmostEqual(self.converter.convert(100, toUnit='f'), 212)
        self.assertAlmostEqual(self.converter.convert(37, toUnit='f'), 98.6)

        self.assertAlmostEqual(self.converter.convert(0,fromUnit='c', toUnit='f'), 32)
        self.assertAlmostEqual(self.converter.convert(100,fromUnit='c', toUnit='f'), 212)
        self.assertAlmostEqual(self.converter.convert(37,fromUnit='c', toUnit='f'), 98.6)

        self.assertAlmostEqual(self.converter.convert(0,fromUnit='c'), 32)
        self.assertAlmostEqual(self.converter.convert(100,fromUnit='c'), 212)
        self.assertAlmostEqual(self.converter.convert(37,fromUnit='c'), 98.6)

    def test_convert_f_to_c(self):
        self.assertAlmostEqual(self.converter.convert(32, toUnit='c'), 0)
        self.assertAlmostEqual(self.converter.convert(212, toUnit='c'), 100)
        self.assertAlmostEqual(self.converter.convert(98.6, toUnit='c'), 37)

        self.assertAlmostEqual(self.converter.convert(32,fromUnit='f', toUnit='c'), 0)
        self.assertAlmostEqual(self.converter.convert(212,fromUnit='f', toUnit='c'), 100)
        self.assertAlmostEqual(self.converter.convert(98.6,fromUnit='f', toUnit='c'), 37)

        self.assertAlmostEqual(self.converter.convert(32,fromUnit='f'), 0)
        self.assertAlmostEqual(self.converter.convert(212,fromUnit='f'), 100)
        self.assertAlmostEqual(self.converter.convert(98.6,fromUnit='f'), 37)


class TestMassConverter(unittest.TestCase):
    converter = Converter(baseUnit="g")
    def test_convert_bad_units(self):
        # Including both measures, mass is base unit
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g', toUnit='c')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='c', toUnit='g')
        # if toUnit is temperature, then the fromUnit is assumed to be the opposite temperature and vice versa
        # so we are not testing 
        # self.converter.convert(100, toUnit='c') or self.converter.convert(100, fromUnit='f')

        # Try again unknown units to raise error
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g', toUnit='ml')        
        with self.assertRaises(ValueError):
            self.converter.convert(100, toUnit='ml')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='ml', toUnit='g')        
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='ml')

    def test_convert_within_mass(self):
        self.assertEqual(self.converter.convert(120, toUnit='g'), 120)
        self.assertEqual(self.converter.convert(120, toUnit='kg'), 0.12)
        self.assertEqual(self.converter.convert(1, toUnit='mg'), 1000)
        self.assertAlmostEqual(self.converter.convert(LB, toUnit='lb'), 1)
        self.assertAlmostEqual(self.converter.convert(OZ, toUnit='oz'), 1)

        self.assertAlmostEqual(self.converter.convert(1, fromUnit='g'), G)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='kg'), KG)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='mg'), MG)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='lb'), LB)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='oz'), OZ)

        self.assertAlmostEqual(self.converter.convert(1000, fromUnit='mg', toUnit='kg'), 0.001)

    def test_convert_to_volume(self):
        # fresh converter for this to avoid conflicts
        converter = Converter(baseUnit="g")

        # Start by making sure that it fails without known Conversions
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g', toUnit='ml')
        with self.assertRaises(ValueError):
            self.converter.convert(100, toUnit='ml')

        # Add the conversion
        # Here 1 ml = 10 g
        converter.knownConversions = {'ml': 10}

        # Now it should work
        self.assertAlmostEqual(converter.convert(100, fromUnit='g', toUnit='ml'), 10)

        converter.knownConversions = {'ml': 1}
        # self.assertAlmostEqual(converter.convert(100, fromUnit='g', toUnit='ml'), 100)
        self.assertAlmostEqual(converter.convert(CUP, fromUnit='g', toUnit='cup'), 1)
        self.assertAlmostEqual(converter.convert(1, fromUnit='g', toUnit='cup'), 1/CUP)
        self.assertAlmostEqual(converter.convert(CUP, toUnit='cup'), 1)
        self.assertAlmostEqual(converter.convert(1, toUnit='cup'), 1/CUP)
        self.assertAlmostEqual(converter.convert(1, fromUnit='cup'), CUP)
        self.assertAlmostEqual(converter.convert(1/CUP, fromUnit='cup'), 1)

        converter.knownConversions = {'ml': 3.5}
        self.assertAlmostEqual(converter.convert(1, fromUnit='g', toUnit='ml'), 1/3.5)
        self.assertAlmostEqual(converter.convert(10, fromUnit='g', toUnit='ml'), 10/3.5)
        self.assertAlmostEqual(converter.convert(1, toUnit='ml'), 1/3.5)
        self.assertAlmostEqual(converter.convert(10, toUnit='ml'), 10/3.5)
        self.assertAlmostEqual(converter.convert(1/3.5, fromUnit='ml'), 1)
        self.assertAlmostEqual(converter.convert(10/3.5, fromUnit='ml'), 10)

        converter.knownConversions = {'cup': 120}
        self.assertAlmostEqual(converter.convert(120, fromUnit='g', toUnit='cup'), 1)
        self.assertAlmostEqual(converter.convert(1, fromUnit='g', toUnit='cup'), 1/120)
        self.assertAlmostEqual(converter.convert(120, toUnit='cup'), 1)
        self.assertAlmostEqual(converter.convert(1, toUnit='cup'), 1/120)
        self.assertAlmostEqual(converter.convert(120, toUnit='tbsp'), CUP/TBSP)

        self.assertAlmostEqual(converter.convert(CUP/TBSP, fromUnit='tbsp'), 120)



    def test_convert_to_count(self):
        ...

class TestVolumeConverter(unittest.TestCase):
    converter = Converter(baseUnit="ml")

    def test_convert_bad_units(self):
        # Including both measures, volume is base unit
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='ml', toUnit='c')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='c', toUnit='ml')

        # Try again unknown units to raise error
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='ml', toUnit='g')
        with self.assertRaises(ValueError):
            self.converter.convert(100, toUnit='g')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g', toUnit='ml')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g')

    def test_convert_within_volume(self):
        self.assertEqual(self.converter.convert(120, toUnit='ml'), 120)
        self.assertEqual(self.converter.convert(120, toUnit='l'), 0.12)
        self.assertEqual(self.converter.convert(1, toUnit='cl'), 0.1)
        self.assertEqual(self.converter.convert(CUP, toUnit='cup'), 1)
        self.assertEqual(self.converter.convert(TSP, toUnit='tsp'), 1)
        self.assertEqual(self.converter.convert(TBSP, toUnit='tbsp'), 1)
        self.assertEqual(self.converter.convert(GAL, toUnit='gal'), 1)

        self.assertAlmostEqual(self.converter.convert(1, fromUnit='ml'), 1)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='l'), 1000)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='cl'), 10)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='cup'), CUP)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='tsp'), TSP)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='tbsp'), TBSP)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='gal'), GAL)

    def test_convert_to_mass(self):
        counter = Converter(baseUnit="ml")

        # Start by making sure that it fails without known Conversions
        with self.assertRaises(ValueError):
            counter.convert(100, fromUnit='ml', toUnit='g')
        with self.assertRaises(ValueError):
            counter.convert(100, toUnit='g')

        # Add the conversion
        # Here 1 ml = 10 g
        counter.knownConversions = {'g': 10}

        # Now it should work
        self.assertAlmostEqual(counter.convert(100, fromUnit='ml', toUnit='g'), 10)
        self.assertAlmostEqual(counter.convert(100, toUnit='g'), 10)
        self.assertAlmostEqual(counter.convert(100, fromUnit='g', toUnit='ml'), 1000)
        self.assertAlmostEqual(counter.convert(100, fromUnit='g'), 1000)

        counter.knownConversions = {'g': 3.5}
        self.assertAlmostEqual(counter.convert(1, fromUnit='ml', toUnit='g'), 1/3.5)
        self.assertAlmostEqual(counter.convert(10, toUnit='g'), 10/3.5)
        self.assertAlmostEqual(counter.convert(1, fromUnit='g', toUnit='ml'), 3.5)
        self.assertAlmostEqual(counter.convert(10, fromUnit='g'), 35)


    def test_convert_to_count(self):
        ...


class TestCountConverter(unittest.TestCase):
    converter = Converter(baseUnit="unit")

    def test_convert_bad_units(self):
        # Including both measures, count is base unit
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='each', toUnit='c')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='c', toUnit='each')

        # Try again unknown units to raise error
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='unit', toUnit='g')
        with self.assertRaises(ValueError):
            self.converter.convert(100, toUnit='g')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g', toUnit='unit')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='g')

        # Check it in volume just to be sure
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='unit', toUnit='ml')
        with self.assertRaises(ValueError):
            self.converter.convert(100, toUnit='ml')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='ml', toUnit='unit')
        with self.assertRaises(ValueError):
            self.converter.convert(100, fromUnit='ml')

    def test_convert_within_count(self):
        self.assertEqual(self.converter.convert(120, toUnit='unit'), 120)
        self.assertEqual(self.converter.convert(120, toUnit='each'), 120)
        self.assertEqual(self.converter.convert(120, toUnit='dozen'), 10)
        self.assertEqual(self.converter.convert(12, toUnit='dozen'), 1)

        self.assertAlmostEqual(self.converter.convert(1, fromUnit='unit'), 1)
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='dozen'), 12)
        self.assertAlmostEqual(self.converter.convert(1/12, fromUnit='dozen'), 1)

        # Test a custom conversion
        self.converter.knownConversions = {'bunch': 24}
        self.assertAlmostEqual(self.converter.convert(1, fromUnit='bunch', toUnit="whole"), 24)
        self.assertAlmostEqual(self.converter.convert(24, toUnit='bunch'), 1)
        self.assertAlmostEqual(self.converter.convert(2, fromUnit='dozen', toUnit='bunch'), 1)

    def test_convert_to_mass(self):
        counter = Converter(baseUnit="each")
        
        # Start by making sure that it fails without known Conversions
        with self.assertRaises(ValueError):
            counter.convert(100, fromUnit='each', toUnit='g')

        # Add the conversion
        counter.knownConversions = {'g': 1/10, 'ml': 1/100}
        self.assertAlmostEqual(counter.convert(1, fromUnit='each', toUnit='g'), 10)
        self.assertAlmostEqual(counter.convert(1, toUnit='g'), 10)
        self.assertAlmostEqual(counter.convert(1, fromUnit='whole', toUnit='g'), 10)
        self.assertAlmostEqual(counter.convert(1, fromUnit='dozen', toUnit='g'), 120)
        self.assertAlmostEqual(counter.convert(10, fromUnit='each', toUnit='g'), 100)
        self.assertAlmostEqual(counter.convert(20, fromUnit="each", toUnit='kg'), 0.2)
        self.assertAlmostEqual(counter.convert(20, fromUnit="each", toUnit='kg'), 0.2)
        self.assertAlmostEqual(counter.convert(20, toUnit='kg'), 0.2)
        self.assertAlmostEqual(counter.convert(0.2, fromUnit='kg'), 20)


    def test_convert_to_volume(self):
        counter = Converter(baseUnit="each")

        # Start by making sure that it fails without known Conversions
        with self.assertRaises(ValueError):
            counter.convert(100, fromUnit='each', toUnit='ml')

        # Add the conversion
        counter.knownConversions = {'g': 1/10, 'ml': 1/100}
        self.assertAlmostEqual(counter.convert(1, fromUnit='each', toUnit='ml'), 100)
        self.assertAlmostEqual(counter.convert(1, toUnit='ml'), 100)
        self.assertAlmostEqual(counter.convert(1, fromUnit='whole', toUnit='ml'), 100)
        self.assertAlmostEqual(counter.convert(1, fromUnit='dozen', toUnit='ml'), 1200)
        self.assertAlmostEqual(counter.convert(10, fromUnit='each', toUnit='ml'), 1000)
        self.assertAlmostEqual(counter.convert(20, fromUnit="each", toUnit='l'), 2)
        self.assertAlmostEqual(counter.convert(20, toUnit='l'), 2)
        self.assertAlmostEqual(counter.convert(0.2, fromUnit='l'), 2)
        
    def test_converting_between_volume_and_mass(self):
        counter = Converter(baseUnit="each")

        # Start by making sure that it fails without known Conversions
        with self.assertRaises(ValueError):
            counter.convert(100, fromUnit='g', toUnit='ml')

        # Add the conversion
        counter.knownConversions = {'g': 1/10, 'ml': 1/100}
        self.assertAlmostEqual(counter.convert(1, fromUnit='g', toUnit='ml'), 10)
        self.assertAlmostEqual(counter.convert(100, fromUnit='ml', toUnit='g'), 10)

    