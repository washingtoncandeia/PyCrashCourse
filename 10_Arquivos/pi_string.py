##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 10 - Arquivos
# pi_string.py, p.260
##-----------------------------

# path = "C:\\Users\\Wash Araujo\\Documents\\Pycrash\\book_resources\\ehmatthes-pcc\\chapter_10\\"
filename = "pi_million_digits.txt"

with open(filename) as file_obj:
    lines = file_obj.readlines()

# 1. Criar uma variável para armazenar os dígitos contidos no arquivo
#    Deve estar fora do loop, pois ao reiniciá-lo, Python adiciona-o ao próximo dígito
pi_string = ''

# 2. Agora iniciar o loop contendo as linhas de dígitos a serem adicionadas a pi_string
#    Remover o caractere de quebra de linha com o método strip para remover do lado esquerdo
for line in lines:
    pi_string += line.strip()

# 3. Exibir pi_string
print(pi_string[:52] + '...')

# 4. Mostrar o tamanho de pi_string
print(len(pi_string))
