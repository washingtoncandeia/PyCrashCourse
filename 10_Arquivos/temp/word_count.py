##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# p.274 a 276
##----------------------------------

def count_words(filename):
    """Conta o número aproximado de palavras de um arquivo."""

    try:
        with open(filename) as f_ojb:
            contents = f_ojb.read()

    except FileNotFoundError:
        print("O arquivo '" + filename + "' não existe ou não está nesse diretório.")
        #pass

    else:
        words = contents.split()
        num_words = len(words)
        print("O arquivo '" + filename + "' tem " + str(num_words) + " palavras.")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    count_words(filename)

