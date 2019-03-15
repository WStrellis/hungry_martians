#! python3

import pygame as pg, hm_gamefunctions as gameFunc

from hm_settings import Settings
from hm_ship import Ship
from hm_cow import Cow
from hm_farmer import Farmer
from pygame.locals import *

def run_game():
    """The main game loop"""
    pg.init()

    gameSettings = Settings()

    FPS = gameSettings.fps # frames per second setting
    fpsClock = pg.time.Clock() #limit the speed of the game to a maxium of 30 loops per second

    #create a screen for the game
    gameDisplay = pg.display.set_mode((gameSettings.screen_width,gameSettings.screen_height))
    # set name of program at top of window
    pg.display.set_caption("Hungry Hungry Martians")

    player = Ship(gameDisplay)
    cow = Cow(gameDisplay)
    farmer = Farmer(gameDisplay)

    while True:

        gameFunc.check_events(player)
        player.move_ship()
        cow.move_cow()
        farmer.move_farmer()
        gameFunc.update_screen(gameSettings,gameDisplay,player,cow,farmer)

        fpsClock.tick(FPS)

if __name__ == '__main__':
    run_game()