import random

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.brawlers = []  # List of 3 chosen Brawlers
        self.deck = []  # The deck of 10 cards

    def choose_brawlers(self, available_brawlers):
        """Allow the player to choose 3 Brawlers."""
        self.brawlers = random.sample(available_brawlers, 3)  # For simplicity, use random selection for now

    def build_deck(self):
        """Build a deck of cards based on chosen Brawlers."""
        self.deck = []
        for brawler in self.brawlers:
            self.deck.extend(brawler['cards']['brawler_specific'])
        # Add 3 random equipment cards (for now)
        self.deck.extend(random.sample(equipment_cards_pool, 3))

    def take_turn(self):
        """Player takes their turn by moving and playing a card."""
        print(f"{self.player_name}'s turn")
        # Move Brawlers
        # Play a card from the hand
