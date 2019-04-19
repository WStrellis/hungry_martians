#!python3

import pygame as pg
from hm_characters import Character
from hm_bullets import Bullet

class Farmer(Character):
    """ Class for Farmers"""

    def __init__(self, display, centerx, bottom, moving_left, moving_right, speed, shot_trigger):
        super().__init__(display, centerx, bottom, moving_left, moving_right, speed)

        self.farmerLeft = pg.image.load("farmer_left.png")
        self.farmerRight = pg.image.load("farmer_right.png")

        if self.moving_left:
            self.image = self.farmerLeft
        else: 
            self.image = self.farmerRight

        self.shot_trigger = shot_trigger
        self.move_tracker = 0

    def move_self(self):
        if self.moving_right:
            self.image = self.farmerRight
            if self.rect.right <= (self.display_rect.right - 6):
                self.rect.centerx += self.speed
            else:
                self.moving_right = False
                self.moving_left = True
        if self.moving_left:
            self.image = self.farmerLeft
            if self.rect.left >= 6:
                self.rect.centerx -= self.speed
            else:
                self.moving_right = True
                self.moving_left = False

        # used to trigger when the farmer shoots
        self.move_tracker += 1
    
    def farmer_aim(self):
        """ return the coordinates of the barrel of the 
        gun so that bullets can be properly positioned"""
        if self.moving_left:
            return list(self.rect.topleft)
        elif self.moving_right:
            return list(self.rect.topright)

    def shoot(self,display,bullets):
        """ create a bullet""" 
        bullet_start = self.farmer_aim()
        new_bullet = Bullet(display, bullet_start[0], bullet_start[1], 0, 0, 15)
        bullets.add(new_bullet)
