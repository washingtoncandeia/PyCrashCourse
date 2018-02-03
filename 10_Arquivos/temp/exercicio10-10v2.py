##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.277
# 10.10 - Palavras comuns
##----------------------------------
# Contar palavras nos textos baixados utilizando o método .count()

filenames = [
    'on_the_origin_of_species.txt',
    'descent_of_men.txt',
    'watson_evolution.txt'
]
# Lendo todos os arquivos:
for file in filenames:
    try:
        with open(file) as obj:
            contents = obj.read()

    except FileNotFoundError:
        print("O arquivo '" + file + "' não existe ou não está nesse diretório.")

    else:
        file_word_content = contents.lower().count('evolution')
        print("O arquivo '" + file + "' apresenta a essa palavra " + str(file_word_content) + " vezes.")
