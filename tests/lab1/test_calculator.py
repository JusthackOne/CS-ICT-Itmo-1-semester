import unittest
from calculator import calculator

class CalculatorTestCase(unittest.TestCase):
    def test_one(self): # Обычная проверка
        res = calculator('2+3')
        self.assertEqual(res, 5)
    def test_two(self): #Проверка деления на ноль
        res = calculator('10/0')
        self.assertEqual(res, 'Некоректные данные')
    def test_three(self): # Проверка на некорректные данные
        res = calculator('abc')
        self.assertEqual(res, 'Некоректные данные')

    def test_four(self): # Обычная проверка
        res = calculator('2**6')
        self.assertEqual(res, 64)