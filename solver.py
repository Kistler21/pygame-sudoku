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

    def solve(self):
        '''
        Solves the game from it's current state with a backtracking algorithm.
        Returns True if successful and False if not solvable.
        '''
        # Loop through each cell
        for row in range(9):
            for col in range(9):

                # Check if cell is empty
                if self.board[row][col].value == None:

                    # Check each possible value in cell
                    for val in range(1, 10):

                        # Check if the value is a valid move
                        if not self.check_move(self.board[row][col], val):
                            continue

                        # Place value in board
                        self.board[row][col].value = val

                        # If all recursive calls return True then board is solved
                        if self.solve() == True:
                            return True

                        # Undo move is solve was unsuccessful
                        self.board[row][col].value = None

                    # No moves were successful
                    return False

        # No cells are empty meaning board is solved
        return True

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
