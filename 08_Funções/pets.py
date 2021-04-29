##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# pets.py, p.188
##-----------------------------

# Argumentos posicionais
def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print('\nEu tenho um ' + animal_type + '.')
    print('Meu ' + animal_type + ' se chama ' + pet_name.title() + '.')

# Chamada de função com argumentos posicionais
describe_pet('cachorro', 'leia')

# Argumentos nomeados (keyword arguments)
describe_pet(animal_type="cachorra", pet_name="leia")

# Valores default
def describe_pet(pet_name, animal_type="cachorro(a)"):
    """Exibe informações sobre um animal de estimação"""
    print('\nEu tenho um ' + animal_type + '.')
    print('Meu ' + animal_type + ' se chama ' + pet_name.title() + '.')

describe_pet('leia')