class GridMap:
    def __init__(self, grid_size, cell_size):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.selected_brawler = None

    def draw_grid(self, screen):
        """Draw the grid on the screen."""
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    def place_brawler(self, brawler, x, y):
        """Place a Brawler on the grid at a specific location."""
        self.grid[y][x] = brawler
        brawler.position = (x, y)

    def move_brawler(self, brawler, new_x, new_y):
        """Move a Brawler to a new grid position."""
        old_x, old_y = brawler.position
        if self.grid[new_y][new_x] is None:
            self.grid[old_y][old_x] = None
            self.grid[new_y][new_x] = brawler
            brawler.position = (new_x, new_y)

    def handle_click(self, pos):
        """Handle clicks for selecting and moving Brawlers."""
        x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
        if self.selected_brawler is None:
            self.selected_brawler = self.grid[y][x]  # Select a Brawler
        else:
            self.move_brawler(self.selected_brawler, x, y)
            self.selected_brawler = None
