##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.263
##------------------------------

# 10.1 - Aprendendo Python
# 1. Ler o arquivo inteiro
with open('learning_python.txt') as obj:
    conteudo = obj.read()
    print(conteudo.rstrip())


# 2. Percorrer o objeto em laço
with open('learning_python.txt') as obj:
    for linha in obj:
        print(linha.rstrip())


# 3. Armazenar em uma lista
with open('learning_python.txt') as obj:
    lista = obj.readlines()

# Fora do bloco with
for l in lista:
    print(l.rstrip())
