##-------------------------------
# Cap.9 - Classes
# Python Crash Course
# Autor: Washington Candeia
# Faça você mesmo, p.251
# 9.13 - Reescrevendo o programa com OrderedDict
##-------------------------------

from collections import OrderedDict

glossario = OrderedDict()

glossario['instanciar'] = 'atribuir comportamento e características de uma classe a um objeto'
glossario['oop'] = 'programação orientada a objetos'
glossario['dicionário'] = 'estrutura de dados chave-valor em python'
glossario['módulo'] = 'arquivo contendo funções e classes'
glossario['classe'] = 'oop; estrutura que guarda comportamentos e características de um objeto real'

for k, v in glossario.items():
    print('Palavra e sifnificado: \n'
          + k.title() + ': ' + v.title() + '\n')

