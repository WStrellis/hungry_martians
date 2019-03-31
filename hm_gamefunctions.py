#!python3

import sys, pygame as pg
from pygame.locals import *
from hm_ux import Text

def init_stats(settings, ship, shield):
    """ reset everything to the start value"""
    settings.level = 1
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

def check_events(player,settings,ngUX,goUX, shield, lvlUX, tb):
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
            if event.key == K_SPACE and player.charged == True:
                player.fire_tb(tb)

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
                    resetButton = goUX[1]
                    quitButton = goUX[2]
                    resetGame(mouse_x,mouse_y,settings, resetButton,quitButton, player, shield)

                if settings.state == 'level':
                    huntButton = lvlUX[1]
                    startLevel(mouse_x,mouse_y,settings, huntButton)

def playGame(mouse_x, mouse_y, settings, play_button,quit_button):
    """ start the game if the player clicks the mouse button"""
    if play_button.rect.collidepoint(mouse_x,mouse_y) and play_button.onscreen == True:
        settings.state = "level"
        play_button.onscreen = False
    if quit_button.rect.collidepoint(mouse_x,mouse_y) and quit_button.onscreen == True:
      quitGame() 

def startLevel(mouse_x, mouse_y, settings, hunt_button):
    """ start the round if the player clicks the mouse button"""
    if hunt_button.rect.collidepoint(mouse_x,mouse_y) and hunt_button.onscreen == True:
        settings.state = "running"
        hunt_button.onscreen = False

def resetGame(mouse_x, mouse_y, settings, reset_button,quit_button, player,shield):
    """ reset game settings to initial values"""
    if reset_button.rect.collidepoint(mouse_x,mouse_y) and reset_button.onscreen == True:
        init_stats(settings, player,shield)
        settings.state = "level"
        reset_button.onscreen = False
    if quit_button.rect.collidepoint(mouse_x,mouse_y) and quit_button.onscreen == True:
      quitGame() 


def quitGame():
    """ quit the game if the player clicks the quit button"""
    pg.quit()
    sys.exit()

def update_characters(gameSettings, gameDisplay, player,cow,farmers,bullets,shield,tb):
    """ update images on the screen and draw new screen"""
    gameDisplay.fill(gameSettings.bg_color)
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    player.blit_self()
    for f in farmers:
        f.blit_self()
    cow.blit_self()
    # used to control how long the tb is displayed on the screen
    if tb.lifespan > 0:
        tb.blit_self()
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

def levelIntro(gameSettings,gameDisplay, lvlUX):
    """ methods for newgame state"""
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    for i in lvlUX:
        if isinstance(i, Text):
            currLVL = gameSettings.currentLVL()
            i.msg = currLVL
        i.blit_self()

    pg.display.update()

def gameover(gameSettings,gameDisplay,gameoverUX):
    """ methods for gameover state"""
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    for g in gameoverUX:
        g.blit_self()

    pg.display.update()
