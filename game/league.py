from game import Game

class League:
    def __init__(self, teams):
        self.teams = teams
        self.matches = []
        self.results = {}

    def schedule_match(self, team1, team2, grid):
        """Schedule a match between two teams."""
        match = Match(team1, team2, grid)
        self.matches.append(match)
        print(f"Scheduled match: {team1.name} vs {team2.name}")

    def play_matches(self):
        """Play all scheduled matches."""
        for match in self.matches:
            match.play_match()