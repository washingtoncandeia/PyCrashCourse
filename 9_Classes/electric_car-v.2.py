##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 9 - Classes
# Faça você mesmo, p.232
##-----------------------------


class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        """Atributos"""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, gas):
        """Abastecer o carro com gasolina."""
        if gas >= self.gas_tank:
            self.gas_tank += gas
        else:
            print("You can't fill the gas tank with this.")
        print("This car has " + str(self.gas_tank) + 'L on gas tank.')


class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos de uma bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade de uma bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)


class ElectricCar(Car):
    """Representa aspectos de um carro específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atrubutos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self, gas):
        """Abastecer o carro com gasolina."""
        print("Este carro não precisa de um tanque de gasolina!")
