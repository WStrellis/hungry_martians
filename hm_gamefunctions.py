#!python3

import sys, pygame as pg
from pygame.locals import *

def move_farmers(farmers):
    """ move each farmer"""
    for f in farmers:
        f.move_farmer()

def farmer_shoot(farmers,display,bullets):
    """ call shoot for each farmer"""
    for f in farmers:
        if f.move_tracker == f.shot_trigger:
            f.shoot(display,bullets)
            f.move_tracker = 0

def move_bullet(bullets):
    """move each bullet"""
    for b in bullets:
        b.move_bullet()
    # remove bullets that have left the screen
    for b in bullets.copy():
        if b.rect[1] <= 0:
            bullets.remove(b)

def player_movement(player):
    """ check the players movement flags and move the player"""
    if player.moving_right == True: 
        # player.move_ship()
        player.move_self()
    if player.moving_left == True: 
        # player.move_ship()
        player.move_self()

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

def update_screen(gameSettings, gameDisplay, player,cow,farmers,bullets):
    """ update images on the screen and draw new screen"""
    gameDisplay.fill(gameSettings.bg_color)
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    player.blit_self()
    for f in farmers:
        f.blit_farmer()
    cow.blit_self()
    for b in bullets:
        b.blit_bullet()
    pg.display.update()
