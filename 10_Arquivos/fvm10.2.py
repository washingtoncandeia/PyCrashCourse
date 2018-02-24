##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Autor do livro: Eric Matthes
# Autor: Washington Candeia
# Faça você mesmo, p.263
##------------------------------

# 10.2 - Aprendendo C

# Forma 1
with open('learning_python.txt') as obj:
    conteudo = obj.read()
    print(conteudo.replace('Python', 'C'))



# Forma 2
with open('learning_python.txt') as obj:
    conteudo = obj.read().replace('Python', 'C')
    print(conteudo)



# Forma 3
with open('learning_python.txt') as obj:
    lista = obj.readlines()

# Fora do bloco
for l in lista:
    print(l.rstrip().replace('Python', 'C'))



# Forma 4
with open('learning_python.txt') as file_obj:
    lines = file_obj.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
