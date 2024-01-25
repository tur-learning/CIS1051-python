import pygame
import game

position = game.random_pos()

spawn = False

def init():
    spawn = True

def draw(game_window):
    pygame.draw.rect(game_window, game.white, pygame.Rect(
                     position[0], position[1], 10, 10))

def position_overlaps_with_walls(pos, wall_positions): #fruit doesnt overlap with walls
    return pos in wall_positions
    if not position_overlaps_with_walls(new_position, wall_positions):
            return new_position



def locate():
    return game.random_pos()
    