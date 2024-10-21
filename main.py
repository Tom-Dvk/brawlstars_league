import pygame
from gridmap import GridMap
from card import CardDeck
from brawler import Brawler
from player import Player
from game import Game

# Initialize Pygame
pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600  # Extra space for card deck
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Brawler Game")

# Game Setup
grid = GridMap(5, 100)
card_deck = CardDeck()

# Create Brawlers
brawler1 = Brawler("Shelly", 3600, 500, 3)
brawler2 = Brawler("Colt", 3200, 600, 4)
brawler3 = Brawler("Jessie", 3400, 400, 3)
brawler4 = Brawler("Brock", 2800, 800, 5)

# Create Players
player1 = Player("Alice")
player2 = Player("Bob")
available_brawlers = [brawler1, brawler2, brawler3, brawler4]

# Choose Brawlers for each player
player1.choose_brawlers(available_brawlers)
player2.choose_brawlers(available_brawlers)

# Place Brawlers on the grid (example positions)
grid.place_brawler(brawler1, 0, 0)
grid.place_brawler(brawler2, 1, 1)
grid.place_brawler(brawler3, 2, 2)
grid.place_brawler(brawler4, 3, 3)

# Create a match between the two teams
match = Match(player1.team, player2.team, grid)

# Main Game Loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))  # Black background
    grid.draw_grid(screen)
    card_deck.draw_deck(screen, grid.grid_size * grid.cell_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] < grid.grid_size * grid.cell_size:  # Click is inside the grid
                grid.handle_click(pos)
            else:  # Click is in the card area
                card_deck.handle_card_click(pos, grid.selected_brawler, grid.grid_size * grid.cell_size)

    # Play one turn per frame
    if not match.game_over:
        match.play_turn()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(1)  # Slow down the game, 1 FPS (adjust this for testing)
    
pygame.quit()
