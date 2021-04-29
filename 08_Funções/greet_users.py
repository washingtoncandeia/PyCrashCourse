##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# greet_users.py, p.202-203
##-----------------------------

# Passando uma lista para uma função
def greet_users(users):
    """Exibe uma saudação a cada usuário da lista."""
    for user in users:
        print('\nHello, ' + user.title() + '!')

users = ['leia', 'sol', 'jimmi']

greet_users(users)

