##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# p.272
##----------------------------------

filename = 'alice.txt'
# Usando instrução try em arquivos
try:
    with open(filename) as f_object:
        contents = f_object.read()
except FileNotFoundError:
    print("O arquivo '" + filename + "' não existe ou não está neste diretório.")

