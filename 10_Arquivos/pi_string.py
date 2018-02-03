##----------------------------------
# Cap.10 - Arquivos e Exceções
# Python Crash Course - Eric Matthes
# Autor: Washington Candeia
##----------------------------------
import os
os.chdir('C:\\Users\\Wash Araujo\\Documents\\Pycrash\\book_resources\\ehmatthes-pcc-7597c2b\\chapter_10')

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
