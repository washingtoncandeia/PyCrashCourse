"""
Washington Candeia
Livro: Curso Intensivo de Python - Eric Matthes
Cap.6 - Dicionários
"""
import os

# Atual path
path = os.getcwd()
print(path)

# Mudar de diretório
os.chdir("C:\\Users\\Wash Araujo\\Documents")
print(os.getcwd())
print(os.listdir())

# Criando diretório para pycrashcourse
novo_diretorio = "pycrash"

# Se ele existir, ok
try:
    os.makedirs(novo_diretorio, exist_ok=True)

# Senão, faça uma exceção, crie um novo
except TypeError:
    if not os.path.isdir(novo_diretorio):
        os.mkdir(novo_diretorio)
# Confirmando
os.listdir()

# Mudando para pycrash/
os.chdir("C:\\Users\\Wash Araujo\\Documents\\pycrash")
os.getcwd()
os.listdir()