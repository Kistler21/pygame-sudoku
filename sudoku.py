import pygame
import sys
from solver import Cell, Sudoku


pygame.init()

# Set size of game and other constants
cell_size = 50
minor_grid_size = 1
major_grid_size = 3
edge_buffer = 5
width = cell_size*9 + minor_grid_size*6 + major_grid_size*4 + edge_buffer*2
height = cell_size*9 + minor_grid_size*6 + major_grid_size*4 + edge_buffer*2
size = width, height
white = 255, 255, 255
black = 0, 0, 0
gray = 200, 200, 200

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sudoku')


class RectCell(pygame.Rect):
    '''
    A class built upon the pygame Rect class used to represent individual cells in the game.
    This class has a few extra attributes not contained within the base Rect class.
    '''

    def __init__(self, left, top, row, col):
        super().__init__(left, top, cell_size, cell_size)
        self.row = row
        self.col = col


def create_cells():
    '''Creates all 81 cells with RectCell class.'''
    cells = [[] for _ in range(9)]

    # Set attributes for for first RectCell
    row = 0
    col = 0
    left = edge_buffer + major_grid_size
    top = edge_buffer + major_grid_size

    while row < 9:
        while col < 9:
            cells[row].append(RectCell(left, top, row, col))

            # Update attributes for next RectCell
            left += cell_size + minor_grid_size
            if col != 0 and (col + 1) % 3 == 0:
                left = left + major_grid_size - minor_grid_size
            col += 1

        # Update attributes for next RectCell
        top += cell_size + minor_grid_size
        if row != 0 and (row + 1) % 3 == 0:
            top = top + major_grid_size - minor_grid_size
        left = edge_buffer + major_grid_size
        col = 0
        row += 1

    return cells


def draw_grid():
    '''Draws the major and minor grid lines for Sudoku.'''
    # Draw minor grid lines
    lines_drawn = 0
    pos = edge_buffer + major_grid_size + cell_size
    while lines_drawn < 6:
        pygame.draw.line(screen, black, (pos, edge_buffer),
                         (pos, width-edge_buffer-1), minor_grid_size)
        pygame.draw.line(screen, black, (edge_buffer, pos),
                         (width-edge_buffer-1, pos), minor_grid_size)

        # Update number of lines drawn
        lines_drawn += 1

        # Update pos for next lines
        pos += cell_size + minor_grid_size
        if lines_drawn % 2 == 0:
            pos += cell_size + major_grid_size

    # Draw major grid lines
    for pos in range(edge_buffer+major_grid_size//2, width, cell_size*3 + minor_grid_size*2 + major_grid_size):
        pygame.draw.line(screen, black, (pos, edge_buffer),
                         (pos, width-edge_buffer-1), major_grid_size)
        pygame.draw.line(screen, black, (edge_buffer, pos),
                         (width-edge_buffer-1, pos), major_grid_size)


def fill_cells(cells, board):
    '''Fills in all the numbers for the game.'''
    font = pygame.font.Font(None, 36)
    font.bold = True

    for row in range(9):
        for col in range(9):
            if board.board[row][col].value is None:
                continue
            text = font.render(f'{board.board[row][col].value}', 1, black)
            xpos, ypos = cells[row][col].center
            xpos -= 6
            ypos -= 10
            screen.blit(text, (xpos, ypos))


def play():
    '''Contains all the functionality for playing a game of Sudoku.'''
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
    game = Sudoku(easy)
    cells = create_cells()
    active_cell = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Handle mouse click
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                # Test if point in any rect
                active_cell = None
                for row in cells:
                    for cell in row:
                        if cell.collidepoint(mouse_pos):
                            active_cell = cell

                # Test if active cell is empty
                if game.board[active_cell.row][active_cell.col].value is not None:
                    active_cell = None

        screen.fill(white)
        draw_grid()
        fill_cells(cells, game)
        if active_cell is not None:
            pygame.draw.rect(screen, gray, active_cell)
        pygame.display.flip()


if __name__ == '__main__':
    play()
