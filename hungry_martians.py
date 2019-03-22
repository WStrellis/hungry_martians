#! python3

import pygame as pg, hm_gamefunctions as gameFunc

from hm_settings import Settings
from hm_ship import Ship
from hm_cow import Cow
from hm_farmer import Farmer
from hm_bullets import Bullet
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

    player = Ship(gameDisplay)
    cow = Cow(gameDisplay)

    #create farmers
    farmer1 = Farmer(gameDisplay)
    farmer2 = Farmer(gameDisplay)
    #create a group for the farmers
    farmers = pg.sprite.Group()
    farmers.add([farmer1,farmer2])

    bullet = Bullet(gameDisplay,farmer1)

    while True:

        gameFunc.check_events(player)
        gameFunc.player_movement(player)
        player.move_ship()
        cow.move_cow()
        gameFunc.move_farmers(farmers)
        gameFunc.update_screen(gameSettings,gameDisplay,player,cow,farmers,bullet)

        clock.tick(FPS) #limit fps to 30

if __name__ == '__main__':
    run_game()