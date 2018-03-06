##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 10 - Arquivos
# Faça você mesmo, p.263
##-----------------------------

#10.1 - Aprendendo Python
# 1. Conteúdo inteiro
with open('learning_python.txt') as obj:
    print(obj.read())

# 2. Em laço
with open('learning_python.txt') as obj:
    for line in obj:
        print(line.rstrip())

# 3. Armazenando linhas em uma lista e trabalhando fora do bloco
with open('learning_python.txt') as obj:
    lines = obj.readlines()

# Trabalhando fora do bloco with
for line in lines:
    print(line.rstrip())
