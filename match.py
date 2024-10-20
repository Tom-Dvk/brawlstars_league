class Match:
    def __init__(self, team1, team2, grid):
        self.team1 = team1
        self.team2 = team2
        self.grid = grid
        self.turn = 0
        self.current_team = team1  # Start with team1
        self.game_over = False

    def play_turn(self):
        """Play a single turn and then return control to the main loop."""
        if self.game_over:
            return

        self.turn += 1
        print(f"\nTurn {self.turn}: {self.current_team.team_name}'s turn")
        
        # Each team takes a turn, alternate between teams
        if self.turn % 2 == 1:
            self.take_turn(self.team1)
        else:
            self.take_turn(self.team2)

        # Switch teams after each turn
        self.current_team = self.team2 if self.current_team == self.team1 else self.team1

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
        if all(brawler.health <= 0 for brawler in self.team1.brawlers):
            print(f"{self.team2.team_name} wins!")
            return True
        elif all(brawler.health <= 0 for brawler in self.team2.brawlers):
            print(f"{self.team1.team_name} wins!")
            return True
        return False
