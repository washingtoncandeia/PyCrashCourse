##---------------------
# Cap5 - Instruções If
# toppings.py, p.133
##---------------------

# Lista de ingredientes
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# Laço for, incluindo ingrediente faltante
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')
