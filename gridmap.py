class GridMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]  # 2D grid representation

    def place_brawler(self, brawler, x, y):
        """Place a brawler on the grid at a specific position."""
        self.grid[y][x] = brawler
        brawler.position = (x, y)

    def move_brawler(self, brawler, new_x, new_y):
        """Move a brawler to a new position on the grid."""
        old_x, old_y = brawler.position
        if self.grid[new_y][new_x] is None:  # Make sure the new position is free
            self.grid[old_y][old_x] = None  # Free the old position
            self.grid[new_y][new_x] = brawler
            brawler.position = (new_x, new_y)
            print(f"{brawler.name} moves to ({new_x}, {new_y})")
        else:
            print("Position occupied!")

    def display_grid(self):
        """Print the current state of the grid."""
        for row in self.grid:
            print(["B" if b is not None else "." for b in row])
