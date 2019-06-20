# lista vazia
requested_toppings = []

if requested_toppings:
    for request in requested_toppings:
        if request == 'green peppers':
            print('Desculpe, green peppers in falta.')
        else:
            print('Adicionando ' + request + '.')
    print('\nSua pizza está pronta!')        
    
else:
    print('Tem certeza de que quer uma pizza?')