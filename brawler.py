# FIle used for the brawler

class Brawler:
    def __init__(self,name,speed,damage_nattack,distance,reload_speed,super_damage,super_range):

        # health and speed of the brawler
        self.name = name 
        self.speed = speed

        # his normal attack
        self.damage_nattack = damage_nattack
        self.distance = distance
        self.reload_speed = reload_speed

        # his super attack
        self.super_damage = super_damage
        self.super_range = super_range

    def normal_attack(self): 
        '''
        Method that define the normal attack of a brawler
        '''
        return self.damage_nattack

    def super_attack(self):
        '''
        Method that define the super attack of a brawler
        '''
        return self.super_damage