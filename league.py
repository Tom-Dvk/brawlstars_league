######################################
##  This script define the league   ##
######################################


# First Class define a game
class Game:
    def __init__(self, team1, team2):

        self.equipe1 = team1 # We define a game by confronting two teams
        self.equipe2 = team2
    
    def play_game(self): # 
        '''
        The method to play the game and return a winner 
        '''

        ## we have to define how a match is win for a team. Using specificities of brawlers and teams.
        return None
    
class Tournament:
    def __init__(self, teams):

        self.teams = teams # Contains all the teams that are playing the tournament

    def simulate(self):
        '''
        This function simulate the whole tournament, and return the team of the winners
        '''
        return None