import random
import time


class Cell:
    '''Represents a cell within a game of Sudoku.'''

    def __init__(self, row, col, value=None):
        '''Initializes an instance of a Sudoku cell.'''
        self.row = row
        self.col = col
        self.value = value

    @property
    def row(self):
        '''Getter method for row.'''
        return self._row

    @row.setter
    def row(self, row):
        '''Setter method for row.'''
        if row < 0 or row > 8:
            raise AttributeError('Row must be between 0 and 8.')
        else:
            self._row = row

    @property
    def col(self):
        '''Getter method for col.'''
        return self._col

    @col.setter
    def col(self, col):
        '''Setter method for col.'''
        if col < 0 or col > 8:
            raise AttributeError('Col must be between 0 and 8.')
        else:
            self._col = col

    @property
    def value(self):
        '''Getter method for value.'''
        return self._value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    @value.setter
    def value(self, value):
        '''Setter method for value.'''
        if value != None and (value < 1 or value > 9):
            raise AttributeError('Value must be between 1 and 9.')
        else:
            self._value = value


class Sudoku:
    '''Represents a game/board of Sudoku.'''

    def __init__(self, board=None):
        '''Initializes an instance of a Sudoku game.'''
        if board == None:
            self.generate_board()
        else:
            self.board = []
            for row in range(9):
                self.board.append([])
                for col in range(9):
                    if board[row][col] == 0:
                        val = None
                    else:
                        val = board[row][col]
                    self.board[row].append(Cell(row, col, val))

    def check_move(self, cell, num):
        '''Returns whether a number is a valid move for a cell.'''
        # Check if the number is valid for the row
        for col in range(9):
            if self.board[cell.row][col].value == num:
                return False

        # Check if the number is valid for the column
        for row in range(9):
            if self.board[row][cell.col].value == num:
                return False

        # Check if the number is valid in its box
        for row in range(cell.row // 3 * 3, cell.row // 3 * 3 + 3):
            for col in range(cell.col // 3 * 3, cell.col // 3 * 3 + 3):
                if self.board[row][col].value == num:
                    return False

        # Move is valid
        return True

    def get_possible_moves(self, cell):
        '''Returns a list of the valid moves for a cell.'''
        possible_moves = [num for num in range(1, 10)]

        # Check numbers in the row
        for col in range(9):
            if self.board[cell.row][col].value in possible_moves:
                possible_moves.remove(self.board[cell.row][col].value)

        # Check numbers in the column
        for row in range(9):
            if self.board[row][cell.col].value in possible_moves:
                possible_moves.remove(self.board[row][cell.col].value)

        # Check numbers in the box
        for row in range(cell.row // 3 * 3, cell.row // 3 * 3 + 3):
            for col in range(cell.col // 3 * 3, cell.col // 3 * 3 + 3):
                if self.board[row][col].value in possible_moves:
                    possible_moves.remove(self.board[row][col].value)

        return possible_moves

    def get_empty_cell(self):
        '''Returns an empty cell. Returns False if all cells are filled in.'''
        for row in range(9):
            for col in range(9):
                if self.board[row][col].value == None:
                    return self.board[row][col]

        return False

    def solve(self):
        '''
        Solves the game from it's current state with a backtracking algorithm.
        Returns True if successful and False if not solvable.
        '''
        cell = self.get_empty_cell()

        # Board is complete if cell is false
        if not cell:
            return True

        # Check each possible value in cell
        for val in range(1, 10):

            # Check if the value is a valid move
            if not self.check_move(cell, val):
                continue

            # Place value in board
            cell.value = val

            # If all recursive calls return True then board is solved
            if self.solve() == True:
                return True

            # Undo move is solve was unsuccessful
            cell.value = None

        # No moves were successful
        return False

    def generate_board(self):
        '''Generates a random, solvable game of Sudoku.'''
        # Create list of open squares
        self.board = [[Cell(row, col) for col in range(9)] for row in range(9)]

        open_positions = []
        for row in range(9):
            for col in range(9):
                open_positions.append(str(row) + str(col))

        # Shuffle open_positions so order is random
        random.seed()
        random.shuffle(open_positions)

        # Put random numbers into board until is it full
        while len(open_positions) > 0:
            # Get random empty cell
            spot_to_fill = open_positions.pop()
            row = int(spot_to_fill[0])
            col = int(spot_to_fill[1])
            cell = self.board[row][col]

            # Make random move for cell unitl valid move is made
            moves = self.get_possible_moves(cell)
            random.shuffle(moves)
            while True:
                num = moves.pop()
                cell.value = num
                if self.test_solve():
                    break

    def get_board(self):
        '''Returns a list of values that are in the Sudoku board.'''
        return [[self.board[row][col].value for col in range(9)] for row in range(9)]

    def test_solve(self):
        '''Checks if the current configuration is solvable.'''
        current_board = self.get_board()
        solvable = self.solve()

        # Reset board to state before solve check
        for row in range(9):
            for col in range(9):
                self.board[row][col].value = current_board[row][col]

        return solvable

    def __str__(self):
        '''Returns a string representing the board.'''
        board = ''
        for row, line in enumerate(self.board):
            for col, cell in enumerate(line):
                if cell.value == None:
                    val = ' '
                else:
                    val = cell.value
                if col < 8:
                    board += f' {val} |'
                    if (col + 1) % 3 == 0:
                        board += '|'
                else:
                    board += f' {val}'
            if row < 8:
                board += '\n---|---|---||---|---|---||---|---|---\n'
                if (row + 1) % 3 == 0:
                    board += '---|---|---||---|---|---||---|---|---\n'
        return board


if __name__ == '__main__':
    s = Sudoku()
    print(s)
