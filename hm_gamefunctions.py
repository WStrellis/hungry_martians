#!python3

import sys, pygame as pg, random
from hm_cow import Cow
from hm_chicken import Chicken
from hm_farmer import Farmer
from pygame.locals import *
from hm_ux import Text

def makeCharacters(settings):
    """ make farmers and cows"""
    settings.farmers.empty()
    settings.animals.empty()
    makeFarmer(settings)
    makeCow(settings)
    if settings.level >= 3:
        makeChicken(settings)

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

def ship_hit(ship, bullets, settings):
    """ Check if the player's ship has been hit by farmer's bullets"""
    if pg.sprite.spritecollideany(ship,bullets):
        # subtract 1 hp from the ship
        ship.hp -= 1
        # update the shield icon
        settings.shield_indicator.setImage(ship.hp)
        #delete all bullets
        for b in bullets.copy():
            b.kill()
        if ship.hp < 0:
                settings.state = "gameover"
    
def animals_hit(beam, settings):
    """ determine if animals have been shot by the laser"""
    animalsHit = pg.sprite.spritecollide(beam, settings.animals, False)

    for a in animalsHit:
        # makes the animal move up the screen
        a.captured = True
        # play the animal's sound
        a.speak()


def player_movement(player):
    """ check the players movement flags and move the player"""
    if player.moving_right == True: 
        player.move_self()
    if player.moving_left == True: 
        player.move_self()

def check_events(player, settings, tb):
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
                settings.setCaptured()

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
                    playGame(mouse_x,mouse_y,settings, player)

                if settings.state == 'gameover':
                    resetGame(mouse_x,mouse_y,settings, player)

                if settings.state == 'startLevel':
                    setupLevelStart(mouse_x,mouse_y,settings, player )

                if settings.state == 'endLevel':
                    loadNext(mouse_x,mouse_y,settings, player)

def playGame(mouse_x, mouse_y, settings, ship):
    """ start the game if the player clicks the mouse button"""
    if settings.playButton.rect.collidepoint(mouse_x,mouse_y) and settings.playButton.onscreen == True:
        settings.setupNewGame()
        ship.resetHP()
        settings.state = "startLevel"
        settings.playButton.onscreen = False
        
    if settings.quitButton.rect.collidepoint(mouse_x,mouse_y) and settings.quitButton.onscreen == True:
      quitGame() 

def setupLevelStart(mouse_x, mouse_y, settings, ship):
    """ sets up the screen to start each new level"""

    if settings.huntButton.rect.collidepoint(mouse_x,mouse_y) and settings.huntButton.onscreen == True:
        makeCharacters(settings)
        settings.state = "running"
        settings.huntButton.onscreen = False

def loadNext(mouse_x, mouse_y, settings, ship):
    """ executed when all of the cows have been captured"""

    if settings.nextButton.rect.collidepoint(mouse_x,mouse_y) and settings.nextButton.onscreen == True:
        settings.setupNextLevel()
        ship.resetHP()
        level = settings.level
        settings.levelHeading = Text(settings.gameDisplay, 120, 500, 340, settings.light_orange, "Farm {0}".format(level))
        updatedHeading = settings.levelHeading
        settings.startUX[0] = updatedHeading
        settings.state = "startLevel"
        settings.nextButton.onscreen = False

def resetGame(mouse_x, mouse_y, settings, player):
    """ reset game settings to initial values"""
    if settings.restartButton.rect.collidepoint(mouse_x,mouse_y) and settings.restartButton.onscreen == True:
        settings.state = "newgame"
        settings.setupNewGame()
        player.resetHP()
        settings.restartButton.onscreen = False
    if settings.quitButton.rect.collidepoint(mouse_x,mouse_y) and settings.quitButton.onscreen == True:
      quitGame() 


def quitGame():
    """ quit the game if the player clicks the quit button"""
    pg.quit()
    sys.exit()

def update_characters(settings, player, bullets, tb):
    """ update images on the screen and draw new screen"""
    settings.gameDisplay.fill(settings.bg_color)
    settings.gameDisplay.blit(settings.bg_image,(0,0))
    player.blit_self()
    for f in settings.farmers:
        f.blit_self()
    for a in settings.animals:
        if a.rect.bottom > 550:
            a.blit_self()
    # used to control how long the tb is displayed on the screen
    if tb.lifespan > 0:
        tb.blit_self()
    for b in bullets:
        b.blit_self()
    settings.shield_indicator.blit_self()

    pg.display.update()

def newgame(settings):
    """ methods for newgame state"""
    settings.gameDisplay.blit(settings.bg_image,(0,0))
    for n in settings.newgameUX:
        n.blit_self()

    pg.display.update()

def startLevel(settings):
    """ methods for start level state"""
    settings.gameDisplay.blit(settings.bg_image,(0,0))

    for i in settings.startUX:
        i.blit_self()

    pg.display.update()

def endLevel(settings):
    """ methods for end level state"""
    settings.gameDisplay.blit(settings.bg_image,(0,0))
    for i in settings.endUX:
        i.blit_self()

    pg.display.update()

def gameover(settings):
    """ methods for gameover state"""
    settings.gameDisplay.blit(settings.bg_image,(0,0))
    for g in settings.gameoverUX:
        g.blit_self()

    pg.display.update()

def setupMovement():
    """ returns a tuple of either 1,0 or 0,1"""
    mvmt = random.choice([(0,1),(1,0),(0,1),(1,0)])
    return mvmt

def setStartPoint(numCharacters):
    """ set up the characters to be evenly spaced"""
    evenDistance = int(1000 / (numCharacters + 1 ))
    positions = [ evenDistance * (x+ 1) for x in range(0, numCharacters)]

    negOffset = -int(evenDistance * 0.15)
    posOffset = int(evenDistance * 0.15)

    final = []

    for x in positions: 
        final.append( x + random.choice([negOffset,posOffset]))
    # return positions
    return final

def makeFarmer(settings):
    """ function to make a farmer"""

    # create list of start points
    startPoints = setStartPoint(settings.num_farmers)

    for x in range(0, settings.num_farmers):
        # make a tuple containing 0/1  for moveleft/moveingright
        left, right = setupMovement()

        # create a value for the shot trigger
        possible = [ x for x in range(25, 40)]
        random.shuffle(possible)
        shotTrig= random.choice(possible)

        location = startPoints[x]
        settings.farmers.add(Farmer(settings.gameDisplay, location, 730, left, right, 3, shotTrig))

def makeCow(settings):
    """ function to make a cow"""

    # create list of start points
    startPoints = setStartPoint(settings.num_cows)

    for x in range(0, settings.num_cows):
        # make a tuple containing 0/1  for moveleft/moveingright
        left, right = setupMovement()

        location = startPoints[x]
        settings.animals.add(Cow(settings.gameDisplay, location, 770, left, right, 5, settings.cowLeft, settings.cowRight , settings.cowsSay))

def makeChicken(settings):
    """ function to make chickens"""
    left, right = setupMovement()
    settings.animals.add(Chicken(settings.gameDisplay, 500, 770, left, right, 7, settings.chickenLeft, settings.chickenRight, settings.chickensSay))
