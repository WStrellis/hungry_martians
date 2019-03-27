#!python3

import pygame as pg

class UX():
    """A class to manage the menus"""

    def __init__(self):
        """initialize game settings"""
        #game display
        self.green_sheild = pg.image.load("D:/Python/hungry_martians/green_shield.png")
        self.yellow_shield = pg.image.load("D:/Python/hungry_martians/yellow_shield.png")
        self.orange_shield = pg.image.load("D:/Python/hungry_martians/orange_shield.png")
        self.red_sheild = pg.image.load("D:/Python/hungry_martians/red_shield.png")
