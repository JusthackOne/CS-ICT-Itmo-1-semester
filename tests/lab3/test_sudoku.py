import unittest

import src.lab3.sudoku as sudoku
import random, string

grid1 = [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

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


    def test_get_block(self):
        res = sudoku.get_block(grid1, (0, 1))
        self.assertEqual(res, ['5', '3', '.', '6', '.', '.', '.', '9', '8'])

        res = sudoku.get_block(grid1, (4, 7))
        self.assertEqual(res, ['.', '.', '3', '.', '.', '1', '.', '.', '6'])

        res = sudoku.get_block(grid1, (8, 8))
        self.assertEqual(res, ['2', '8', '.', '.', '.', '5', '.', '7', '9'])


    def test_find_empty_positions(self):
        res = sudoku.find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
        self.assertEqual(res, (0, 2))

        res = sudoku.find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
        self.assertEqual(res, (1, 1))

        res = sudoku.find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
        self.assertEqual(res, (2, 0))


    def test_find_possible_values(self):
        res = sudoku.find_possible_values(grid1, (0,2))
        self.assertEqual(set(res), {'1', '2', '4'})

        res = sudoku.find_possible_values(grid1, (4,7))
        self.assertEqual(set(res), {'2', '5', '9'})

       




   