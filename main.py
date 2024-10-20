import pygame
from gridmap import GridMap
from card import CardDeck
from brawler import Brawler
from player import Player
from match import Match

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

# Create Brawlers
brawler1 = Brawler("Shelly", 3600, 500, 3)
brawler2 = Brawler("Colt", 3200, 600, 4)
brawler3 = Brawler("Jessie", 3400, 400, 3)  # Add a third Brawler
brawler4 = Brawler("Brock", 2800, 800, 5)   # Add a fourth Brawler

# Make sure to pass enough Brawlers to choose from
available_brawlers = [brawler1, brawler2, brawler3, brawler4]

# Create Players
player1 = Player("Alice")
player2 = Player("Bob")
player1.choose_brawlers(available_brawlers)
player2.choose_brawlers(available_brawlers)

# Place Brawlers on the grid (simplified example)
grid.place_brawler(brawler1, 0, 0)
grid.place_brawler(brawler2, 1, 1)

# Create a match between the two teams
match = Match(player1.team, player2.team, grid)

# Start the match (alternates between players until a winner is decided)
match.play_match()

# Main Game Loop
running = True
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

    pygame.display.flip()

pygame.quit()
