##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 10 - Arquivos
# Faça você mesmo, p.263
##-----------------------------

# 10.2 - Aprendendo C
with open('learning_python.txt') as obj:
    print(obj.read())

with open('learning_python.txt') as obj:
    lines = obj.readlines()

for line in lines:
    print(line.replace('Python', 'C').rstrip())

