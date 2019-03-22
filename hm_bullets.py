#!python3

import pygame as pg, random

class Bullet(pg.sprite.Sprite):
    """ Bullets from farmers"""
    def __init__(self,start_pos,display):
        super(Bullet, self).__init__()
        """initialize a bullet"""
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/hm_bullet.png").convert_alpha()

        # starting position
        self.rect = list(start_pos)

        #movement 
        self.speed = 15 

    def move_bullet(self):
        """move the bullet"""
        self.rect[1] -= self.speed

    def blit_bullet(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)

    