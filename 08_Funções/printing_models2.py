##---------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# printing_models.py, p.203
##-----------------------------

def print_models(unprinted_designs, complete_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para complete_models após a impressão.
    :param unprinted_designs: lista de objetos e/ou tipos de design.
    :param complete_models: lista vazia, que receberá os objetos e/ou tipos de design feitos.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simula a criação de uma impressão 3D a partir do design
        print('\nPrinting model: ' + current_design)
        complete_models.append(current_design)

def show_completed_models(complete_models):
    """Mostra todos os modelos impressos."""
    print('\nThe following models have been printed: ')
    for completed_model in complete_models:
        print(completed_model)


unprint = ['casaco', 'taco', 'bola']
complete = []

print_models(unprint, complete)
show_completed_models(complete)