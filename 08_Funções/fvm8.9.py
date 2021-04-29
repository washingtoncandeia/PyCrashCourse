##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# Faça você mesmo, p.207
##-----------------------------

# 8.9 - Magicos
magicos = ['david blaine', 'houdini', 'chris angel', 'david copperfield']

def show_magicians(magicians):
    """Exibe o nome de mágicos em uma lista."""
    for magico in magicians:
        print(magico.title())

show_magicians(magicos)

# 8.10 - Grandes mágicos
def make_great(magicians):
    """Modifica a lista de mágicos, adicionando 'O Grande' no início."""
    temp_magic = []

    while magicians:
        magician = magicians.pop()
        temp_magic.append('O grande ' + magician)

    for magician in temp_magic:
        magicians.append(magician)

make_great(magicos)
show_magicians(magicos)

# 8.11 - Mágicos inalterados
def make_great(magicians):
    "Exibe o nome dos mágicos, adicionando 'O Grande' no início."
    temp_magic = []

    while magicians:
        magician = magicians.pop()
        temp_magic.append('O Grande ' + magician.title())

    for magician in temp_magic:
        magicians.append(magician)

    return magicians

print('\nOs mágicos inalterados: ')
magicos2 = ['magico um', 'magico dois', 'magico tres']

mag_inalterado = make_great(magicos2[:])
show_magicians(mag_inalterado)

print('\nOs mágicos2 originais: ')
show_magicians(magicos2)
