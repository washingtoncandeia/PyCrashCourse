##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.266 a 267
##----------------------------------
flag = True
while flag:
    usuario = input("Ola, qual o seu nome? (Digite 'sair' para terminar). Digite:")
    if usuario == 'sair':
        flag = False
    else:
        print("Olá, " + usuario.title() + "! Saudações!")
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(usuario + '\n')
