requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# Funcionando:
for requested in requested_toppings:
    print('Adicionando o ingrediente ' + requested + '.')

# Funcionando:
for requested in requested_toppings:
    if requested == 'mushrooms':
        print('\n\t=== Desculpe, ingrediente ' + requested + ' faltando. ===\n')
    else:
        print('Adicionando o ingrediente ' + requested + '.')


# Erros:
for requested in requested_toppings:
    if 'mushrooms' in requested_toppings:
        print('O ingrediente mushroom está faltando.')
    else:
        print('Adicionando o ingrediente ' + requested + '.')

# Sem erro aparente, mas não totalmente correto.
for requested in requested_toppings:
    print('Adicionando o ingrediente ' + requested + '.')
    
    if 'mushrooms':
        print('Mushrooms está em falta!')