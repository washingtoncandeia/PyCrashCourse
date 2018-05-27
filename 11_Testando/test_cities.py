#!/usr/bin/env python
import unittest
from cities import city_country

class CityCountryTest(unittest.TestCase):
    """Classe para testar 'cities.py'."""
   
    def test_city_country(self):
        """A saída é 'Cairo Egito'?"""
        location = city_country('cairo', 'egito')
        self.assertEqual(location, 'Cairo Egito')
    
unittest.main()        
        