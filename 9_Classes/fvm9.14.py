##-------------------------------
# Cap.9 - Classes
# Python Crash Course
# Autor: Washington Candeia
# Faça você mesmo, p.251
# 9.14 - Dados
##-------------------------------

from random import randint

class Die():
    """Cria uma classe que modela um dado (objeto) do mundo real."""
    def __init__(self, sides):
        """Atributo que representa os 6 lados de um dado."""
        self.sides = sides

    def roll_die(self):
        """Método que exibeum número aleatório entre 1 e o valor final."""
        lançar = randint(1, self.sides)
        print(lançar)

dado = Die(20)
dado.roll_die()
