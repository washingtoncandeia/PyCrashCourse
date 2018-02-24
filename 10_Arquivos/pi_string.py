##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# pi_string.py, p.260
##-------------------------------

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# Trabalhando fora do bloco with
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
