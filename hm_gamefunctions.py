#!python3

import sys, pygame as pg
from pygame.locals import *

def init_stats(settings, ship, shield):
    """ reset everything to the start value"""
    settings.level = 0
    ship.hp = 3
    shield.setImage(ship.hp)

def move_farmers(farmers):
    """ move each farmer"""
    for f in farmers:
        f.move_self()

def farmer_shoot(farmers,display,bullets):
    """ call shoot for each farmer"""
    for f in farmers:
        if f.move_tracker == f.shot_trigger:
            f.shoot(display,bullets)
            f.move_tracker = 0

def move_bullet(bullets):
    """move each bullet"""
    for b in bullets:
        b.move_self()
    # remove bullets that have left the screen
    for b in bullets.copy():
        if b.rect[1] <= 0:
            bullets.remove(b)

def ship_hit(ship,bullets,shield, gameState):
    """ Check if the player's ship has been hit by farmer's bullets"""
    if pg.sprite.spritecollideany(ship,bullets):
        # subtract 1 hp from the ship
        ship.hp -= 1
        # update the shield icon
        shield.setImage(ship.hp)
        #delete all bullets
        for b in bullets.copy():
            b.kill()
        if ship.hp < 0:
                gameState.state = "gameover"


def player_movement(player):
    """ check the players movement flags and move the player"""
    if player.moving_right == True: 
        player.move_self()
    if player.moving_left == True: 
        player.move_self()

def check_events(player,settings,ngUX,goUX, shield):
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

        #start the game when the player clicks "play"
        if settings.state in ['newgame','gameover','level']:
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()

                if settings.state == 'newgame':
                    playButton = ngUX[1]
                    quitButton = ngUX[2]
                    playGame(mouse_x,mouse_y,settings, playButton,quitButton)

                if settings.state == 'gameover':
                    resetButton = ngUX[1]
                    quitButton = ngUX[2]
                    resetGame(mouse_x,mouse_y,settings, resetButton,quitButton, player, shield)

                if settings.state == 'level':
                    pass

def playGame(mouse_x, mouse_y, gameState, play_button,quit_button):
    """ start the game if the player clicks the mouse button"""
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        gameState.state = "running"
    if quit_button.rect.collidepoint(mouse_x,mouse_y):
      quitGame() 

def resetGame(mouse_x, mouse_y, gameState, reset_button,quit_button, player,shield):
    """ reset game settings to initial values"""
    if reset_button.rect.collidepoint(mouse_x,mouse_y):
        init_stats(gameState, player,shield)
        gameState.state = "running"
    if quit_button.rect.collidepoint(mouse_x,mouse_y):
      quitGame() 


def quitGame():
    """ quit the game if the player clicks the quit button"""
    pg.quit()
    sys.exit()

def update_characters(gameSettings, gameDisplay, player,cow,farmers,bullets,shield):
    """ update images on the screen and draw new screen"""
    gameDisplay.fill(gameSettings.bg_color)
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    player.blit_self()
    for f in farmers:
        f.blit_self()
    cow.blit_self()
    for b in bullets:
        b.blit_self()
    shield.blit_self()

    pg.display.update()

def newgame(gameSettings,gameDisplay,newgameUX):
    """ methods for newgame state"""
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    for n in newgameUX:
        n.blit_self()

    pg.display.update()

def gameover(gameSettings,gameDisplay,gameoverUX):
    """ methods for gameover state"""
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    for g in gameoverUX:
        g.blit_self()

    pg.display.update()
