import unittest

from src.lab4.recomendation import Recomendation
from unittest.mock import patch

from io import StringIO
import sys


set_ageGroups_test1 = [['100', '123'], ['80', '100'], ['60', '80'], ['45', '60'], ['35', '45'], ['25', '35'], ['18', '25'], ['-1', '18']]
class RecomendationTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='1,2')
    def test_get_user_history(self, mock_input):
        recomendation = Recomendation()
        history = recomendation.get_user_history()
        self.assertEqual(history, {'1', '2'})

    def test_get_recomendation_history_users(self):
        recomendation = Recomendation()
        history = {'1', '2'}
        history = recomendation.get_recomendation_history_users(history)
        self.assertEqual(history, [['3', '5', '6', 1.0], ['3', '4', 0.5], ['3', 0.5], ['3', '4', 1.0]])

    def test_get_recomendation_list(self):
        recomendation = Recomendation()
        recomendationHistories = [['3', '5', '6', 1.0], ['3', '4', 0.5], ['3', 0.5], ['3', '4', 1.0]]
        recomendationList = recomendation.get_recomendation_list(recomendationHistories)
        self.assertEqual(recomendationList, {'3': 0.25, '5': 1.0, '6': 1.0, '4': 0.5})

    def test_get_recomendation_film_id(self):
        recomendation = Recomendation()
        recomendationList = {'3': 0.25, '5': 1.0, '6': 1.0, '4': 0.5}
        recomendationFilmId = recomendation.get_recomendation_film_id(recomendationList)
        self.assertEqual(recomendationFilmId, '4')

    def test_get_recomendation_film_name(self):
        recomendation = Recomendation()
        recomendationFilmId = '4'
        film = recomendation.get_recomendation_film_name(recomendationFilmId)
        self.assertEqual(film, 'Унесенные призраками')

if __name__ == '__main__':
    unittest.main()