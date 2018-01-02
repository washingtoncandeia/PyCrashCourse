##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# greeter.py, p.200
##-----------------------------

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nPor favor, diga-me seu nome:')
    print("(digite 'q' para sair)")

    f_name = input('Primeiro nome: ')
    if f_name == 'q':
        break

    l_name = input('Sobrenome: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nOlá, ' + formatted_name.title() + '!')