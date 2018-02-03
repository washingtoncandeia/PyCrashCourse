##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.277
# 10.8
##----------------------------------

# Trabalhando com vários arquivos, p.274 - 276
# Armazenar os nomes dos arquivos numa lista:
filenames = ['cats.txt', 'dogs.txt']

# Criar uma função para facilitar o manuseio dos arquivos:
def conteudo_arquivos(filename):
    """Função para mostrar o conteúdo meus arquivos."""

    try:
        with open(filename) as obj:
            conteudo_arquivo = obj.read()

    except FileNotFoundError:
        print("\nO arquivo '" + filename + "' não existe ou não está nesse diretório.")

    else:
        print(conteudo_arquivo)

# Agora, vamos procurar os arquivos e mostrar seus conteúdos:
for file in filenames:
    conteudo_arquivos(file)
