#!python3

import pygame as pg

class Ship():
    """ The player controlled space ship"""
    def __init__(self,display):
        """ initialize ship""" 
        self.display = display
        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/alien_ship.png").convert_alpha()
        # starting position
        self.rect = self.image.get_rect()
        self.display_rect = display.get_rect()

        #set ship starting position
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = 200 

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.speed = 10
        
        #health
        self.hp = 3

    def blit_ship(self):
        """ draw ship at its current location"""
        self.display.blit(self.image,self.rect)

    def move_ship(self):
        """ move the ship on the screen"""
        if self.moving_right and self.rect.right <= 994:
            self.rect.centerx += self.speed
        if self.moving_left and self.rect.left >= 6:
            self.rect.centerx -= self.speed

class Cow():
    """ Cows!! """
    def __init__(self,display):
        """initialize a cow"""
        self.display = display
        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/cow.png").convert_alpha()
        # starting position
        self.rect = self.image.get_rect()
        self.display_rect = display.get_rect()

        #set cow starting position
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = 750 

        #movement flags
        self.moving_right = True
        self.moving_left = False
        self.speed = 5

    def blit_cow(self):
        """ draw ship at its current location"""
        self.display.blit(self.image,self.rect)

    def move_cow(self):
        """ move the cow on the screen"""
        if self.moving_right:
            if self.rect.right <= 994:
                self.rect.centerx += self.speed
            else:
                self.moving_right = False
                self.moving_left = True
        if self.moving_left:
            if self.rect.left >= 6:
                self.rect.centerx -= self.speed
            else:
                self.moving_right = True
                self.moving_left = False
