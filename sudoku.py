import pygame
import sys
from solver import Cell, Sudoku


pygame.init()

# Set size of game and other constants
cell_size = 75
minor_grid_size = 1
major_grid_size = 3
edge_buffer = 5
width = cell_size*9 + minor_grid_size*6 + major_grid_size*4 + edge_buffer*2
height = cell_size*9 + minor_grid_size*6 + major_grid_size*4 + edge_buffer*2
size = width, height
white = 255, 255, 255
black = 0, 0, 0

screen = pygame.display.set_mode(size)


def draw_grid():
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


def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(white)
        draw_grid()
        pygame.display.flip()


if __name__ == '__main__':
    play()
