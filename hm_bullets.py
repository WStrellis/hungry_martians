#!python3

import pygame as pg, random

class Bullet(pg.sprite.Sprite):
    """ Bullets from farmers"""
    def __init__(self,display,farmer):
        super(Bullet, self).__init__()
        """initialize a bullet"""
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/hm_bullet.png").convert_alpha()

        # starting position
        self.rect = farmer.farmer_aim()

        #set bullet starting position
        # self.rect.centerx = 500
        # self.rect.centery = 400 

        #movement 
        self.speed = 20 

    def blit_bullet(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)

    