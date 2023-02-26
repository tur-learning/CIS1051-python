import pygame
import game
import fruit

# defining snake default position
position = [100, 50]

# defining first 4 blocks of snake body
body = [ [100, 50],
         [ 90, 50],
         [ 80, 50],
         [ 70, 50] ]

def draw(game_window):
    for pos in body:
        pygame.draw.rect(game_window, game.green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

def move():
    grow = False
    
    body.insert(0, list(position))

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10

    grow = eat()

    if grow == False:
        body.pop()
        fruit.spawn = True
    else:
        fruit.spawn = False

def eat():
    if position[0] == fruit.position[0] and position[1] == fruit.position[1]:
        return True
    else:
        return False

