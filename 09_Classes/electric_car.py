##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 9 - Classes
# Faça você mesmo, p.232
##-----------------------------

# Heranca

class Car():
    """Uma tentativa simples de simular um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        """Descreve o carro."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print('\nA milhagem do carro é de ' + str(self.odometer_reading) + ' -milhas.')

    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com o valor especificado."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('\Você não pode mudar a milhagem abaixo de zero.')

    def increment_odometer(self, miles):
        """Incrementa a milhagem do carro."""
        self.odometer_reading += miles

    def fill_gas_tank(self, gas):
        """Abastecer o carro com gasolina."""
        if gas >= self.gas_tank:
            self.gas_tank += gas
        else:
            print("Não se pode abastecer com esse volume de gasolina.")

        print('Este carro possui ' + str(self.gas_tank) + 'L de gasolina no tanque.')


class ElectricCar(Car):
    """Representa aspectos de um carro específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atrubutos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade de uma bateria."""
        print('Este carro tem uma bateria com ' + str(self.battery_size) + '-kWh de capacidade.')

    def fill_gas_tank(self, gas):
        """Abastecer o carro com gasolina."""
        print("Este carro não precisa de um tanque de gasolina!")

# Aplicando
# Carro eletrico
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank(50)

# Carro
carro = Car('agile', 'tlz', 2011)
print(carro.get_descriptive_name())
carro.fill_gas_tank(50)
