import unittest
from calculator import calculator

class CalculatorTestCase(unittest.TestCase):
    def test_one(self):
        res = calculator('2+3')
        self.assertEqual(res, 5)
    def test_two(self):
        res = calculator('10/0')
        self.assertEqual(res, 'Некоректные данные')
    def test_three(self):
        res = calculator('abc')
        self.assertEqual(res, 'Некоректные данные')

    def test_four(self):
        res = calculator('2**6')
        self.assertEqual(res, 64)