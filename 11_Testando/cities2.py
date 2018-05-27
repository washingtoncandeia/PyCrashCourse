#!/usr/bin/env python

# Exercicio 11.2
def city_country(city, country, population=''):
    """Cria uma funçao que exibe o nome de uma cidade e seu país."""
    if population:
        location = city.title() + ', ' + country.title() + ' - população ' + str(population)
    else:
        location = city.title() + ' ' + country.title()
        
    return location

cidade = city_country('cairo', 'egito', population=19500000)
print(cidade)
