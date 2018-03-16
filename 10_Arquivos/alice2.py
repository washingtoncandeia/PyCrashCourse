##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Eric Matthes
# Autor: Washington Candeia
# division.py, p.273
##-------------------------------
filename = 'alice.txt'

try:
    with open(filename) as file_obj:
        contents = file_obj.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

else:
    # Conta o número aproximado de palavras no arquivo
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

