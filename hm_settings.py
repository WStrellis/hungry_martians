#!python3

import pygame as pg
from hm_ship import Ship, TBeam
from hm_cow import Cow
from hm_farmer import Farmer
from hm_bullets import Bullet
from hm_ux import UXcomponent,ShieldIcon, Text

class Settings():
    """A class to store all settings"""

    def __init__(self):
        """initialize game settings"""
        #game display
        self.screen_width = 1000
        self.screen_height = 800
        self.gameDisplay = pg.display.set_mode((self.screen_width, self.screen_height))
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

        self.titleImg = pg.image.load("D:/Python/hungry_martians/title.png")

        self.playImg = pg.image.load("D:/Python/hungry_martians/play_button.png")
        self.quitImg = pg.image.load("D:/Python/hungry_martians/quit_button.png")
        self.nextImg = pg.image.load("D:/Python/hungry_martians/next_button.png")
        self.restartImg = pg.image.load("D:/Python/hungry_martians/restart_button.png")
        self.huntImg = pg.image.load("D:/Python/hungry_martians/hunt_button.png")

        self.greenShield = pg.image.load("D:/Python/hungry_martians/green_shield.png")

        # ux components
        self.shield_indicator = ShieldIcon(self.gameDisplay,self.greenShield, 31, 35, 35, 75)

        self.title = UXcomponent(self.gameDisplay,self.titleImg, 513, 141, 500,340)

        self.playButton = UXcomponent(self.gameDisplay,self.playImg, 173, 159,500,500)
        self.restartButton = UXcomponent(self.gameDisplay, self.restartImg, 173, 159,500,500)
        self.quitButton = UXcomponent(self.gameDisplay, self.quitImg, 173, 159, 500, 700)

        # start level screen components
        self.levelHeading = Text(self.gameDisplay, 120, 500, 340, self.light_orange, "Farm {0}".format(self.level))
        self.huntButton = UXcomponent(self.gameDisplay, self.huntImg, 173, 159,500,500)

        # end level screen components
        self.goodJob = Text(self.gameDisplay, 120, 500, 240, self.light_orange, "Good Job!")
        self.endMsg = Text(self.gameDisplay, 120, 500, 340, self.light_orange, "All animals abducted!")
        self.nextButton = UXcomponent(self.gameDisplay, self.nextImg, 173, 159,500,500)

        # group for new game menu components
        self.newgameUX = [self.title, self.playButton, self.quitButton]
        
        # group for start level screen components
        self.startUX = [self.levelHeading, self.huntButton]

        # group for start level screen components
        self.endUX = [self.goodJob, self.endMsg, self.nextButton]

        # group for game over menu components
        self.gameoverUX = [self.title, self.restartButton, self.quitButton]
        
        

    def currentLVL(self):
        """ update the level message"""
        msg = "Farm {0}".format(self.level)
        return msg
