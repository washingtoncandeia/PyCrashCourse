##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.277
# 10.6 e 10.7
##----------------------------------

# 10-6 - Adição
# 10-7 - Calculadora para adição
while True:
    print('\nDê-me dois números para eu somar!')
    print("(Digite 'sair' para encerrar.)")
    num1 = input('Número 1: ')
    if num1 == 'sair':
        break
    num2 = input('Número 2: ')
    if num2 == 'sair':
        break

    try:
        soma = int(num1) + int(num2)
    except ValueError:
        print('Opa... Parece que você não digitou um número inválido. Por favor, digite um número.')
    else:
        print('O valor da soma é ' + str(soma) + '.')
