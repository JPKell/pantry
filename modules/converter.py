from constants import *

measures = {
     "ml":            {"factor": ML,            "name": "milliliter",    "type":"volume","system": "metric"},
     "cl":            {"factor": CL,            "name": "centiliter",    "type":"volume","system": "metric"},
     "l":             {"factor": L,             "name": "liter",         "type":"volume","system": "metric"},
     "tsp":           {"factor": TSP,           "name": "teaspoon",      "type":"volume","system": "imperial"},
     "tbsp":          {"factor": TBSP,          "name": "tablespoon",    "type":"volume","system": "imperial"},
     "cup":           {"factor": CUP,           "name": "cup",           "type":"volume","system": "imperial"},
     "qt":            {"factor": QT,            "name": "quart",         "type":"volume","system": "imperial"},
     "fl oz":         {"factor": FL_OZ,         "name": "fluid ounce",   "type":"volume","system": "imperial"},
     "gal":           {"factor": GAL,           "name": "gallon",        "type":"volume","system": "imperial"}, # US gallon
     "pint":          {"factor": US_PINT,       "name": "US pint",       "type":"volume","system": "imperial"},
     "us pint":       {"factor": US_PINT,       "name": "US pint",       "type":"volume","system": "imperial"},
     "imperial pint": {"factor": IMPERIAL_PINT, "name": "Imperial pint", "type":"volume","system": "imperial"},

    # Mass
     "mg":    {"factor": MG,     "name": "miligram",    "type":"mass",  "system": "metric"},
     "g":     {"factor": G,      "name": "gram",        "type":"mass",  "system": "metric"},
     "kg":    {"factor": KG,     "name": "kilogram",    "type":"mass",  "system": "metric"},
     "oz":    {"factor": OZ,     "name": "ounce",       "type":"mass",  "system": "imperial"},
     "lb":    {"factor": LB,     "name": "pound",       "type":"mass",  "system": "imperial"},
    
    # Count 
     "each":  {"factor": 1,      "name": "each",        "type":"count", "system": "metric"},
     "unit":  {"factor": 1,      "name": "unit",        "type":"count", "system": "metric"},
     "dozen": {"factor": 12,     "name": "dozen",       "type":"count", "system": "metric"},
     "slice": {"factor": 1,      "name": "slice",       "type":"count", "system": "metric"},
     "loaf":  {"factor": 1,      "name": "loaf",        "type":"count", "system": "metric"},
     "clove": {"factor": 1,      "name": "clove",       "type":"count", "system": "metric"},
     "whole": {"factor": 1,      "name": "whole",       "type":"count", "system": "metric"},
     "bunch": {"factor": 1,      "name": "bunch",       "type":"count", "system": "metric"},
     "stick": {"factor": 1,      "name": "stick",       "type":"count", "system": "metric"},
     "sprig": {"factor": 1,      "name": "sprig",       "type":"count", "system": "metric"},

    # Temperature
     "c":     {"factor": 1,      "name": "celsius",     "type":"temperature", "system": "metric"},
     "f":     {"factor": 1,      "name": "fahrenheit",  "type":"temperature", "system": "imperial"},
}


class Converter:
    ''' Unit conversion is an important function of this program.
        Reimplementation of conversion for different classes is error prone so consolidate everything here.

        Everything should be in metric and conversions made to and from metric as needed.
    '''

    def __init__(self, baseUnit:str=None, knownConversions:dict=None):
        ''' converter will be initialized with every ingredient and recipe object. To speed up bulk conversions
            only load the bare minimum at initialization.'''
        ################
        # Set attributes
        # When the converter is instantiated with an object these attributes which belong to the object and will not change.
        self._baseUnit:str = None           # baseUnit is the default measurement for the object this converter is attached to.
        self._baseName:str = None           # full name of the unit
        self._baseType:str = None           # mass, volume, count, temperature
        self._baseSystem:str = None         # imperial, metric
        self._baseFactor:float = None       # factor to convert to metric
        self.baseUnit = baseUnit            # the class property will get additional information from the measures dictionary.

        self._knownConversions:dict = None      # knownConversions is used to convert between different types of units. ie grams to cups
        self.knownConversions = knownConversions  # known conversions must always match on the toType if toType varies from the baseType


        # The following will be used during conversions and will fluctuate depending on the conversion needed.
        self._fromUnit:str = None         # measurement unit that the value is currently in. Class property
        self._fromName:str = None         # full name of the unit 
        self._fromType:str = None         # mass, volume, count, temperature
        self._fromSystem:str = None       # imperial, metric
        self._fromFactor:float = None     # factor to convert to metric

        self._toUnit:str = None           # measurement unit that the value will be converted to.
        self._toName:str = None           
        self._toType:str = None           
        self._toSystem:str = None         
        self._toFactor:float = None


    ################
    # Properties
    # These are attributes that when set should trigger the retrieval of more data
    @property
    def baseUnit(self) -> str:
        return self._baseUnit
    
    @baseUnit.setter
    def baseUnit(self, value:str):
        # Reset the attribute values if the value is None
        if value == None:
            self._baseUnit   = None
            self._baseName   = None
            self._baseType   = None
            self._baseSystem = None
            self._baseFactor = None 
            return
        
        if not isinstance(value, str):
            raise TypeError("baseUnit must be a string")
        
        value = value.lower()
        # If the values are the same we can skip the rest of the function
        if value == self._baseUnit:
            return
        
        self._baseUnit = value
        
        # Get details of the unit
        unitDict = measures.get(self._baseUnit)
        if unitDict is None:
            raise ValueError(f"Unit {self._baseUnit} not found in measures")
        
        self._baseName   = unitDict.get("name")
        self._baseType   = unitDict.get("type")
        self._baseSystem = unitDict.get("system")
        self._baseFactor = unitDict.get("factor")

    @property
    def fromUnit(self) -> str:
        return self._fromUnit
    
    @fromUnit.setter
    def fromUnit(self, value:str):
        # Reset the attribute values if the value is None
        if value == None:
            self._fromUnit   = None
            self._fromName   = None
            self._fromType   = None
            self._fromSystem = None
            self._fromFactor = None 
            return
        
        if not isinstance(value, str):
            raise TypeError("fromUnit must be a string")
        
        value = value.lower()
        # If the values are the same we can skip the rest of the function
        if value == self._fromUnit:
            return

        self._fromUnit = value.lower()
        
        # Get details of the unit
        unitDict = measures.get(self._fromUnit)
        if unitDict is None:
            raise ValueError(f"Unit {self._fromUnit} not found in measures")
        
        self._fromName   = unitDict.get("name")
        self._fromType   = unitDict.get("type")
        self._fromSystem = unitDict.get("system")
        self._fromFactor = unitDict.get("factor")

    @property
    def toUnit(self) -> str:
        return self._toUnit
    
    @toUnit.setter
    def toUnit(self, value:str):
        # Reset the attribute values if the value is None
        if value == None:
            self._toUnit   = None
            self._toName   = None
            self._toType   = None
            self._toSystem = None
            self._toFactor = None 
            return
        
        if not isinstance(value, str):
            raise TypeError("fromUnit must be a string")
        
        value = value.lower()
        # If the values are the same we can skip the rest of the function
        if value == self._toUnit:
            return
        
        self._toUnit = value

        # Get details of the unit
        unitDict = measures.get(self._toUnit)
        if unitDict is None:
            raise ValueError(f"Unit {self._toUnit} not found in measures")
        
        self._toName   = unitDict.get("name")
        self._toType   = unitDict.get("type")
        self._toSystem = unitDict.get("system")
        self._toFactor = unitDict.get("factor")

    @property
    def knownConversions(self) -> dict:
        return self._knownConversions
    
    @knownConversions.setter
    def knownConversions(self, value:dict):
        # Reset the attribute values if the value is None
        if value == None:
            self._knownConversions = None
            return
        
        if not isinstance(value, dict):
            raise TypeError("knowConversions must be a dictionary like {'unit':  factor}}")
        
        output = {}
        for unit, value in value.items():
            if unit not in measures:
                raise ValueError(f"knowConversion unit {unit} not found in measures")
            # deep copy the dictionary so we don't change the original
            output[unit] = { **measures[unit] }
            output[unit]["factor"] = value        

        self._knownConversions = output




    def convert(self, value:float, fromUnit:str=None, toUnit:str=None) -> float:
        ''' Convert a value from one unit to another.
            This is the meat and potatoes of the converter. Keep it clean and easy to make sense of
        '''
        # There are many ways to convert units. The variables are...
        # fromUnit: mass, volume, count or temperature
        # toUnit: mass, volume, count or temperature
        # 
        # system: imperial or metric
        # 
        # temperature conversions are a little different. They are not simple factor of 10 like mass and volume. 
        # so if the conversion is between temperature units we will need to split the logic here

        # Count to count is 1 to 1 unless we have a known conversion between counts
        # Count to mass or volume is a little more difficult. ie 1 clove of garlic to grams


        # The simplest conversion is when they are both the same unit. ie grams to grams
        # 
        # The next simplest is when they are both the same type but different units. ie grams to kilograms or cups to ml
        # 
        # Next we will have an easy time if the to or from unit is a known conversion. ie grams to cups
        # 
        # The most difficult is when the from and to units are different types. ie grams to cups 
        

        if fromUnit == None and toUnit == None:
            raise ValueError("Either fromUnit or toUnit must be provided")

        # Setting the up the conversion units. 
        self.fromUnit = fromUnit
        self.toUnit   = toUnit

        # Simplest case is the from and to units are the same
        if self._fromUnit == self._toUnit:
            return value

        # split the logic for temperature conversions before we fill in the missing units
        # Temperature is either Celsius or Fahrenheit and if fromUnit was provided but not toUnit we will assume the opposite unit for the toUnit
        if self._baseType == "temperature" or self._fromType == "temperature" or self._toType == "temperature":
            return self.__convert_temperature__(value)

        # One of the units may not have been provided so we will assume the base unit for that one.
        self.__set_missing_units_to_base_unit__()

        # If the from and to units are the same type we can convert them directly
        if self._fromType == self._toType and self._fromType != "count":
            return value * self._fromFactor / self._toFactor
    

        # split the logic for count conversions
        if self._fromType == "count" or self._toType == "count":
            return self.__convert_count__(value)

        # From here the only conversions left are mass to volume and volume to mass
        # These can be done with a single method

        return self.__convert_mass_and_volume__(value)
    
    ################
    # Conversion functions
    def __convert_temperature__(self, value:float) -> float:
        ''' Convert between Celsius and Fahrenheit '''
        # Check that there are no unexpected units
        if self._fromUnit not in ["c", "f", None] or self._toUnit not in ["c", "f", None] or (self._fromUnit not in ["c", "f", None] and self._toUnit not in ["c", "f", None]):
            raise ValueError(f"Conversion from {self._fromUnit} to {self._toUnit} not supported")

        # If the toUnit was not provided we will assume the opposite unit for the toUnit
        if self._toUnit == None:
            self.toUnit = "f" if self._fromUnit == "c" else "c"
        # If toUnit was provided we will assume the fromUnit is the opposite since same unit conversions are caught in the main conversion function
        else:
            self.fromUnit = "f" if self._toUnit == "c" else "c"

        if self._toUnit == "f":
            return (value * 9/5) + 32
        elif self._toUnit == "c":
            return (value - 32) * 5/9
        else:
            raise ValueError(f"Conversion from {self._fromUnit} to {self._toUnit} not supported")

    def __convert_mass_and_volume__(self, value:float) -> float:
        ''' 
            At this point we can assume the following:
            - The from and to units are not the same type
            - The from and to units are not temperature
            - The from and to units are not count

            We need at least one know conversion type to do the conversion.
            The other type must either be known in the knownConversions or the baseType  
        '''
        # Must be at least one knownConversion to proceed or we will raise an error assuming there is data
        if self.knownConversions == None:
            raise ValueError("No known conversions provided")

        # Find the known conversion types which are compatible with one of the units
        knownConversionTypes = []
        if self.knownConversions != None:
            knownConversionTypes = [x['type'] for x in self.knownConversions.values()]

        # To do a conversion across different types we need to know at least one conversion type
        if len(knownConversionTypes) == 0:
            raise ValueError(f"Conversion from {self._fromType} to {self._toType} not supported")

        fromMatchFound = False
        toMatchFound = False
        if self.fromUnit in self.knownConversions:
            fromMatchFound = True
            self._fromFactor = self.knownConversions[self.fromUnit]['factor']
        
        if self.toUnit in self.knownConversions:
            toMatchFound = True
            self._toFactor = self.knownConversions[self.toUnit]['factor']

        # This a
        # if matchFound:
        #     return value * self._fromFactor / self._toFactor

            # If we know the conversion type for the from unit we can convert to the base unit
        if not fromMatchFound and self._fromType in knownConversionTypes:
            knownMeasure = [k for k,v in self.knownConversions.items() if v['type'] == self._fromType][0]
            knownFactor = self.knownConversions[knownMeasure]['factor']
            self._fromFactor = knownFactor * measures[self._fromUnit]['factor'] / measures[knownMeasure]['factor']

        # If we know the conversion type for the to unit we can convert from the base unit
        if not toMatchFound and self._toType in knownConversionTypes:
            knownMeasure = [k for k,v in self.knownConversions.items() if v['type'] == self._toType][0]
            knownFactor = self.knownConversions[knownMeasure]['factor']
            self._toFactor = knownFactor / measures[knownMeasure]['factor'] * measures[self._toUnit]['factor']

        return value * self._fromFactor / self._toFactor

        
    def __convert_count__(self, value:float) -> float:
        ''' Convert a value to and or from count '''
        # Count does not convert cleanly between other counts, they tend to be specific to the ingredient
        # 1 bunch of parsley has a different number of stems than one bunch of green onions
        # So count to count conversions will require a known conversion

        knownConversionTypes = []
        if self.knownConversions != None:
            knownConversionTypes = [x['type'] for x in self.knownConversions.values()]
            
        # We need to determine if we can get a known conversion for the from or to unit
        # We need to at least match on a know conversion type
        if self._toType != "count" and self._toType != self._baseType:
            if self.knownConversions == None or self._toType not in knownConversionTypes:
                raise ValueError(f"Conversion from {self._fromType} to {self._toType} not supported")

        if self._fromType != "count" and self._fromType != self._baseType:
            if self.knownConversions == None or self._fromType not in knownConversionTypes:
                raise ValueError(f"Conversion from {self._fromType} to {self._toType} not supported")


        if self.knownConversions == None:
            if self._fromType == "count" and self._toType == "count":
                return value * self._fromFactor / self._toFactor
            raise ValueError("No known conversions provided")


        # If we know one of the conversions we can convert the value to the other unit
        matchFound = False
        if self.fromUnit in self.knownConversions:
            self._fromFactor = self.knownConversions[self.fromUnit]['factor']
            matchFound = True

        # Check both conversion factors incase we need to convert to the other unit as well
        if self.toUnit in self.knownConversions:
            self._toFactor = self.knownConversions[self.toUnit]['factor']
            matchFound = True

        if matchFound:
            return value * self._fromFactor / self._toFactor

        # If both types are count and we don't have a known conversion then use the base unit to convert
        if self._fromType == "count" and self._toType == "count":
            return value * self._fromFactor / self._toFactor

        # From here out we know that we don't know a direct conversion for any of the units 
        # and that they are not both count. 
        # The options are: 
        # - 1 count and 1 not-count (mass/volume)
        # - 2 not-count (mass to volume)

        if self._fromType == "count" or self._toType == "count":
            # If we know the conversion type for the from unit we can convert to the base unit
            if self._fromType != "count" and self._fromType in knownConversionTypes:
                knownMeasure = [k for k,v in self.knownConversions.items() if v['type'] == self._fromType][0]
                knownFactor = self.knownConversions[knownMeasure]['factor']
                self._fromFactor = knownFactor * measures[self._fromUnit]['factor']

            # If we know the conversion type for the to unit we can convert from the base unit
            if self._toType != "count" and self._toType in knownConversionTypes:
                knownMeasure = [k for k,v in self.knownConversions.items() if v['type'] == self._toType][0]
                knownFactor = self.knownConversions[knownMeasure]['factor']
                self._toFactor = knownFactor * measures[self._toUnit]['factor']

        return value * self._fromFactor / self._toFactor


    
    ################
    # Helper functions
    def __set_missing_units_to_base_unit__(self):
        ''' If the from or to unit is not provided we will assume the base unit for that one.'''
        if self.fromUnit == None:
            self.fromUnit = self.baseUnit
        if self.toUnit == None:
            self.toUnit = self.baseUnit

    def __get_know_conversion_details__(self) -> dict:
        ''' Get the known conversion details for the from and to units '''
        output = {}
        
        for unit, value in self.knownConversions.items():
            # deep copy the dictionary so we don't change the original
            output[unit] = { **measures[unit] }
            output[unit]["factor"] = value        

        return output
