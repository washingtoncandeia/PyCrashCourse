#!/bin/env python
# p.164

# Armazenar uma lista de pets
pets = []

# pet 1
animal1 = {
    'tipo': 'cachorro',
    'nome': 'costelinha',
    'amigo': 'doug',
}

pets.append(animal1)

animal2 = {
    'tipo': 'gato',
    'nome': 'garfield',
    'amigo': 'jon arbuckle'
}

pets.append(animal2)

animal3 = {
    'tipo': 'passaro',
    'nome': 'woodstock',
    'amigo': 'snoopy'
}

pets.append(animal3)

for animal in pets:
    print('\nNome: ' + animal['nome'].title())
    nome = animal['nome']
    tipo = animal['tipo']
    amigo = animal['amigo']

    print(nome.title() + ' é um ' + tipo + '. Seu amigo é ' + amigo.title() + '.')