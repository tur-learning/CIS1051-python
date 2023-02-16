import pygame
import game
import random

position = game.random_pos()

body = []

offset = 2

def draw(game_window):
    for pos in body:
        pygame.draw.rect(game_window, game.red,
            pygame.Rect(pos[0], pos[1], 10, 10))

def locate():
    return game.random_pos(offset)
'''
def generateShape(pos):
    newBody = []
    newBody.append(pos)
    orientation = random.randint(1, 4)
    if orientation == 1:
        newBody.append([pos[0], pos[1]-10])
        newBody.append([pos[0], pos[1]-20])
        newBody.append([pos[0]+10, pos[1]])
        newBody.append([pos[0]+20, pos[1]])
    elif orientation == 2: # fix this
        newBody.append([pos[0], pos[1]+10])
        newBody.append([pos[0], pos[1]+20])
        newBody.append([pos[0]+10, pos[1]])
        newBody.append([pos[0]+20, pos[1]])
    elif orientation == 3: # fix this
        newBody.append([pos[0], pos[1]-10])
        newBody.append([pos[0], pos[1]-20])
        newBody.append([pos[0]-10, pos[1]])
        newBody.append([pos[0]-20, pos[1]])
    else: # fix this
        newBody.append([pos[0], pos[1]+10])
        newBody.append([pos[0], pos[1]+20])
        newBody.append([pos[0]-10, pos[1]])
        newBody.append([pos[0]-20, pos[1]])
    return newBody
'''

def generateShape(pos):
    newBody = []
    newBody.append(pos)
    orientation = random.randint(1, 4)
    if orientation == 1:
        newBody.append([pos[0], pos[1]-10])
        newBody.append([pos[0], pos[1]-20])
        newBody.append([pos[0]+10, pos[1]])
        newBody.append([pos[0]+20, pos[1]])
    elif orientation == 2: 
        newBody.append([pos[0], pos[1]+10])
        newBody.append([pos[0], pos[1]+20])
        newBody.append([pos[0]+10, pos[1]])
        newBody.append([pos[0]+20, pos[1]])
    elif orientation == 3: 
        newBody.append([pos[0], pos[1]-10])
        newBody.append([pos[0], pos[1]-20])
        newBody.append([pos[0]-10, pos[1]])
        newBody.append([pos[0]-20, pos[1]])
    else: 
        newBody.append([pos[0], pos[1]+10])
        newBody.append([pos[0], pos[1]+20])
        newBody.append([pos[0]-10, pos[1]])
        newBody.append([pos[0]-20, pos[1]])
    return newBody

def newWall():
    position = locate()
    shape = generateShape(position)
    for i in shape:
        body.append(i)
        if len(body) > 25:
            for i in range(5):
                body.pop(0)
