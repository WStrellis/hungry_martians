#!python3

import pygame as pg, random

class Farmer():
    """ Farmers"""
    def __init__(self,display):
        """initialize a cow"""
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/farmer_left.png").convert_alpha()

        # starting position
        self.rect = self.image.get_rect()

        #set farmer starting position
        self.rect.centerx = random.randint(20,970)
        self.rect.bottom = 750 

        #movement flags
        self.moving_right = True
        self.moving_left = False
        self.speed = 3

    def blit_farmer(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)

    def move_farmer(self):
        if self.moving_right:
            self.image = pg.image.load("D:/Python/hungry_martians/farmer_right.png").convert_alpha()
            if self.rect.right <= 994:
                self.rect.centerx += self.speed
            else:
                self.moving_right = False
                self.moving_left = True
        if self.moving_left:
            self.image = pg.image.load("D:/Python/hungry_martians/farmer_left.png").convert_alpha()
            if self.rect.left >= 6:
                self.rect.centerx -= self.speed
            else:
                self.moving_right = True
                self.moving_left = False

    