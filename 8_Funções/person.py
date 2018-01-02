##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# person.py, p.199
##-----------------------------

# Devolvendo uum dicionário
def build_person(first_name, last_name):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

eu = build_person('washington', 'araujo', age=34)
print(eu)