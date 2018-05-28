# Exercício 11.3 - Faça voce mesmo, p.303
class Employee():
    """Simula um empregado de uma empresa."""
    
    def __init__(self, first_name, last_name, ann_salary):
        """Atributos do empregado."""
        self.first_name = first_name
        self.last_name = last_name
        self.ann_salary = ann_salary
        
    
    def give_raise(self, increment=5000):
        """Aumento de $5000,00 ao empregado."""
        self.ann_salary += increment
