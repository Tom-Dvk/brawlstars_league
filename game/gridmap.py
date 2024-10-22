import pygame

class GridMap:
    def __init__(self, rows=5, cols=5, cell_size=100):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)  # White grid lines

    def draw_possible_moves(self, screen, moves):
        for row, col in moves:
            rect = pygame.Rect(
                col * self.cell_size,
                row * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(screen, (0, 255, 0), rect, 3)  # Green border
