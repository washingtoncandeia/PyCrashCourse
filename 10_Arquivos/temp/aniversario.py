import os
os.chdir('C:\\Users\\Wash Araujo\\Documents\\Pycrash\\book_resources\\ehmatthes-pcc-7597c2b\\chapter_10')

with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input('Digite sua data de nascimento, na forma mmddaa:')
if birthday in pi_string:
    print('Sua data de nascimento aparece no primeiro milhão de dígitos de pi!')
else:
    print('Sua data de nascimento não aparece no primeiro milhão de dígitos de pi.')
