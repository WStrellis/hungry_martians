#!python3

import pygame as pg

class Settings():
    """A class to store all settings"""

    def __init__(self):
        """initialize game settings"""
        #game display
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (0,230,230)
        self.fps = 30
        self.bg_image = pg.image.load("D:/Python/hungry_martians/farm.png")
