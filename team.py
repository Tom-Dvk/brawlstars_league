# File for the team class
import random
import json

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.brawlers = []  # List of Brawlers on the team

    def add_brawler(self, brawler):
        """Add a Brawler to the team."""
        if len(self.brawlers) < 3:
            self.brawlers.append(brawler)
        else:
            print(f"Team {self.team_name} already has 3 Brawlers!")

    def remove_brawler(self, brawler_name):
        """Remove a Brawler from the team by name."""
        self.brawlers = [b for b in self.brawlers if b['name'] != brawler_name]

    def display_team(self):
        """Display the current team setup."""
        print(f"Team {self.team_name}:")
        for b in self.brawlers:
            print(f" - {b['name']} (Role: {b['role']}, Health: {b['basics']['health']}, Attack Damage: {b['attack']['damage']}, , Trophies: {b.get('trophies', 0)})")

    def total_trophies(self):
        """Calculate the total trophies for the team."""
        return sum(b.get('trophies', 0) for b in self.brawlers)

    @staticmethod
    def load_brawlers(file_path):
        """Load Brawler data from a JSON file."""
        with open(file_path, 'r') as f:
            return json.load(f)
    
    @staticmethod
    def load_trophies(file_path):
        """Load Brawler trophies from a JSON file."""
        with open(file_path, 'r') as f:
            return json.load(f)

    @classmethod
    def create_balanced_teams(cls, team_names, brawler_data, trophies_data):
        """Create balanced teams based on Brawlers' trophies."""
        # Combine brawler data with their respective trophies
        brawlers = []
        for brawler_name, brawler_info in brawler_data.items():
            brawler_info['trophies'] = trophies_data.get(brawler_name, 0)  # Default to 0 trophies if not found
            brawlers.append(brawler_info)
        
        # Sort Brawlers by trophies in descending order
        brawlers.sort(key=lambda x: x['trophies'], reverse=True)

        # Create empty teams
        teams = {team_name: cls(team_name) for team_name in team_names}

        # Distribute Brawlers to teams in a balanced way (round-robin style)
        team_names_cycle = iter(team_names * (len(brawlers) // len(team_names) + 1))
        for brawler in brawlers:
            team_name = next(team_names_cycle)
            teams[team_name].add_brawler(brawler)

        return teams

if __name__ == "__main__":
    # Load Brawlers and trophies from JSON files (replace with your file paths)
    brawler_data = Team.load_brawlers('data/brawlers_data.json')
    trophies_data = Team.load_trophies('data/brawlers_trophies.json')

    # Create balanced teams
    team_names = ["Team A", "Team B"]
    teams = Team.create_balanced_teams(team_names, brawler_data, trophies_data)

    # Display teams
    for team in teams.values():
        team.display_team()
        print(f"Total Trophies for {team.team_name}: {team.total_trophies()}\n")
