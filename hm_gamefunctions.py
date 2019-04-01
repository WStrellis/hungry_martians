#!python3

import sys, pygame as pg
from pygame.locals import *
from hm_ux import Text

def init_stats(settings, ship, shield):
    """ reset everything to the start value"""
    settings.level = 1
    ship.hp = 3
    settings.captured = 0
    settings.state = "startLevel"
    shield.setImage(ship.hp)

def levelComplete(settings):
    """ if all animals are captured go the the next level"""
    if len(settings.animals) == settings.captured:
        settings.state = "endLevel"
        settings.level += 1

def move_farmers(farmers):
    """ move each farmer"""
    for f in farmers:
        f.move_self()

def move_animals(animals):
    """ move each cow"""
    for a in animals:
        if a.rect.bottom >550:
            a.move_self()

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
    
def animals_hit(beam, settings):
    """ determine if animals have been shot by the laser"""
    animalsHit = pg.sprite.spritecollide(beam, settings.animals, False)
    for a in animalsHit:
        a.captured = True
        settings.captured += 1


def player_movement(player):
    """ check the players movement flags and move the player"""
    if player.moving_right == True: 
        player.move_self()
    if player.moving_left == True: 
        player.move_self()

def check_events(player,settings,ngUX,goUX, shield, startUX, endUX, tb):
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
                animals_hit(tb, settings)
                levelComplete(settings)

        elif event.type == KEYUP :
            if event.key == K_RIGHT: 
                player.moving_right = False
            elif event.key == K_LEFT: 
                player.moving_left = False

        #start the game when the player clicks "play"
        if settings.state in ['newgame','gameover','startLevel', 'endLevel']:
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

                if settings.state == 'startLevel':
                    huntButton = startUX[1]
                    startEvents(mouse_x,mouse_y,settings, huntButton)

                if settings.state == 'endLevel':
                    nextButton = endUX[2]
                    loadNext(mouse_x,mouse_y,settings, nextButton)

def playGame(mouse_x, mouse_y, settings, play_button,quit_button):
    """ start the game if the player clicks the mouse button"""
    if play_button.rect.collidepoint(mouse_x,mouse_y) and play_button.onscreen == True:
        settings.state = "startLevel"
        play_button.onscreen = False
    if quit_button.rect.collidepoint(mouse_x,mouse_y) and quit_button.onscreen == True:
      quitGame() 

def startEvents(mouse_x, mouse_y, settings, hunt_button):
    """ start the round if the player clicks the mouse button"""
    if hunt_button.rect.collidepoint(mouse_x,mouse_y) and hunt_button.onscreen == True:
        settings.state = "running"
        hunt_button.onscreen = False

def loadNext(mouse_x, mouse_y, settings, next_button):
    """ start the round if the player clicks the mouse button"""
    if next_button.rect.collidepoint(mouse_x,mouse_y) and next_button.onscreen == True:
        settings.state = "startLevel"
        next_button.onscreen = False

def resetGame(mouse_x, mouse_y, settings, reset_button,quit_button, player,shield):
    """ reset game settings to initial values"""
    if reset_button.rect.collidepoint(mouse_x,mouse_y) and reset_button.onscreen == True:
        init_stats(settings, player,shield)
        reset_button.onscreen = False
    if quit_button.rect.collidepoint(mouse_x,mouse_y) and quit_button.onscreen == True:
      quitGame() 


def quitGame():
    """ quit the game if the player clicks the quit button"""
    pg.quit()
    sys.exit()

def update_characters(gameSettings, gameDisplay, player, farmers,bullets,shield,tb):
    """ update images on the screen and draw new screen"""
    gameDisplay.fill(gameSettings.bg_color)
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    player.blit_self()
    for f in farmers:
        f.blit_self()
    for a in gameSettings.animals:
        if a.rect.bottom > 550:
            a.blit_self()
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

def startLevel(gameSettings,gameDisplay, startUX):
    """ methods for start level state"""
    gameDisplay.blit(gameSettings.bg_image,(0,0))

    #update the level number
    currLVL = "Farm {0}".format(gameSettings.level)
    print(gameSettings.level)
    # startUX[0].msg = "Farm {0}".format(gameSettings.level)
    startUX[0].msg = currLVL

    for i in startUX:
        i.blit_self()

    pg.display.update()

def endLevel(gameSettings,gameDisplay, endUX):
    """ methods for end level state"""
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    for i in endUX:
        i.blit_self()

    pg.display.update()

def gameover(gameSettings,gameDisplay,gameoverUX):
    """ methods for gameover state"""
    gameDisplay.blit(gameSettings.bg_image,(0,0))
    for g in gameoverUX:
        g.blit_self()

    pg.display.update()
