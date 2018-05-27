#!/usr/bin/env python
# Exercicio 11.2

import unittest
from cities2 import city_country

class CityCountryTest(unittest.TestCase):
    """Classe para testar 'Cairo, Egito - população 19500000'"""
    
    def test_city_country_population(self):
        """A saída é 'Cairo, Egito - população 19500000'?"""
        location = city_country('cairo', 'egito', population=19500000)
        self.assertEqual(location, 'Cairo, Egito - população 19500000')
    
unittest.main()
