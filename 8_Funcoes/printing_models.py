##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# printing_models.py, p.203
##-----------------------------

# Modificando uma lista em uma função
# Começa com alguns designs que devem ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design até que não haja nenhum
# Transfere cada design para completed_models após a impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simula a criação de uma impressão 3D a partir do design
    print('Printing model: ' + current_design)
    completed_models.append(current_design)

# Exibe todos os modelos finalizados
print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model)


