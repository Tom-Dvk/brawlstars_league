from brawler import Brawler
import random
from team import Team

class Player:
    def __init__(self, name):
        self.name = name
        self.team = Team(f"{self.name}'s Team")  # Each player has a team of 3 Brawlers
        self.deck = []  # The deck of 10 cards
        self.hand = []  # The player's current hand of cards
        self.actions_per_turn = 3

    def choose_brawlers(self, available_brawlers):
        """Allow the player to choose 3 Brawlers."""
        chosen_brawlers = random.sample(available_brawlers, 3)  # For simplicity, use random selection for now then we will use player input
        for brawler in chosen_brawlers:
            self.team.add_brawler(brawler)
    
    def display_team(self):
        """Display the player's team of Brawlers."""
        self.team.display_team()
    
    def build_deck(self):
        """Build a deck of cards based on chosen Brawlers."""
        for brawler in self.brawlers:
            self.deck.extend(brawler['cards']['brawler_specific'])
        # Add 3 random equipment cards (for now)
        self.deck.extend(random.sample(equipment_cards_pool, 3)) # Simplified: Randomly choose 3 equipment cards from a pool

    def draw_cards(self, deck):
        """Draw cards from the deck."""
        self.hand = [deck.draw_card() for _ in range(3)]

    def take_turn(self, grid):
        """Player takes their turn, choosing to move, attack, or use abilities."""
        for _ in range(self.actions_per_turn):
            # Example: Move a Brawler
            brawler = self.brawlers[0]  # Simplified: Choose a Brawler to act
            new_x, new_y = self.choose_movement()
            brawler.move(grid, new_x, new_y)

            # Example: Play a card
            card = self.hand.pop(0)  # Simplified: Play the first card in hand
            card.activate(brawler)

    def choose_movement(self):
        """For now, choose a random movement. Can be replaced by player input."""
        return (random.randint(0, 4), random.randint(0, 4))

