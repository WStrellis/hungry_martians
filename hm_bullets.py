#!python3

import pygame as pg
from hm_characters import Character

class Bullet(Character):
    """ a class for bullets"""
    def __init__(self, display, centerx, bottom, moving_left, moving_right, speed):
        super().__init__(display, centerx, bottom, moving_left, moving_right, speed)

        self.image = pg.image.load("hm_bullet.png")

    def move_self(self):
        """move the bullet"""
        self.rect.bottom -= self.speed
