#!python3

from hm_characters import Character

class Cow(Character):
    """ a class for cows"""
    def __init__(self,display,image,centerx,bottom,moving_left,moving_right,speed,imgLeft,imgRight):
        super().__init__(display,image,centerx,bottom,moving_left,moving_right,speed,imageLeft=imgLeft,imageRight=imgRight)
        """attributes for the cow""" 

    def move_self(self):
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
