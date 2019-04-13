#!python3

import pygame as pg, random

class Animal(pg.sprite.Sprite):
    """ Super class for all animals in the game"""
    def __init__(self,display, centerx, bottom,moving_left, moving_right, speed, imageLeft, imageRight, sound):
        super(Animal,self).__init__()

        self.display = display
        self.display_rect = display.get_rect()

        self.imageLeft = imageLeft
        self.imageRight = imageRight

        self.captured = False

        self.animalSound = sound

        # rect size
        self.rect = self.imageLeft.get_rect()

        #set starting position
        self.rect.centerx = centerx
        self.rect.bottom = bottom 

        #movement 
        self.moving_left = moving_left
        self.moving_right = moving_right
        self.speed = speed

        if self.moving_left:
            self.image = self.imageLeft
        else: 
            self.image = self.imageRight

    def blit_self(self):
        """ draw entity onto the screen"""
        self.display.blit(self.image,self.rect)

    def move_self(self):
        if self.captured:
            self.rect.bottom -= 5
        else:
            if self.moving_right:
                self.image = self.imageRight
                if self.rect.right <= (self.display_rect.right - 6):
                    self.rect.centerx += self.speed
                else:
                    self.moving_right = False
                    self.moving_left = True
            if self.moving_left:
                self.image = self.imageLeft
                if self.rect.left >= 6:
                    self.rect.centerx -= self.speed
                else:
                    self.moving_right = True
                    self.moving_left = False

    def speak(self):
        """ play the animal's sound"""
        self.animalSound.play() 
