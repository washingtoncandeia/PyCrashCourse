##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 10 - Arquivos
# write_message.py, p.264
##-----------------------------
filename = 'programming.txt'

with open(filename, 'w') as file_obj:
    file_obj.write('I love programming!')

with open(filename, 'r') as obj:
    print(obj.read())
