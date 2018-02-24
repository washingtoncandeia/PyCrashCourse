##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# pi_string.py, p.262
##-------------------------------

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))
