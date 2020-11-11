import unittest
from solver import Cell, Sudoku


class TestCell(unittest.TestCase):
    def test_row_error(self):
        with self.assertRaises(AttributeError):
            Cell(9, 5, 3)
        with self.assertRaises(AttributeError):
            c = Cell(1, 1)
            c.row = -2

    def test_col_error(self):
        with self.assertRaises(AttributeError):
            Cell(6, -1, 3)
        with self.assertRaises(AttributeError):
            c = Cell(1, 1)
            c.col = 23

    def test_value_error(self):
        with self.assertRaises(AttributeError):
            Cell(6, 2, 10)
        with self.assertRaises(AttributeError):
            c = Cell(1, 1)
            c.value = 0

    def test_value(self):
        c = Cell(5, 8)
        c.value = 3
        self.assertEqual(c.value, 3)


if __name__ == '__main__':
    # unittest.main()
    easy = [
        [0, 0, 0, 9, 0, 0, 0, 3, 0],
        [3, 0, 6, 0, 2, 0, 0, 4, 0],
        [2, 0, 4, 0, 0, 3, 1, 0, 6],
        [0, 7, 0, 0, 5, 1, 0, 8, 0],
        [0, 3, 1, 0, 6, 0, 0, 5, 7],
        [5, 0, 9, 0, 0, 0, 6, 0, 0],
        [4, 1, 0, 0, 0, 2, 0, 7, 8],
        [7, 6, 3, 0, 0, 5, 4, 0, 0],
        [9, 2, 8, 0, 0, 4, 0, 0, 1]
    ]
    hard = [
        [0, 0, 0, 0, 9, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 7, 6, 0, 3],
        [0, 7, 0, 5, 0, 0, 0, 0, 1],
        [0, 0, 0, 9, 0, 0, 1, 3, 4],
        [0, 2, 0, 0, 0, 0, 0, 8, 0],
        [3, 5, 4, 0, 0, 8, 0, 0, 0],
        [7, 0, 0, 0, 0, 9, 0, 4, 0],
        [5, 0, 1, 3, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 5, 0, 0, 0, 0]
    ]
    evil = [
        [0, 5, 0, 0, 0, 4, 3, 2, 0],
        [0, 0, 0, 2, 5, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 4, 0],
        [0, 0, 8, 0, 0, 9, 0, 0, 0],
        [4, 0, 2, 0, 0, 0, 6, 0, 5],
        [0, 0, 0, 7, 0, 0, 8, 0, 0],
        [0, 9, 0, 4, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 3, 1, 0, 0, 0],
        [0, 1, 6, 9, 0, 0, 0, 7, 0]
    ]
    test = [
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [1, 0, 0, 8, 0, 0, 0, 7, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 2, 8, 0, 0],
        [0, 5, 7, 0, 9, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 2, 5, 4, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    s = Sudoku(test)
    print(s)
    print(s.solve())
    print(s)
