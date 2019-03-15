#!python3

import pygame as pg

class Ship():
    """ a class for the player's ship"""
    def __init__(self,display):
        """attributes for the player's ship""" 

        # display attributes
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        # self.image = ''
        self.image = pg.image.load("D:/Python/hungry_martians/alien_ship.png").convert_alpha()

        # current location and size
        self.rect = self.image.get_rect()

        #set  starting position
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = 200 

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.speed = 10

        #health
        self.hp = 3


    def blit_ship(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)
 
    def move_ship(self):
        if self.moving_right and self.rect.right <= 994:
            self.rect.centerx += self.speed
        if self.moving_left and self.rect.left >= 6:
            self.rect.centerx -= self.speed
   