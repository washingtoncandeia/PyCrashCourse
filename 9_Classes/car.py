##-----------------------------
# Pycrash Course
# Eric Matthes
# Cap. 9 - Classes
# classe Car, p.226-232
##-----------------------------

class Car():
    """Uma tentativa simples de simular um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

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
