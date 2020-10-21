import unittest
from solver import Cell


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
    unittest.main()
