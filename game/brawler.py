import pygame

class Brawler:
    def __init__(self, name, position, image_path, icon_image_path, cell_size, data):
        self.name = name
        self.position = position  # (row, col)

        # Scale the image to fit the cell size while maintaining proportion
        self.original_image = pygame.image.load(image_path).convert_alpha()
        image_width, image_height = self.original_image.get_size()
        aspect_ratio = image_width / image_height
        cell_size_reduced = cell_size * 0.97

        self.data = data 


        scaled_height = cell_size_reduced # Height is the limiting factor
        scaled_width = int(scaled_height * aspect_ratio)
        self.image = pygame.transform.scale(self.original_image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        
        # Create an icon for the selection screen
        self.icon_image = pygame.image.load(icon_image_path).convert_alpha()
        self.icon_image = pygame.transform.scale(self.icon_image, (50, 50))
        self.icon_rect = self.icon_image.get_rect()

    def draw(self, screen, cell_size):
        row, col = self.position
        self.rect.center = ((col + 0.5) * cell_size, (row + 0.5) * cell_size)
        screen.blit(self.image, self.rect)
    
    def get_possible_moves(self, grid):
        # Calculate possible moves (up to 2 cells on each side, no diagonal)
        moves = []
        row, col = self.position
        max_row, max_col = grid.rows - 1, grid.cols - 1

        for i in range(1, 3):  # Move 1 or 2 cells
            # Up
            if row - i >= 0:
                moves.append((row - i, col))
            # Down
            if row + i <= max_row:
                moves.append((row + i, col))
            # Left
            if col - i >= 0:
                moves.append((row, col - i))
            # Right
            if col + i <= max_col:
                moves.append((row, col + i))

        return moves
    
    def get_rect(self, cell_size):
        row, col = self.position
        rect = pygame.Rect(
            col * cell_size,
            row * cell_size,
            cell_size,
            cell_size
        )
        return rect
    
    def draw_icon(self, screen):
        # Position icons appropriately
        # For simplicity, arrange them in a grid or list
        screen.blit(self.icon_image, self.icon_rect)

    def is_mouse_over_icon(self, mouse_pos):
        return self.icon_rect.collidepoint(mouse_pos)

