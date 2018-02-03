##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
##----------------------------------
filename = 'pi_digits.txt'

# Trabalhando com o conteúdo de um arquivo
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

    print(pi_string)
    print(len(pi_string))
