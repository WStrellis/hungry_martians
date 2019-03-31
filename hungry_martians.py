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

   #set the text for level heading 
    currLVL = gameSettings.currentLVL()
    level_heading = Text(gameDisplay, 120, 500, 340, gameSettings.light_orange, currLVL)
    hunt_button = UXcomponent(gameDisplay,gameSettings.huntButton, 173, 159,500,500)

    # group for new game menu components
    newgameUX = [title,play_button, quit_button]
    
    # group for new level screen components
    levelUX = [level_heading, hunt_button]

    # group for game over menu components
    gameoverUX = [title,restart_button, quit_button]

    # create the player
    player = Ship(gameDisplay,500,200,False,False,10,3)
    tractorBeam = TBeam(gameDisplay, player.rect.centerx, player.rect.bottom, 10)

	# create cows
    cow = Cow(gameDisplay, 500, 750, False, True,5 )

    #create farmers
    farmer1 = Farmer(gameDisplay, 300, 750,True, False, 3, 12)
    farmer2 = Farmer(gameDisplay, 600, 750, False,True, 3, 17)

    #create a group for the farmers
    farmers = pg.sprite.Group()
    farmers.add([farmer1,farmer2])

    #create a group for the bullets
    bullets = pg.sprite.Group()

    while True:

        gameFunc.check_events(player,gameSettings,newgameUX,gameoverUX, shield_indicator, levelUX, tractorBeam)

        if gameSettings.state == "newgame":
            gameFunc.newgame(gameSettings,gameDisplay,newgameUX)

        if gameSettings.state == 'level':
            gameFunc.levelIntro(gameSettings,gameDisplay,levelUX)

        if gameSettings.state == "running":
            gameFunc.player_movement(player)
            player.move_self()
            cow.move_self()
            gameFunc.move_farmers(farmers)
            gameFunc.farmer_shoot(farmers,gameDisplay,bullets)
            gameFunc.move_bullet(bullets)
            gameFunc.ship_hit(player,bullets,shield_indicator, gameSettings)
            gameFunc.update_characters(gameSettings,gameDisplay,player,cow,farmers,bullets,shield_indicator, tractorBeam)


        if gameSettings.state == "gameover":
            gameFunc.gameover(gameSettings,gameDisplay,gameoverUX)


        clock.tick(FPS) #limit fps to 30

if __name__ == '__main__':
    run_game()
