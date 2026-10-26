import sys
import pygame

from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien 
def run_game():
    pygame.init()
    ai_settings = Setting()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    running = True
    # Start the main loop for the game.
    while running:
        screen.fill(ai_settings.bg_color)
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        


run_game()


