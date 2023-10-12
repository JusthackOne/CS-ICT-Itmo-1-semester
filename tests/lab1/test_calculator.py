import unittest
from calculator import calculator

class CalculatorTestCase(unittest.TestCase):
    def test_one(self):
        res = calculator('2+3')
        self.assertEquals(res, 5)
    def test_two(self):
        res = calculator('10/0')
        self.assertEquals(res, 'Некоректные данные')
    def test_three(self):
        res = calculator('abc')
        self.assertEquals(res, 'Некоректные данные')

    def test_four(self):
        res = calculator('2**6')
        self.assertEquals(res, 64)