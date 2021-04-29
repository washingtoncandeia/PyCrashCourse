##-------------------------------
# Cap.9 - Classes
# Python Crash Course
# Autor: Washington Candeia
##-------------------------------

# Faça você mesmo, p.241
# 9.9 - Privileges

class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem o carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        """Descreve o carro de forma elegante."""
        # Poderia-se usar a função print, mas optei por retornar
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """Informa sobre a quilometragem do carro"""
        print("Este carro tem " + str(self.odometer_reading) + "km")

    def update_odometer(self, km):
        """Cria método para fazer update da quilometragem."""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('\n\tVocê não pode baixar a quilometragem do seu carro!')

    def increment_odometer(self, kmters):
        """Incrementa o valor da quilometragem do carro."""
        self.odometer_reading += kmters
        print('\nA quilometragem passou a ser: ' + str(self.odometer_reading))

    def fill_gas_tank(self, fill):
        """Enche o tanque do carro com o que você informou."""
        self.gas_tank += fill
        print('Seu carro tem ' + str(self.gas_tank) + 'L no tanque.')


class Battery():
    """Cria uma classe que contém as informações acerca da bateria do carro."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Informa como está a situação da bateria."""
        print('Este carro tem uma bateria de ' + str(self.battery_size) + '-kWh.')

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro consegue percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'Este carro pode andar, aproximadamente, ' + str(range)
        message += ' quilômetros sem abastecer.'
        print(message)

    def upgrade_battery(self):
        """Método verifica a capacidade da bateria e define-a para 85 se o valor for diferente."""
        if self.battery_size != 85:
            self.battery_size = 85
        else:
            print('\tA capacidade da bateria é 85-kWh.')


class ElectricCar(Car):
    """Cria uma classe que representa um carro elétrico."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # Utiliza atributos da classe Pai.
        self.battery = Battery()             # Instância Battery como atributo.

    def fill_gas_tank(self, fill):
        """Carros elétricos não têm tanques de gasolina."""
        print('Carros elétricos não têm tanques de gasolina.')

# Instancia carro_eletrico
carro_eletrico = ElectricCar('atom', 'lsd', 2048)
carro_eletrico.battery.describe_battery()
carro_eletrico.fill_gas_tank(100)
carro_eletrico.battery.get_range()

# Usando novo método para fazer upgrade:
carro_eletrico.battery.upgrade_battery()
carro_eletrico.battery.get_range()