import unittest

import src.lab3.sudoku as sudoku
import random, string

class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        res = sudoku.group([1,2,3,4], 2)
        self.assertEqual(res, [[1, 2], [3, 4]])

        res = sudoku.group([1,2,3,4,5,6,7,8,9], 3)
        self.assertEqual(res, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
   