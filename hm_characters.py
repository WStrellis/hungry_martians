#!python3

import pygame as pg, random 

class Entity():
    """ The base class for all game entities"""
    def __init__(self,display):
        """attributes of all entities""" 

        # display attributes
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        # self.image = ''
        self.image = pg.image.load("D:/Python/hungry_martians/alien_ship.png").convert_alpha()

        # current location and size
        self.rect = self.image.get_rect()

        #set  starting position
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = 0 

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.speed = 1

    def blit_entity(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)
 
    def move_entity(self):
            """ move the entity on to a different location"""
            if isinstance(self,Ship):
                if self.moving_right and self.rect.right <= 994:
                    self.rect.centerx += self.speed
                if self.moving_left and self.rect.left >= 6:
                    self.rect.centerx -= self.speed
            # if isinstance(self,(Cow,Farmer)):
            else:
                if self.moving_right:
                    if self.rect.right <= 994:
                        self.rect.centerx += self.speed
                    else:
                        self.moving_right = False
                        self.moving_left = True
                if self.moving_left:
                    if self.rect.left >= 6:
                        self.rect.centerx -= self.speed
                    else:
                        self.moving_right = True
                        self.moving_left = False

class Ship(Entity):
    """ The player controlled space ship"""
    def __init__(self,display):
        """ initialize ship""" 
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/alien_ship.png").convert_alpha()

        # current location and size
        self.rect = self.image.get_rect()

        #set ship starting position
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = 200 

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.speed = 10
        
        #health
        self.hp = 3

   
class Cow(Entity):
    """ Cows!! """
    def __init__(self,display):
        """initialize a cow"""
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/cow.png").convert_alpha()

        # starting position
        self.rect = self.image.get_rect()

        #set cow starting position
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = 750 

        #movement flags
        self.moving_right = True
        self.moving_left = False
        self.speed = 5
    
class Farmer(Entity):
    """ Farmers"""
    def __init__(self,display):
        """initialize a cow"""
        self.display = display
        self.display_rect = display.get_rect()

        # load player image get its rect
        self.image = pg.image.load("D:/Python/hungry_martians/farmer_left.png").convert_alpha()

        # starting position
        self.rect = self.image.get_rect()

        #set farmer starting position
        self.rect.centerx = random.randint(20,970)
        self.rect.bottom = 750 

        #movement flags
        self.moving_right = True
        self.moving_left = False
        self.speed = 5

  