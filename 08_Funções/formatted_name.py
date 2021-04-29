##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# formatted_name.py, p.197-198
##-----------------------------

# Valores de retorno
def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de mode elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Teste
eu = get_formatted_name('washington', 'araujo')
print(eu)

# Argumento opcional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
eu2 = get_formatted_name('Washington', 'araujo', middle_name='candeia')
print(eu2)

# Argumento opcional com escolha lógica
def get_formatted_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

eu3 = get_formatted_name('washington', 'araujo', middle_name='candeia')
print(eu3)
