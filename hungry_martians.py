#! python3

import pygame as pg, hm_gamefunctions as gameFunc

from hm_settings import Settings 
from hm_ship import Ship, TBeam
from hm_cow import Cow
from hm_farmer import Farmer
from hm_bullets import Bullet
# from hm_ux import UXcomponent,ShieldIcon, Text
from pygame.locals import *

def run_game():
    """The main game loop"""
    pg.init()

    gameSettings = Settings()

    FPS = gameSettings.fps # frames per second setting
    clock = pg.time.Clock() #limit the speed of the game to a maxium of 30 loops per second

    #create a screen for the game
    # gameDisplay = pg.display.set_mode((gameSettings.screen_width,gameSettings.screen_height))

    # set name of program at top of window
    pg.display.set_caption("Hungry Martians")

   
    # create the player
    player = Ship(gameSettings.gameDisplay, 500, 200, 0, 0, 10, 3)
    tractorBeam = TBeam(gameSettings.gameDisplay, player.rect.centerx, player.rect.bottom, 10)

	# create cows
    cow1 = Cow(gameSettings.gameDisplay, 300, 750, 1, 0,5 )
    cow2 = Cow(gameSettings.gameDisplay, 500, 750, 0, 1,5 )

    #create a group for all animals
    gameSettings.animals.add([cow1,cow2])

    #create farmers
    farmer1 = Farmer(gameSettings.gameDisplay, 300, 750, 1, 0, 3, 12)
    farmer2 = Farmer(gameSettings.gameDisplay, 600, 750, 0, 1, 3, 17)

    #create a group for the farmers
    farmers = pg.sprite.Group()
    farmers.add([farmer1,farmer2])

    #create a group for the bullets
    bullets = pg.sprite.Group()

    while True:

        gameFunc.check_events(player, gameSettings, tractorBeam )

        if gameSettings.state == "newgame":
            gameFunc.newgame(gameSettings)

        if gameSettings.state == 'startLevel':
            gameFunc.startLevel(gameSettings)

        if gameSettings.state == "running":
            gameFunc.player_movement(player)
            player.move_self()
            gameFunc.move_farmers(farmers)
            gameFunc.move_animals(gameSettings.animals)
            gameFunc.farmer_shoot(farmers,gameSettings.gameDisplay,bullets)
            gameFunc.move_bullet(bullets)
            gameFunc.ship_hit(player,bullets, gameSettings)
            gameFunc.update_characters(gameSettings, player, farmers, bullets, tractorBeam)
            player.chargeBeam()

        if gameSettings.state == "endLevel":
            gameFunc.endLevel(gameSettings)

        if gameSettings.state == "gameover":
            gameFunc.gameover(gameSettings)


        clock.tick(FPS) #limit fps to 30

if __name__ == '__main__':
    run_game()
