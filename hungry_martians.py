#! python3

import pygame as pg, hm_gamefunctions as gameFunc

from hm_settings import Settings 
from hm_ship import Ship, TBeam
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

    # set name of program at top of window
    pg.display.set_caption("Hungry Martians")
   
    # create the player
    player = Ship(gameSettings.gameDisplay, 425, 150, 0, 0, 10, 3)
    tractorBeam = TBeam(gameSettings.gameDisplay, player.rect.centerx, player.rect.bottom, 10)

    #create a group for the bullets
    bullets = pg.sprite.Group()

    # music
    pg.mixer.music.load("Shady_Grove_Instrumental1.ogg")
    pg.mixer.music.set_volume(0.6) 
    pg.mixer.music.play(loops= -1)

    while True:

        gameFunc.check_events(player, gameSettings, tractorBeam )

        if gameSettings.state == "newgame":
            gameFunc.newgame(gameSettings)

        if gameSettings.state == 'startLevel':
            gameFunc.startLevel(gameSettings)

        if gameSettings.state == "running":
            gameFunc.player_movement(player)
            player.move_self()
            gameFunc.move_farmers(gameSettings.farmers)
            gameFunc.move_animals(gameSettings.animals)
            gameFunc.farmer_shoot(gameSettings.farmers, gameSettings.gameDisplay, bullets)
            gameFunc.move_bullet(bullets)
            gameFunc.ship_hit(player,bullets, gameSettings)
            gameFunc.update_characters(gameSettings, player, bullets, tractorBeam)
            player.chargeBeam()
            if len(gameSettings.animals) == gameSettings.captured:
                gameSettings.state = 'endLevel'
                tractorBeam.lifespan = 0
                player.charged = True
                player.chargingTimer = 0
                bullets.empty()

        if gameSettings.state == "endLevel":
            gameFunc.endLevel(gameSettings)

        if gameSettings.state == "gameover":
            gameFunc.gameover(gameSettings)


        clock.tick(FPS) #limit fps to 30

if __name__ == '__main__':
    run_game()
