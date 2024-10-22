class Game:
    def __init__(self, player, robot, grid):
        self.player = player
        self.robot = robot
        self.grid = grid
        self.turn = 0
        self.current_turn = "player"  # Player starts first
        self.game_over = False

    def play_turn(self):
        """Play a single turn and then return control to the main loop."""
        if self.game_over:
            return

        self.turn += 1
        print(f"\nTurn {self.turn}: {self.current_team.team_name}'s turn")

        # Each team takes a turn, alternate between teams
        if self.turn % 2 == 1:
            self.take_turn(self.player)
        else:
            self.take_turn(self.robot)

        # Switch teams after each turn
        self.current_team = self.robot if self.current_team == self.player else self.player

        # Check for win conditions after every turn
        if self.check_win_conditions():
            self.game_over = True

    def take_turn(self, team):
        """Allow a team to take its turn."""
        print(f"{team.team_name} is taking their turn.")
        # For now, just print Brawler status
        for brawler in team.brawlers:
            print(f"{brawler.name} is ready with {brawler.health} HP")

    def check_win_conditions(self):
        """Check if one team has won by eliminating all Brawlers of the other team."""
        if all(brawler.health <= 0 for brawler in self.player.brawlers):
            print(f"{self.robot.team_name} wins!")
            return True
        elif all(brawler.health <= 0 for brawler in self.robot.brawlers):
            print(f"{self.player.team_name} wins!")
            return True
        return False
