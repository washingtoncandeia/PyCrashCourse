##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.277
# 10.9 - Gatos e cachorros silenciosos
##----------------------------------

# Esse é só uma modificação do exercício 10.8

arquivos = ['cats.txt', 'dogs.txt']

for file in arquivos:
    try:
        with open(file) as obj:
            conteudo_arquivo = obj.read()
            print(conteudo_arquivo)

    except FileNotFoundError:
        pass
    