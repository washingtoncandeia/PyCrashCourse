##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.263
##----------------------------------
# 10.1 - Aprendendo C

import os
os.chdir('C:\\Users\\Wash Araujo\\Documents\\Pycrash\\pycharm\\cap10\\')

with open('learning_python.txt') as objeto:
    contents = objeto.read().replace('Python', 'C')
    print(contents)



with open('learning_python.txt') as objeto:
    contents = objeto.read()
    print(contents.replace('Python', 'C'))



with open('learning_python.txt') as file_obj:
    lines = file_obj.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
