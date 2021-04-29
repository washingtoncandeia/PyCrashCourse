##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# user_profile.py, p.210
##-----------------------------

def build_profile(first, last, **user_info):
    """Constroi um dicionário contendo tudo o que sabemos sobre um usuário."""
    profile = {}

    profile['first'] = first
    profile['last'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

