import pygame

class Card:
    def __init__(self, name, image_path, position):
        self.name = name
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.is_selected = False  # To track if the card is selected

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_mouse_over(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw_zoomed(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, CARD_WIDTH, CARD_HEIGHT):
        # Zoom the card to a larger size
        zoom_width, zoom_height = CARD_WIDTH * 2, CARD_HEIGHT * 2
        zoomed_image = pygame.transform.scale(self.image, (zoom_width, zoom_height))
        # Center the card on the screen
        center_x = (SCREEN_WIDTH - zoom_width) // 2
        center_y = (SCREEN_HEIGHT - zoom_height) // 2
        screen.blit(zoomed_image, (center_x, center_y))
        self.zoomed_rect = pygame.Rect(center_x, center_y, zoom_width, zoom_height)

    def draw_play_button(self, screen, SCREEN_WIDTH):
        # Draw a "Play the Card" button below the zoomed card
        button_width, button_height = 120, 40
        button_x = (SCREEN_WIDTH - button_width) // 2
        button_y = self.zoomed_rect.bottom + 10
        self.button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, (0, 255, 0), self.button_rect)
        # Render button text
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render('Play the Card', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        screen.blit(text_surface, text_rect)