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
    playtime = 0

    #create a screen for the game
    gameDisplay = pg.display.set_mode((gameSettings.screen_width,gameSettings.screen_height))
    # set name of program at top of window
    pg.display.set_caption("Hungry Hungry Martians")

    player = Ship(gameDisplay)
    cow = Cow(gameDisplay)
    farmer = Farmer(gameDisplay)
    bullet = Bullet(gameDisplay,farmer)


    while True:

        # milliseconds = clock.tick(FPS)
        # playtime += milliseconds / 1000.0
        # print(playtime)

        gameFunc.check_events(player)
        gameFunc.player_movement(player)
        player.move_ship()
        cow.move_cow()
        farmer.move_farmer()
        gameFunc.update_screen(gameSettings,gameDisplay,player,cow,farmer,bullet)

        clock.tick(FPS) #limit fps to 30

if __name__ == '__main__':
    run_game()