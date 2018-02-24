##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# pi_string.py, p.261
##-------------------------------

filename = 'pi_30_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


# Trabalhando fora do bloco with
pi_string = ''
for line in lines:
    # Usando strip para retirar espaço a esquerda:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
