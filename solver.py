import random


class Cell:
    '''Represents a cell within a game of Sudoku.'''

    def __init__(self, row, col, value, editable):
        '''Initializes an instance of a Sudoku cell.'''
        self.row = row
        self.col = col
        self.value = value
        self._editable = editable

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

    @property
    def editable(self):
        '''Getter method for editable.'''
        return self._editable

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    @value.setter
    def value(self, value):
        '''Setter method for value.'''
        if value is not None and (value < 1 or value > 9):
            raise AttributeError('Value must be between 1 and 9.')
        else:
            self._value = value


class Sudoku:
    '''Represents a game/board of Sudoku.'''

    def __init__(self, board):
        '''Initializes an instance of a Sudoku game.'''
        self.board = []
        for row in range(9):
            self.board.append([])
            for col in range(9):
                if board[row][col] == 0:
                    val = None
                    editable = True
                else:
                    val = board[row][col]
                    editable = False
                self.board[row].append(Cell(row, col, val, editable))

    def check_move(self, cell, num):
        '''Returns whether a number is a valid move for a cell.'''
        # Check if the number is valid for the row
        for col in range(9):
            if self.board[cell.row][col].value == num and col != cell.col:
                return False

        # Check if the number is valid for the column
        for row in range(9):
            if self.board[row][cell.col].value == num and row != cell.row:
                return False

        # Check if the number is valid in its box
        for row in range(cell.row // 3 * 3, cell.row // 3 * 3 + 3):
            for col in range(cell.col // 3 * 3, cell.col // 3 * 3 + 3):
                if (
                    self.board[row][col].value == num
                    and row != cell.row
                    and col != cell.col
                ):
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
                if self.board[row][col].value is None:
                    return self.board[row][col]

        return False

    def solve(self):
        '''
        Solves the game from it's current state with a backtracking algorithm.
        Returns True if successful and False if not solvable.
        '''
        cell = self.get_empty_cell()

        # Board is complete if cell is False
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
            if self.solve():
                return True

            # Undo move is solve was unsuccessful
            cell.value = None

        # No moves were successful
        return False

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

    def reset(self):
        '''Resets the game to its starting state.'''
        for row in self.board:
            for cell in row:
                if cell.editable:
                    cell.value = None

    def __str__(self):
        '''Returns a string representing the board.'''
        board = ' -----------------------\n'
        for row, line in enumerate(self.board):
            board += '|'
            for col, cell in enumerate(line):
                if cell.value is None:
                    val = '-'
                else:
                    val = cell.value
                if col < 8:
                    board += f' {val}'
                    if (col + 1) % 3 == 0:
                        board += ' |'
                else:
                    board += f' {val} |\n'
            if row < 8 and (row + 1) % 3 == 0:
                board += '|-------|-------|-------|\n'
        board += ' -----------------------\n'
        return board
