class Brawler:
    def __init__(self, name, health, attack, movement_range):
        self.name = name
        self.health = health
        self.attack = attack
        self.movement_range = movement_range
        self.position = None  # This will be set when the Brawler is placed on the grid

    def move(self, grid, new_x, new_y):
        """Move the Brawler on the grid."""
        grid.move_brawler(self, new_x, new_y)
