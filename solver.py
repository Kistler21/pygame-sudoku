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
