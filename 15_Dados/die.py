from random import randint

class Die():
    """Uma classe que simula um dado de seis lados."""
    
    def __init__(self, num_sides=6):
        """Supõe um dado de seis lados."""
        self.num_sides = num_sides
        
    def roll(self):
        """"Retorna um valor entre 1 e o número de lados."""
        return randint(1, self.num_sides)
