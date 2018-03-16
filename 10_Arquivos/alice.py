##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Eric Matthes
# Autor: Washington Candeia
# division.py, p.270
##-------------------------------

filename = 'alice.txt'

# Leitura do arquivo
try:
    with open(filename) as file_obj:
        contents = file_obj.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    print(contents)

