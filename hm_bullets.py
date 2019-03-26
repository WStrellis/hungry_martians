#!python3

from hm_characters import Character
from hm_settings import Settings

class Bullet(Character):
    # used to access the bullet image
    gs = Settings()
    """ a class for the player's ship"""
    def __init__(self, display, image, centerx, bottom, moving_left, moving_right, speed):
        super().__init__(display, image, centerx, bottom, moving_left, moving_right, speed)

    def move_self(self):
        """move the bullet"""
        self.rect.bottom -= self.speed
