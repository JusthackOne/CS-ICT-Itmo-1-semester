import unittest

import src.lab3.sudoku as sudoku
import random, string

class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        res = sudoku.group([1,2,3,4], 2)
        self.assertEqual(res, [[1, 2], [3, 4]])

        res = sudoku.group([1,2,3,4,5,6,7,8,9], 3)
        self.assertEqual(res, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    def test_get_row(self):
        res = sudoku.get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
        self.assertEqual(res, ['1', '2', '.'])

        res = sudoku.get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
        self.assertEqual(res, ['4', '.', '6'])

        res = sudoku.get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
        self.assertEqual(res, ['.', '8', '9'])

    def test_get_col(self):
        res = sudoku.get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
        self.assertEqual(res, ['1', '4', '7'])

        res = sudoku.get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
        self.assertEqual(res, ['2', '.', '8'])

        res = sudoku.get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
        self.assertEqual(res, ['3', '6', '9'])



   