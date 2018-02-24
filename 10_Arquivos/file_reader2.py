##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# file_reader.py, p.256
##-------------------------------

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
