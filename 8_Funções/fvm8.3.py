##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# pets.py, p.195
##-----------------------------

# 8.3. Camiseta
def make_shirt(tam, msg):
    """Função para estampar uma camiseta."""
    print('\nO tamanho da camiseta é ' + tam.title() + '.')
    print('Sua mensagem deve ser: ' + msg.title() + '.')

make_shirt('m', "be happy!")

# 8.4. Camisetas grandes:
def make_shirt(tam='g', msg='eu amo python!'):
    """Função para estampar uma camiseta."""
    print('\nO tamanho da camiseta é ' + tam.title() + '.')
    print('Sua mensagem deve ser: ' + msg.title() + '.')

make_shirt()

# 8.5. Cidades
def describe_city(cidade='natal', pais='brasil'):
    """Exibe o nome de uma cidade e seu país."""
    print('\nO nome da cidade onde resido é ' + cidade.title() + '.')
    print('Essa cidade pertence ao ' + pais.title() + '.')

describe_city()
describe_city(cidade='acapulco', pais='méxico')
