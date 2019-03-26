#!python3

from hm_characters import Character

class Ship(Character):
    """ a class for the player's ship"""
    def __init__(self,display,image,centerx,bottom,moving_left,moving_right,speed,hp):
        super().__init__(display,image,centerx,bottom,moving_left,moving_right,speed)
        """attributes for the player's ship""" 

        #health
        self.hp = hp
