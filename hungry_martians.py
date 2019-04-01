#! python3

import pygame as pg, hm_gamefunctions as gameFunc

from hm_settings import Settings
from hm_ship import Ship, TBeam
from hm_cow import Cow
from hm_farmer import Farmer
from hm_bullets import Bullet
from hm_ux import UXcomponent,ShieldIcon, Text
from pygame.locals import *

def run_game():
    """The main game loop"""
    pg.init()

    gameSettings = Settings()

    FPS = gameSettings.fps # frames per second setting
    clock = pg.time.Clock() #limit the speed of the game to a maxium of 30 loops per second

    #create a screen for the game
    gameDisplay = pg.display.set_mode((gameSettings.screen_width,gameSettings.screen_height))

    # set name of program at top of window
    pg.display.set_caption("Hungry Martians")

    # ux components
    shield_indicator = ShieldIcon(gameDisplay,gameSettings.green_shield,31, 35, 35, 75)

    title = UXcomponent(gameDisplay,gameSettings.title, 513, 141, 500,340)

    play_button = UXcomponent(gameDisplay,gameSettings.playButton, 173, 159,500,500)
    restart_button = UXcomponent(gameDisplay,gameSettings.restartButton, 173, 159,500,500)
    quit_button = UXcomponent(gameDisplay,gameSettings.quitButton, 173, 159, 500, 700)

   # start level screen components
    currLVL = gameSettings.currentLVL()
    level_heading = Text(gameDisplay, 120, 500, 340, gameSettings.light_orange, currLVL)
    hunt_button = UXcomponent(gameDisplay,gameSettings.huntButton, 173, 159,500,500)

   # end level screen components
    goodJob = Text(gameDisplay, 120, 500, 240, gameSettings.light_orange, "Good Job!")
    endMsg = Text(gameDisplay, 120, 500, 340, gameSettings.light_orange, "All animals abducted!")
    next_button = UXcomponent(gameDisplay, gameSettings.nextButton, 173, 159,500,500)

    # group for new game menu components
    newgameUX = [title,play_button, quit_button]
    
    # group for start level screen components
    startUX = [level_heading, hunt_button]

    # group for start level screen components
    endUX = [goodJob, endMsg, next_button]

    # group for game over menu components
    gameoverUX = [title,restart_button, quit_button]

    # create the player
    player = Ship(gameDisplay, 500, 200, 0, 0, 10, 3)
    print(player.rect.left)
    print(player.rect.right)
    tractorBeam = TBeam(gameDisplay, player.rect.centerx, player.rect.bottom, 10)

	# create cows
    cow1 = Cow(gameDisplay, 300, 750, 1, 0,5 )
    cow2 = Cow(gameDisplay, 500, 750, 0, 1,5 )

    #create a group for all animals
    gameSettings.animals.add([cow1,cow2])

    #create farmers
    farmer1 = Farmer(gameDisplay, 300, 750, 1, 0, 3, 12)
    farmer2 = Farmer(gameDisplay, 600, 750, 0, 1, 3, 17)

    #create a group for the farmers
    farmers = pg.sprite.Group()
    farmers.add([farmer1,farmer2])

    #create a group for the bullets
    bullets = pg.sprite.Group()

    while True:

        gameFunc.check_events(player,gameSettings,newgameUX,gameoverUX, shield_indicator, startUX, endUX, tractorBeam )

        if gameSettings.state == "newgame":
            gameFunc.newgame(gameSettings,gameDisplay,newgameUX)

        if gameSettings.state == 'startLevel':
            gameFunc.startLevel(gameSettings,gameDisplay,startUX)

        if gameSettings.state == "running":
            gameFunc.player_movement(player)
            player.move_self()
            gameFunc.move_farmers(farmers)
            gameFunc.move_animals(gameSettings.animals)
            gameFunc.farmer_shoot(farmers,gameDisplay,bullets)
            gameFunc.move_bullet(bullets)
            gameFunc.ship_hit(player,bullets,shield_indicator, gameSettings)
            gameFunc.update_characters(gameSettings, gameDisplay, player, farmers, bullets, shield_indicator, tractorBeam)
            player.chargeBeam()

        if gameSettings.state == "endLevel":
            gameFunc.endLevel(gameSettings,gameDisplay,endUX)

        if gameSettings.state == "gameover":
            gameFunc.gameover(gameSettings,gameDisplay,gameoverUX)


        clock.tick(FPS) #limit fps to 30

if __name__ == '__main__':
    run_game()
