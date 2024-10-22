import pygame
import sys
import os
import json
from game.gridmap import GridMap
#from game.player import Player
from game.brawler import Brawler
from game.card import Card


# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 60, 90  # Adjust as needed
HAND_Y_POSITION = SCREEN_HEIGHT - CARD_HEIGHT - 10  # 10 pixels from the bottom


# Load card images and create card instances
def load_player_hand():
    hand = []
    for i in range(10):
        card_image_path = f'assets/images/cards/pokemon-hoopa.png'  # Replace with actual paths
        position = (10 + i * (CARD_WIDTH + 5), HAND_Y_POSITION)  # Spacing between cards
        card = Card(f'Card {i}', card_image_path, position)
        hand.append(card)
    return hand

def load_deck():
    deck_image_path = 'assets/images/cards/brawlstars_card_back.png'
    position = (SCREEN_WIDTH - CARD_WIDTH - 10, HAND_Y_POSITION)
    deck_card = Card('Deck', deck_image_path, position)
    return deck_card

def load_available_brawlers(cell_size):
    brawlers = []
    data_file = os.path.join('data', 'brawlers_data.json')

    # Load brawler data from JSON file
    with open(data_file, 'r') as f:
        brawler_data_dict = json.load(f)

    # Define icon positions for the selection screen
    icon_positions = []
    icon_spacing = 70  # Space between icons
    icons_per_row = 5
    start_x, start_y = 50, 50

    index = 0
    for brawler_name, brawler_data in brawler_data_dict.items():
        # Calculate icon position
        row = index // icons_per_row
        col = index % icons_per_row
        x = start_x + col * icon_spacing
        y = start_y + row * icon_spacing
        icon_position = (x, y)

        # Construct file paths using the brawler's name
        image_path = f"assets/images/brawlers/{brawler_name}.png"
        icon_image_path = f"assets/images/brawler_icons/{brawler_name}.png"

        # Verify that the image files exist
        if not os.path.isfile(image_path):
            print(f"Image file not found for {brawler_name}: {image_path}")
            continue  # Skip this brawler if image is missing
        if not os.path.isfile(icon_image_path):
            print(f"Icon image file not found for {brawler_name}: {icon_image_path}")
            continue  # Skip this brawler if icon image is missing

        # Create Brawler instance
        brawler = Brawler(
            name=brawler_name,
            position=(0, 0),  # Will be set when the game starts
            image_path=image_path,
            cell_size=cell_size,
            icon_image_path=icon_image_path,
            data=brawler_data  # Pass the entire brawler data
        )
        brawler.icon_position = icon_position

        brawlers.append(brawler)
        index += 1

    return brawlers

def brawler_selection_screen(screen, clock, cell_size):
    selected_brawlers = []
    available_brawlers = load_available_brawlers(cell_size)

    # Set up the selection screen
    running = True
    while running:
        screen.fill((50, 50, 50))  # Dark background

        # Display available brawlers
        for brawler in available_brawlers:
            brawler.draw_icon(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                for brawler in available_brawlers:
                    if brawler.is_mouse_over_icon(mouse_pos):
                        if brawler not in selected_brawlers:
                            selected_brawlers.append(brawler)
                        if len(selected_brawlers) == 3:
                            running = False
                        break

        pygame.display.flip()
        clock.tick(60)

    return selected_brawlers


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width, screen_height = 1000, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Brawl Stars Card Game')

    # Game clock
    clock = pygame.time.Clock()

    # Load cards
    player_hand = load_player_hand()
    deck_card = load_deck()

    # Create game objects
    cell_size = 100
    grid_map = GridMap(rows=10, cols=6, cell_size=cell_size)

    #player1 = Player(name='Player 1')
    #player2 = Player(name='Player 2')
    # After setting up the grid_map
    # Position the selected brawlers on the grid

    # Brawler selection
    selected_brawlers = brawler_selection_screen(screen, clock, cell_size)
    brawler1 = selected_brawlers[0]
    brawler1.position = (0, 0)
    brawler2 = selected_brawlers[1]
    brawler2.position = (4, 4)
    brawler1 = Brawler('Shelly', (0, 0), 'assets/images/brawlers/Shelly.png', cell_size)
    brawler2 = Brawler('Nita', (4, 4), 'assets/images/brawlers/Nita.png', cell_size)

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle other events (mouse clicks, key presses)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    # Determine which cell was clicked
                    col = mouse_pos[0] // grid_map.cell_size
                    row = mouse_pos[1] // grid_map.cell_size
                    print(f'Clicked on cell ({row}, {col})')

                    # If a card is selected, check if the button is clicked
                    selected_card = next((card for card in player_hand if card.is_selected), None)
                    if selected_card:
                        # Check if the play button is clicked
                        if selected_card.button_rect.collidepoint(mouse_pos):
                            print(f'Playing card: {selected_card.name}')
                            # Handle playing the card
                            selected_card.is_selected = False
                            # Remove the card from the hand
                            player_hand.remove(selected_card)
                        # Check if clicked outside the card and button
                        elif not selected_card.zoomed_rect.collidepoint(mouse_pos):
                            selected_card.is_selected = False
                    else:
                        # Check if any card in the hand is clicked
                        for card in player_hand:
                            if card.is_mouse_over(mouse_pos):
                                card.is_selected = True
                                break
                            else:
                                # Deselect cards if clicked outside
                                for card in player_hand:
                                    card.is_selected = False


                    # Check if a brawler is already selected
                    if brawler1.is_selected:
                        possible_moves = brawler1.get_possible_moves(grid_map)
                        if (row, col) in possible_moves:
                            # Move the brawler
                            brawler1.position = (row, col)
                            brawler1.is_selected = False
                    else:
                        # Check if the brawler is clicked
                        brawler_rect = brawler1.get_rect(grid_map.cell_size)
                        if brawler_rect.collidepoint(mouse_pos):
                            brawler1.is_selected = True
            # Handle selection or movement

        # Update game state
        # grid_map.update()
        # player1.update()
        # player2.update()

        # Clear the screen
        screen.fill((0, 0, 0))  # Fill with black color

        # Draw game objects
        grid_map.draw(screen)
        # player1.draw(screen)
        # player2.draw(screen)

        # If a brawler is selected, highlight possible moves
        if brawler1.is_selected:
            possible_moves = brawler1.get_possible_moves(grid_map)
            grid_map.draw_possible_moves(screen, possible_moves)


        # In the main game loop, draw the brawlers
        brawler1.draw(screen, grid_map.cell_size)
        brawler2.draw(screen, grid_map.cell_size)

        # Draw cards
        for card in player_hand:
            if card.is_selected:
                # Draw the zoomed-in card and button
                card.draw_zoomed(screen, SCREEN_WIDTH, SCREEN_HEIGHT, CARD_WIDTH, CARD_HEIGHT)
                card.draw_play_button(screen, SCREEN_WIDTH)
            else:
                card.draw(screen)
        deck_card.draw(screen)


        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
