import pygame
import game

# Setup initial fruit position
position = game.random_pos()

spawn = False

def init():
    spawn = True

def draw(game_window):
    pygame.draw.rect(game_window, game.white, pygame.Rect(
                     position[0], position[1], 10, 10))

# def locate():
#     #TODO