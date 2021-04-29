# p.152
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name, language in favorite_languages.items():
    print('\nA linguagem de ' + name.title() + ' é ' + language.title() + '.')

    if name in friends:
        print('Olá, ' + name.title() + ', como vai voce?')