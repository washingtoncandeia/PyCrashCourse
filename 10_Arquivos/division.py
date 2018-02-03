##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# p.270
##----------------------------------

print('Dê-me dois números e eu os dividirei para você.')
print("(Digite 'sair' para encerrar).")

# Iniciando laço while
while True:
    first_number = input('\nDigite o primeiro número: ')
    if first_number == 'sair':
        break
    second_number = input('Digite o segundo número: ')
    if second_number == 'sair':
        break
    # Iniciar bloco de instrução Try
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Você não pode dividir um número por zero!')
    else:
        print(answer)
