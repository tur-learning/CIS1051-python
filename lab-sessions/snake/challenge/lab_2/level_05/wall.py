import pygame
import game

# defining wall body
body = [ ]

# drawing the blocks in game
def draw(game_window):
    for pos in body:
        pygame.draw.rect(game_window, game.red,
                         pygame.Rect(pos[0], pos[1], 10, 10))

# create a new block in the wall body
def new_wall():
    new_position = game.random_pos()
    body.append(new_position)
    if len(body) > 5:
        body.pop(0)