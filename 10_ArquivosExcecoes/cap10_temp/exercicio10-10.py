##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.277
# 10.10 - Palavras comuns
##----------------------------------
# Contar palavras nos textos baixados utilizando o método .count()
filename = 'on_the_origin_of_species.txt'

try:
    with open(filename) as obj:
        contents = obj.read()


except FileNotFoundError:
    print("O arquivo '" + filename + "' não existe ou não está nesse diretório.")

else:
    contagem = contents.lower().count('evolution')
    print("A palavra aparece " + str(contagem) + " vezes no texto.")
