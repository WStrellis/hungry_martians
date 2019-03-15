#!python3

import pygame as pg

class Cow():
    """ Cows!! """
    def __init__(self,display):
        """initialize a cow"""
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/cow_right.png").convert_alpha()

        # starting position
        self.rect = self.image.get_rect()

        #set cow starting position
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = 750 


        #movement flags
        self.moving_right = True
        self.moving_left = False
        self.speed = 5

    def blit_cow(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)
 
    def move_cow(self):
        if self.moving_right:
            self.image = pg.image.load("D:/Python/hungry_martians/cow_right.png").convert_alpha()
            if self.rect.right <= 994:
                self.rect.centerx += self.speed
            else:
                self.moving_right = False
                self.moving_left = True
        if self.moving_left:
            self.image = pg.image.load("D:/Python/hungry_martians/cow_left.png").convert_alpha()
            if self.rect.left >= 6:
                self.rect.centerx -= self.speed
            else:
                self.moving_right = True
                self.moving_left = False