#!python3

import sys, pygame as pg
from pygame.locals import *

def player_movement(player):
    """ check the players movement flags and move the player"""
    if player.moving_right == True: 
        player.move_ship()
    if player.moving_left == True: 
        player.move_ship()

def check_events(player):
    """Respond to key presses and events"""
    for event in pg.event.get():
        if event.type == QUIT or (event.type== KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player.moving_right = True
            if event.key == K_LEFT:
                player.moving_left = True

        elif event.type == KEYUP :
            if event.key == K_RIGHT: 
                player.moving_right = False
            elif event.key == K_LEFT: 
                player.moving_left = False

def update_screen(gameSettings, gameDisplay, player,cow,farmer,bullet):
    """ update images on the screen and draw new screen"""
    gameDisplay.fill(gameSettings.bg_color)
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    player.blit_ship()
    farmer.blit_farmer()
    cow.blit_cow()
    bullet.blit_bullet()
    pg.display.update()