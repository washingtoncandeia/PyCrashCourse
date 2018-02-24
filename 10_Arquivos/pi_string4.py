##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# pi_string.py, p.262 - 263
##-------------------------------

filename = 'pi_million_digits.txt'

# Armazenar o conteudo de pi_million_digits.txt em uma lista
# Usar o metodo readlines
with open(filename) as file_object:
    lines = file_object.readlines()

# Usar o conteudo da lista
pi_string = ''
for line in lines:
    # Retirar os espaços em branco a esquerda para unir digitos
    pi_string += line.strip()

# Com input, armazenar o dia do aniversario
birthday = input("Enter your birthday, in the form mmddyy: ")

# Se os digitos inseridos estiverem em pi_string (uma longa string):
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')

else:
    print('Your birthday does not appears in the first million digits of pi.')
