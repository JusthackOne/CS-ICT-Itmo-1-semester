import unittest

from src.lab4.ageGroups import AgeGroups
from unittest.mock import patch

from io import StringIO
import sys


set_ageGroups_test1 = [['100', '123'], ['80', '100'], ['60', '80'], ['45', '60'], ['35', '45'], ['25', '35'], ['18', '25'], ['-1', '18']]
class AgeGroupsTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='18 25 35 45 60 80 100')
    def test_set_ageGroups(self, mock_input):
        ageGroup = AgeGroups()
        ageGroup.set_ageGroups()
        self.assertEqual(ageGroup.ageGroups, set_ageGroups_test1)

    @patch('builtins.input', return_value='100')
    def test_set_ageGroups_2(self, mock_input):
        ageGroup = AgeGroups()
        ageGroup.set_ageGroups()
        self.assertEqual(ageGroup.ageGroups, [['100', '123'], ['-1', '100']])

    def test_set_respondents(self):
        mock_input_values = ['Данил Михаил Олегович,26', 'Дима Михаил Олегович,104', 'Волк Михаил Олегович,18', 'END']  # значения, которые хотим передать через input()
        ageGroup = AgeGroups()

        with unittest.mock.patch('builtins.input', side_effect=mock_input_values):
            ageGroup.set_respondents()

        result = [['Данил Михаил Олегович', '26'], ['Дима Михаил Олегович', '104'], ['Волк Михаил Олегович', '18']]
        self.assertEqual(ageGroup.respondents, result)

    def test_sort_respondents(self):
        ageGroup = AgeGroups()
        ageGroup.ageGroups = [['100', '123'], ['80', '100'], ['60', '80'], ['45', '60'], ['35', '45'], ['25', '35'], ['18', '25'], ['-1', '18']]
        ageGroup.respondents = [['Недиков Михаил Олегович', '18'], ['Берёзов Михаил Олегович', '18'], ['Бима Михаил Олегович', '104'], ['Петя Михаил Олегович', '103'], ['Дима Михаил Олегович', '104']]

        # Сохраняем стандартный вывод
        original_stdout = sys.stdout
        try:
            # Создаем файл-буфер для перехвата вывода
            fake_stdout = StringIO()
            sys.stdout = fake_stdout

            ageGroup.sort_respondents()  # вызываем метод, который использует print() в цикле for

            # Получаем значение из буфера вывода
            printed_output = fake_stdout.getvalue().strip()

            # Проверяем результат вывода
            self.assertEqual(printed_output, '101+: Бима Михаил Олегович (104), Дима Михаил Олегович (104), Петя Михаил Олегович (103)\n0-18: Берёзов Михаил Олегович (18), Недиков Михаил Олегович (18)')
        finally:
            # Восстанавливаем стандартный вывод
            sys.stdout = original_stdout

    def test_sort_respondents_by_age_name(self):
        ageGroup = AgeGroups()
        respodents = [['Недиков Михаил Олегович', '18'], ['Берёзов Михаил Олегович', '18'], ['Бима Михаил Олегович', '104'], ['Петя Михаил Олегович', '103'], ['Дима Михаил Олегович', '104']]
        res = ageGroup.sort_respondents_by_age_name(respodents)
        result = [['Бима Михаил Олегович', '104'], ['Дима Михаил Олегович', '104'], ['Петя Михаил Олегович', '103'], ['Берёзов Михаил Олегович', '18'], ['Недиков Михаил Олегович', '18']]
        self.assertEqual(res, result)

if __name__ == '__main__':
    unittest.main()