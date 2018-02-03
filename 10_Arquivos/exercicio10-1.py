##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.263
##----------------------------------

import os
os.chdir('C:\\Users\\Wash Araujo\\Documents\\Pycrash\\pycharm\\cap10\\')
# A - Ler o arquivo completo:
with open('learning_python.txt') as objeto:
    contents = objeto.read()
    print(contents)

# B - Usar for loop:
with open('learning_python.txt') as fileobjeto:
    for line in fileobjeto:
        print(line.rstrip())


# C - Armazenar linhas numa lista para usá-las fora do bloco with:
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

# Usando lines
for line in lines:
    print(line.rstrip())
