##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Sub-seção: Analisando textos, p.272
##----------------------------------

import os
os.chdir('C:\\Users\\Wash Araujo\\Documents\\Pycrash\\book_resources\\ehmatthes-pcc-7597c2b\\chapter_10')

filename = 'alice.txt'
# O erro de exceção é criado por open()
# por isso, a instrução try carrega o bloco:
try:
    with open(filename) as f_obj:
        contents = f_obj.read()

# Agora, lidando com a exceção:
except FileNotFoundError:
    print("O arquivo '" + filename + "' não existe ou não está nesse diretório.")
# Usar o else para obter os resultados:
else:
    words = contents.split()
    num_words = len(words)
    print("O arquivo '" + filename + "' possui aproximadamente " + str(num_words) + " palavras.")
    print("O texto está abaixo: \n")
    print(contents)
