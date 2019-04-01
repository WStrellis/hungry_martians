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

        # group for all animals
        self.animals = pg.sprite.Group()

        #used to track captured animals
        self.captured = 0 

        # ux components
        self.bright_green = (61, 235, 98) 
        self.light_orange = (255, 106, 54)

        self.title = pg.image.load("D:/Python/hungry_martians/title.png")

        self.playButton = pg.image.load("D:/Python/hungry_martians/play_button.png")
        self.quitButton = pg.image.load("D:/Python/hungry_martians/quit_button.png")
        self.nextButton = pg.image.load("D:/Python/hungry_martians/next_button.png")
        self.restartButton = pg.image.load("D:/Python/hungry_martians/restart_button.png")
        self.huntButton = pg.image.load("D:/Python/hungry_martians/hunt_button.png")

        self.green_shield = pg.image.load("D:/Python/hungry_martians/green_shield.png")
    
        

    def currentLVL(self):
        """ update the level message"""
        msg = "Farm {0}".format(self.level)
        return msg
