##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 9 - Classes
# Faça você mesmo, p.225-226
##-----------------------------

# 9.1 - Restaurante
class Restaurant():
    """Simula um restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa atributos do restaurante, como seu nome e especialidade na cozinha."""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Método para descrever o restaurante, com seu nome e especialidade na cozinha."""
        print('\nO nome do restaurante é ' + self.restaurant_name.title() + '.')
        print('Sua especialidade é cozinha ' + self.cuisine_type + '.')

    def open_restaurant(self):
        """Métodos de boas vindas ao restaurante."""
        print('\nSeja bem vindo! O restaurante ' + self.restaurant_name.title() + ' está aberto.')

# Instância
restaurante = Restaurant('roma', 'italiana')

restaurante.open_restaurant()
restaurante.describe_restaurant()

# 9.2 - Três Restaurantes
# Apenas demonstrar como criar instâncias
rest1 = Restaurant('panela de barro', 'mineira')
rest2 = Restaurant('o sertanejo', 'do nordeste')
rest3 = Restaurant('beira-rio', 'matogrossense')

rest1.open_restaurant()
rest1.describe_restaurant()

rest2.open_restaurant()
rest2.describe_restaurant()

rest3.open_restaurant()
rest3.describe_restaurant()

# 9.3 - Usuários
class User():
    """Simula a descrição de usuários."""

    def __init__(self, first_name, last_name, age, work):
        """Inicializa os atributos da classe."""

        self.first_name = first_name
        self.last_name =  last_name
        self.age = age
        self.work = work

    def greet_user(self):
        """Método para saudar o usuário."""
        print('\nOlá, ' + self.first_name.title() + '! Seja bem vindo!')

    def describe_user(self):
        """Um método que exibe um resumo das informações do usuário."""

        print('\nO nome do usuário(a) é ' + self.first_name.title() + '.')
        print('Seu sobrenome é ' + self.last_name.title() + '.')
        print('Sua idade é de ' + str(self.age) + ' anos.')
        print('Sua profissão: ' + self.work.title())

# Instância
wash = User('Washington', 'Araujo', 34, 'biólogo')
wash.greet_user()
wash.describe_user()
