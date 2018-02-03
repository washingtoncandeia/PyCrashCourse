##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.266 a 267
##----------------------------------

nome_usuario = input('Qual o seu nome? Digite aqui: ')

with open('usuario.txt', 'w') as objeto:
    objeto.write(nome_usuario)
