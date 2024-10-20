from brawler import Brawler
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.brawlers = []  # List of the player's 3 chosen Brawlers
        self.deck = []  # The deck of 10 cards
        self.hand = []  # The player's current hand of cards
        self.actions_per_turn = 3

    def choose_brawlers(self, available_brawlers):
        """Allow the player to choose 3 Brawlers."""
        self.brawlers = random.sample(available_brawlers, 3)  # For simplicity, use random selection for now then we will use player input
    
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

