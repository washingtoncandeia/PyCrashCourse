##-------------------------------
# Cap.9 - Classes
# Python Crash Course
# Autor: Washington Candeia
##-------------------------------

# Faça você mesmo, p.241
# 9.6 - Sorveteria

class Restaurant():
    """Cria uma classe que modela um restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """Atributos que descrevem o restaurante."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Descrição do restaurante."""
        print('O nome do restaurante é ' + self.restaurant_name.title() + '.')
        print('Este restaurante é especializado em cozinha ' + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        """Avisa que o restaurante está aberto."""
        print('O restaurante está aberto!')


class IceCreamStand(Restaurant):
    """Cria uma classe filha de Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = lista_sorvetes = [
            'baunilha', 'chocolate', 'morango', 'chocolate amargo',
            'pistache', 'nata-goiaba', 'café', 'sonho-de-valsa',
            'prestígio', 'limão', 'passas', 'cajá', 'menta']

    def ice_cream_flavors(self):
        """Descreve os sabores de sorvetes."""
        print('\n\tOs sabores de sorvete disponíveis são:')
        for i in self.flavors:
            print('-> ' + i.title())


sorveteria = IceCreamStand('pão-de-mel', 'sorvetes')
sorveteria.describe_restaurant()
sorveteria.open_restaurant()
sorveteria.ice_cream_flavors()