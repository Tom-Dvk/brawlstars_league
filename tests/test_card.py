import pygame

class Card:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def activate(self, brawler):
        """Activate the card's effect on a Brawler."""
        if "damage" in self.effect:
            brawler.health -= self.effect["damage"]
            print(f"{brawler.name} takes {self.effect['damage']} damage! Remaining health: {brawler.health}")
        elif "heal" in self.effect:
            brawler.health += self.effect["heal"]
            print(f"{brawler.name} is healed by {self.effect['heal']}! Remaining health: {brawler.health}")

class CardDeck:
    def __init__(self):
        self.cards = [
            Card("Shotgun Blast", {"damage": 100}),
            Card("Super Shell", {"damage": 200}),
            Card("Healing Gadget", {"heal": 50}),
        ]

    def draw_deck(self, screen, card_area_start_y):
        """Draw the cards at the bottom of the screen."""
        for i, card in enumerate(self.cards):
            pygame.draw.rect(screen, (0, 255, 0), (i * 200, card_area_start_y, 180, 100))
            font = pygame.font.Font(None, 24)
            text = font.render(card.name, True, (255, 255, 255))
            screen.blit(text, (i * 200 + 10, card_area_start_y + 20))

    def handle_card_click(self, pos, selected_brawler, card_area_start_y):
        """Handle clicking a card to activate it on a Brawler."""
        if pos[1] > card_area_start_y:  # Click is in the card area
            card_index = pos[0] // 200
            if 0 <= card_index < len(self.cards):
                card = self.cards[card_index]
                if selected_brawler:
                    card.activate(selected_brawler)
