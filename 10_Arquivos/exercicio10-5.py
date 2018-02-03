##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.266 a 267
##----------------------------------

# Escrever laço while, agora com break
while True:
    print("\nDigite 'sair' para encerrar.")
    enquete = input('Por que você gosta de programação? Resposta: ')
    if enquete == 'sair':
        break
    else:
        with open('enquete.txt', 'a') as obj:
            obj.write(enquete + '\n')
