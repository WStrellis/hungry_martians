#!python3

import pygame as pg, random

class Farmer(pg.sprite.Sprite):
    """ Bullets from farmers"""
    def __init__(self,display):
        super(Farmer, self).__init__()
        """initialize a farmer"""
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/farmer_right.png").convert_alpha()

        # starting position
        self.rect = self.image.get_rect()

        #set farmer starting position
        self.rect.centerx = random.randint(20,970)
        self.rect.bottom = 750 

        #movement 
        self.moving_right = True
        self.moving_left = False
        self.speed = 3

        self.shot_trigger = 3
        self.move_tracker = 0

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

        self.move_tracker += 1

    def farmer_aim(self):
        """ return the coordinates of the barrel of the 
        gun so that bullets can be properly positioned"""
        if self.moving_left:
            return self.rect.topleft
        elif self.moving_right:
            return self.rect.topright

    