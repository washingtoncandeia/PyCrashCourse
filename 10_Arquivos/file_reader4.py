##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# file_reader.py, p.258
##-------------------------------

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)
        