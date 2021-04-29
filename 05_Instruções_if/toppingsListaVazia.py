##---------------------
# Cap5 - Instruções If
# toppings.py, p.134
##---------------------

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('Desculpe, não temos green peppers.')
        else:
            print('Adicionando ' + requested_topping + '.')

# Lista vazia
print('Lista vazia: ')

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinihed make your pizza.')

else:
    print('Are you sure you want a plain pizza?')