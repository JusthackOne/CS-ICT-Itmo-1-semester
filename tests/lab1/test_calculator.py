import unittest
from
class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_one(self)
        res = calculator('2+3')
        self.assertEquals(res, 5)