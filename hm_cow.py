#!python3

import pygame as pg
from hm_animal import Animal

class Cow(Animal):
    """ a class for cows"""
    def __init__(self,display,centerx,bottom,moving_left,moving_right,speed, imageLeft, imageRight, sound):
        super().__init__(display,centerx,bottom,moving_left,moving_right,speed, imageLeft, imageRight, sound)
        """attributes for the cow""" 
