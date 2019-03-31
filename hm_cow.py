#!python3

import pygame as pg
from hm_characters import Character

class Cow(Character):
    """ a class for cows"""
    def __init__(self,display,centerx,bottom,moving_left,moving_right,speed):
        super().__init__(display,centerx,bottom,moving_left,moving_right,speed)
        """attributes for the cow""" 
        self.cowLeft = pg.image.load("D:/Python/hungry_martians/cow_left.png")
        self.cowRight = pg.image.load("D:/Python/hungry_martians/cow_right.png")

        self.captured = False

        if self.moving_left:
            self.image = self.cowLeft
        else: 
            self.image = self.cowRight

    def move_self(self):
        if self.captured:
            self.rect.bottom -= 5
        else:
            if self.moving_right:
                self.image = self.cowRight
                if self.rect.right <= (self.display_rect.right - 6):
                    self.rect.centerx += self.speed
                else:
                    self.moving_right = False
                    self.moving_left = True
            if self.moving_left:
                self.image = self.cowLeft
                if self.rect.left >= 6:
                    self.rect.centerx -= self.speed
                else:
                    self.moving_right = True
                    self.moving_left = False
