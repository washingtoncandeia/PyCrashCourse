##-------------------------------
# Cap.9 - Classes
# Python Crash Course
# Autor: Washington Candeia
# Faça você mesmo, p.249
# 9.12 - Vários módulos
##-------------------------------

"""Classe Admin como módulo."""

from user import User
from privileges import Privileges

class Admin(User):
    """Cria uma classe-filha de User."""

    def __init__(self, nome, sobrenome, idade):
        # Trazendo da classe-Pai:
        super().__init__(nome, sobrenome, idade)

        # Utilizando a class Privileges como instância
        self.privileges = Privileges()
