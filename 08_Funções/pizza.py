##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# greet_users.py, p.202-203
##-----------------------------

# Número arbitrário de argumentos
def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    for topping in toppings:
        print('- ' + topping)

# Teste
make_pizza('calabresa', 'pepperoni', 'mussarela', 'lombinho')

# Modificando a funççao para aceitar o argumento tamanho
def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print('\nSerá preparada a pizza com o tamanho ' + str(size)
          + ', com os seguintes ingredientes: ')

    for topping in toppings:
        print('- ', topping)

# Uso
make_pizza(16, 'calabresa', 'pepperoni', 'mussarela', 'parmesão')

