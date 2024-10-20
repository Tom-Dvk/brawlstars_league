class Card:
    def __init__(self, name, effect, card_type):
        self.name = name
        self.effect = effect  # Description of the effect (e.g., damage)
        self.card_type = card_type  # e.g., "Attack", "Super", "Equipment"

    def activate(self, brawler, target=None):
        """Activate the card's effect, either on the brawler or a target."""
        print(f"{brawler.name} uses {self.name}: {self.effect}")
        if target:
            target.health -= self.effect["damage"]
            print(f"{target.name} takes {self.effect['damage']} damage. Remaining health: {target.health}")
