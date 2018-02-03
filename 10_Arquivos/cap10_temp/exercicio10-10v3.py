##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.277
# 10.10 - Palavras comuns, v3
##----------------------------------

def count_file_words(filenames, *words):
    """
    Conta o número de palavras em cada arquivo, cujo nome está designado numa lista Python.
    Cada palavra é passada a uma tupla, como argumento arbitrário.
    """
    for file in filenames:
        for word in words:
            try:
                with open(file) as obj:
                    contents = obj.read()

            except FileNotFoundError:
                print("O arquivo " + file + "' não existe ou não está nesse diretório.")

            else:
                nums_word = contents.lower().count(word)
                print("O arquivo '" + file + "' apresenta a palavra '" + word + "' "
                      + str(nums_word) + " vezes em seu texto.")

filenames = [
    'on_the_origin_of_species.txt',
    'descent_of_men.txt',
    'watson_evolution.txt'
]

# Usando a função:
count_file_words(filenames, 'evolution', 'it')