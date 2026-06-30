import sys
import pygame
from pygame.sprite import Group
from settings import settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    # clock = pygame.time.Clock()
    ai_settings = settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    
    # Make an alien.
    alien = Alien(ai_settings, screen)


    # start the main loop for the game
    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        # clock.tick(390)


run_game()
