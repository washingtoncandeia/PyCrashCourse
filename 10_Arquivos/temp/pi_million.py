import os

os.chdir('C:\\Users\\Wash Araujo\\Documents\\Pycrash\\book_resources\\ehmatthes-pcc-7597c2b\\chapter_10')
#filename = 'C:\\Users\\Wash Araujo\\Documents\\Pycrash\\book_resources\\ehmatthes-pcc-7597c2b\\chapter_10\\pi_million_digits.txt'

with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

    pi_digits = ''
    for line in lines:
        pi_digits += line.strip()

print(pi_digits[:52] + '...')
print(len(pi_digits))
