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
        
        # game state
        self.state = 'newgame'

        # level tracker
        self.level = 1

        #character images
        self.ufo = pg.image.load("D:/Python/hungry_martians/alien_ship.png")

        self.cow_left = pg.image.load("D:/Python/hungry_martians/cow_left.png")
        self.cow_right = pg.image.load("D:/Python/hungry_martians/cow_right.png")

        self.farmer_left = pg.image.load("D:/Python/hungry_martians/farmer_left.png")
        self.farmer_right = pg.image.load("D:/Python/hungry_martians/farmer_right.png")

        self.bullet_img = pg.image.load("D:/Python/hungry_martians/hm_bullet.png")

        # ux components
        self.title = pg.image.load("D:/Python/hungry_martians/title.png")
        self.playButton = pg.image.load("D:/Python/hungry_martians/play_button.png")
        self.quitButton = pg.image.load("D:/Python/hungry_martians/quit_button.png")
        self.restartButton = pg.image.load("D:/Python/hungry_martians/restart_button.png")
        self.green_shield = pg.image.load("D:/Python/hungry_martians/green_shield.png")
