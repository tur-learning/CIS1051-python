import pygame
import game

# defining wall body
body = [ ]

# offset for wall corner generation
offset = 2

def wall_geometry(position):
    a = game.random_int()
    b = game.random_int()
    wall_body = [position,
                 [position[0] + a*10, position[1]],
                 [position[0] + a*20, position[1]],
                 [position[0], position[1] + b*10],
                 [position[0], position[1] + b*20]]
    return wall_body

def draw(game_window):
    for pos in body:
        pygame.draw.rect(game_window, game.red,
                         pygame.Rect(pos[0], pos[1], 10, 10))

def new_wall():
    new_position = game.random_pos(offset)
    wall_body = wall_geometry(new_position)

    for block in wall_body:
        body.append(block)
    if len(body) > 25:
        for _ in range(5):
            body.pop(0)
