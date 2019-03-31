#!python3

import pygame as pg, random

class Character(pg.sprite.Sprite):
    """ Super class for all character entities in the game"""
    def __init__(self,display, centerx, bottom,moving_left, moving_right, speed):
        super(Character,self).__init__()
        self.display = display
        self.display_rect = display.get_rect()

        # load entity image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/alien_ship_charged.png")

        # rect size
        self.rect = self.image.get_rect()

        #set starting position
        self.rect.centerx = centerx
        self.rect.bottom = bottom 

        #movement 
        self.moving_left = moving_left
        self.moving_right = moving_right
        self.speed = speed

    def blit_self(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)

    def move_self(self):
        """ move the entity to a new position"""
        if self.moving_right and self.rect.right <= (self.display_rect.right - 6):
            self.rect.centerx += self.speed
        if self.moving_left and self.rect.left >= 6:
            self.rect.centerx -= self.speed
