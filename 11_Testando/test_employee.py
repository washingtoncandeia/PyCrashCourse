# Exercício 11.3 - Faça voce mesmo, .303
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Classe de testes para 'employee.py'"""
    def setUp(self):
        """Cria um objeto de instancia para todos os métodos."""
        
        self.employee = Employee('donald', 'duck', 60000)
        
        
    def test_give_default_raise(self):
        """Teste para funçao give_raise com valor default."""
        self.employee.give_raise()
        self.assertEqual(self.employee.ann_salary, 65000)
        
    def test_give_custom_raise(self):
        """Teste para funçao give_raise com valor adicionado."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.ann_salary, 70000)
        
unittest.main()

