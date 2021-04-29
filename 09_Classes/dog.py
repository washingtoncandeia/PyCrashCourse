##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 9 - Classes
# dog.py, p.221
##-----------------------------

# Classe Dog
class Dog():
    """Uma tentativa simples de modelar um cachorro."""
    def __init__(self, name, age):
        """Inicializa os atributos da classe."""
        self.name = name
        self.age = age


    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title() + ' rolled over!')


my_dog = Dog('jimi', 5)

my_dog.sit()
my_dog.roll_over()
