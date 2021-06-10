# Dicionários
# 09 de junho de 2021

# Usando if no início:
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f'\nAs linguagens favorita de {name.title()} são:')
        for language in languages:
            print(f'\t- {language.title()}')
    elif len(languages) == 1:
        for lang in languages:
            print(f'\nA linguagem favorita de {name.title()} é {lang.title()}.')
    else:
        pass
