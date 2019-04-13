#!python3

import pygame as pg
from hm_characters import Character

class Ship(Character):
    """ a class for the player's ship"""
    def __init__(self,display,centerx,bottom,moving_left,moving_right,speed,hp):
        super().__init__(display,centerx,bottom,moving_left,moving_right,speed)
        """attributes for the player's ship""" 
        self.ufo_charged = pg.image.load("D:/Python/hungry_martians/alien_ship_charged.png")
        self.ufo_reloading = pg.image.load("D:/Python/hungry_martians/alien_ship_reloading.png")

        self.img = self.ufo_charged

        #health
        self.hp = hp

        # attributes to track tractor beam status
        # the player can't fire the beam if charged is false
        self.charged = True
        self.chargingTimer = 0

        self.beamSound = pg.mixer.Sound("ani-music__massive-laser-blast-laser2.wav")
        self.damageSound = pg.mixer.Sound("danielnieto7__alert.wav")

    def fire_tb(self, tb):
        """ shoot the tractor beam"""
        self.beamSound.play()
        #change the image of the ship to 'charging'
        self.image = self.ufo_reloading

        # set charging timer to 3 seconds
        self.chargingTimer = 90
        self.charged = False

        # center tb under ship
        tb.rect.centerx = self.rect.centerx

        # set tractor beam lifespan to 15
        tb.lifespan = tb.maxlife

    
    def chargeBeam(self):
        """ reduce tb_timer by 1 each time though the game loop"""
        if self.chargingTimer > 0:
            self.chargingTimer -= 1
        else:
            self.image = self.ufo_charged
            self.charged = True

    def resetHP(self):
        """ reset hp to 3"""
        self.hp = 3

    def damageTaken(self):
        """ play a sound when the ship takes damage"""
        self.damageSound.play(maxtime=1000)

class TBeam(pg.sprite.Sprite):
    """ class to make tracor beams"""
    def __init__(self,display, centerx, top, maxlife):
        super(TBeam,self).__init__()
        self.display = display
        self.display_rect = display.get_rect()

        # load entity image 
        self.image = pg.image.load("D:/Python/hungry_martians/tractor_beam.png")

        # rect size
        self.rect = self.image.get_rect()

        #set starting position
        self.rect.centerx = centerx
        self.rect.top = top 
        
        # controls how long to blit the beam
        self.maxlife = maxlife
        self.lifespan = 0

    def blit_self(self):
        """ draw entity onto the screen"""
        self.lifespan -= 1
        self.display.blit(self.image,self.rect)
