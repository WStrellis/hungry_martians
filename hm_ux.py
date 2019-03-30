#!python3

import pygame as pg
import pygame.font

class UXcomponent(pg.sprite.Sprite):
    """A class to manage the menus"""

    def __init__(self, display, image, width, height, centerx, bottom):
        super().__init__()
        """initialize game settings"""
        #game display
        self.display = display
        self.display_rect = display.get_rect()

        # set image 
        self.image = image

     # rect size
        # self.rect = self.image.get_rect()
        self.rect = pg.Rect(0,0, width, height)

        #set starting position
        self.rect.centerx = centerx
        self.rect.bottom = bottom 

    def blit_self(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)

class ShieldIcon(UXcomponent):
    """ a class for the shield indicator"""
    def __init__(self,display,image, width, height, centerx,bottom):
        super().__init__(display,image, width, height, centerx,bottom)

    def setImage(self,ship_hp):
        """ change the shield color based on ship hp"""
        tag = 's' + str(ship_hp)
        shields = {
        's3' : "D:/Python/hungry_martians/green_shield.png",
        's2' : "D:/Python/hungry_martians/yellow_shield.png",
        's1' : "D:/Python/hungry_martians/orange_shield.png",
        's0': "D:/Python/hungry_martians/red_shield.png"
        }
        if ship_hp >= 0 :
            self.image = pg.image.load(shields[tag])

class Text(UXcomponent):
    """ A class for displaying text on the screen"""

    def __init__(self,display,image, width, height, centerx, bottom, msg):
        super().__init__(display,image, width, height, centerx, bottom)

        self.font = pg.font.SysFont(None, 48)
        self.msg = msg
