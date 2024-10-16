class Team:
    def __init__(self, name):

        self.name = name # A team has a name
        self.brawlers = [] # And has brawlers
        self.max_brawlers = 3 # But a team cannot exceed 3 brawlers
    
    def add_player(self, brawler):
        ''' 
        Method to add a brawler in a Team
        '''
        self.brawlers.append(brawler) 

