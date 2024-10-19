from league import League
from team import Team
from brawler import Brawler

def run_league():
    # Initialize your league
    league = League()
    
    # Add some teams (assuming Team is a class)
    team1 = Team(name="Team A")
    team2 = Team(name="Team B")
    
    # Add teams to the league
    league.add_team(team1)
    league.add_team(team2)
    
    # Run a sample match (or the league season)
    league.run_season()

if __name__ == "__main__":
    # Entry point to start the league simulation
    run_league()
