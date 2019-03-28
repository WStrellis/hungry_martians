#! python3

import pygame as pg, hm_gamefunctions as gameFunc

from hm_settings import Settings
from hm_ship import Ship
from hm_cow import Cow
from hm_farmer import Farmer
from hm_bullets import Bullet
from hm_ux import UXcomponent,ShieldIcon
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
    pg.display.set_caption("Hungry Hungry Martians")

    # ux components
    shield_indicator = ShieldIcon(gameDisplay,gameSettings.green_shield,100,70)
    play_button = UXcomponent(gameDisplay,gameSettings.playButton,500,500)
    title = UXcomponent(gameDisplay,gameSettings.title,500,340)

    # group for ux components
    uxObjects = pg.sprite.Group()
    uxObjects.add([shield_indicator])
    

    # create the player
    player = Ship(gameDisplay,gameSettings.ufo,500,200,False,False,10,3)

	# create cows
    cow = Cow(gameDisplay,gameSettings.cow_left,500,750,False,True,5, gameSettings.cow_left, gameSettings.cow_right)

    #create farmers
    farmer1 = Farmer(gameDisplay,gameSettings.farmer_left,300,750,True,False, 3, gameSettings.farmer_left, gameSettings.farmer_right, 12)
    farmer2 = Farmer(gameDisplay,gameSettings.farmer_right,600,750,False,True, 3, gameSettings.farmer_left, gameSettings.farmer_right, 17)

    #create a group for the farmers
    farmers = pg.sprite.Group()
    farmers.add([farmer1,farmer2])

    #create a group for the bullets
    bullets = pg.sprite.Group()

    # gameState = "active"
    gameState = "inactive"

    while True:

        gameFunc.check_events(player)
        if gameState == "active":
            gameFunc.player_movement(player)
            player.move_self()
            cow.move_self()
            gameFunc.move_farmers(farmers)
            gameFunc.farmer_shoot(farmers,gameDisplay,bullets)
            gameFunc.move_bullet(bullets)
            gameFunc.ship_hit(player,bullets,shield_indicator)
        gameFunc.update_screen(gameSettings,gameDisplay,player,cow,farmers,bullets,shield_indicator,gameState,title,play_button)

        clock.tick(FPS) #limit fps to 30

if __name__ == '__main__':
    run_game()
