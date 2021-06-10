bandas = [
    'kyuss', 'yawning man', 'desert sessions',
    'brant bjork', 'vista chino', 'fu manchu',
    'sleep', 'nebula', 'john garcia', 'hermano'
]

lista_play = []

for name in bandas:
    new_play = {name.title():'stoner'.title()}
    lista_play.append(new_play)

# Teste
for band in lista_play:
    print(band)
