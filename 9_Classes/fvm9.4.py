##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 9 - Classes
# Faça você mesmo, p.232
##-----------------------------

# 9.4 - Pessoas atendidas
##--> 9.1 - Restaurante
class Restaurant():
    """Cria uma classe que simula um restaurante."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa atributos da classe."""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Descreve o restaurante, através de seu nome e especialidade na cozinha."""
        print('\nO nome do restaurante é ' + self.restaurant_name.title() + '.')
        print('Sua especialidade é cozinha ' + self.cuisine_type + '.')

    def open_restaurant(self):
        """Boas vindas do restaurante."""
        print('\nSejam bem vindos! O restaurante ' + self.restaurant_name.title() + ' está aberto.')

    def set_number_served(self, served):
        """Modifica o número relativo às pessoas servidas."""

        if served >= self.number_served:
            self.number_served = served

        else:
            print('\n\tNão é possível ter servido esse número de pessoas!')

    def increment_number_served(self, number):
        """Incrementa o número de pessoas servidas a medida em que servem-se refeições."""
        self.number_served += number

# Cont.
# Instancia
restaurante = Restaurant('roma', 'italiana')

restaurante.number_served = 25
print(restaurante.number_served)

# Usando métodos
# 1. Método que apenas modifica o número
restaurante.set_number_served(25)

print(restaurante.number_served)

# 2. Método que incrementa o número
restaurante.increment_number_served(25)

print(restaurante.number_served)

# 9.5 - Tentativa de login
##--> 9.3 - Usuários
class User():
    """Simula a descrição de usuários."""

    def __init__(self, first_name, last_name, age, work):
        """Inicializa os atributos da classe."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.work = work
        self.login_attempts = 0

    def describe_user(self):
        """Um método que exibe um resumo das informações do usuário."""

        print('\nO nome do usuário(a) é ' + self.first_name.title() + '.')
        print('Seu sobrenome é ' + self.last_name.title() + '.')
        print('Sua idade é de ' + str(self.age) + ' anos.')
        print('Sua profissão: ' + self.work.title())

    def greet_user(self):
        """Método para saudar o usuário."""
        print('\nOlá, ' + self.first_name.title() + '! Seja bem vindo!')

    def increment_login_attempts(self, attempts):
        """Incrementa a contagem de tentativas de login."""
        self.login_attempts += attempts
        print('Tentativas de login: ' + str(self.login_attempts))

    def reset_login_attempts(self):
        """Reseta a contagem de tentativas de login"""
        self.login_attempts = 0
        print('\nAtenção! Contagem de tentativas de login resetadas.')

usuario = User('washington', 'araujo', 34, 'biólogo')
usuario.increment_login_attempts(50)
usuario.increment_login_attempts(5)
usuario.reset_login_attempts()
print(usuario.login_attempts)
