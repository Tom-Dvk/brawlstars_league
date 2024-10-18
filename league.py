######################################
##  This script define the league   ##
######################################

from typing import List, Union, Dict

# First Class define a game
class Game:
    def __init__(self, team1: List[str], team2: List[str]) -> None:
        self.team1 = team1
        self.team2 = team2
    
    def play_game(self, teams: Dict{List[str]}, mode={}) -> Union[str, None]: 
        '''
        The method to play the game and return a winner 
        '''

        ## we have to define how a match is win for a team. Using specificities of brawlers and teams.
        return None
    
    def get_results(self, play_game):
        score = play_game(self.)
        print()
    
class Tournament:
    def __init__(self, teams):

        self.teams = teams # Contains all the teams that are playing the tournament

    def simulate(self):
        '''
        This function simulate the whole tournament, and return the team of the winners
        '''
        return None