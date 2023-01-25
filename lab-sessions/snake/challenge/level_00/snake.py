import pygame
import game
# import fruit #TODO

# defining snake default position
position = [100, 50]

# defining first 4 blocks of snake body
body = [ [100, 50],
         [ 90, 50],
         [ 80, 50],
         [ 70, 50],
         [ 60, 50],
         [ 50, 50],
         [ 40, 50],
         [ 30, 50],
         [ 20, 50],
         [ 10, 50],
         [ 0, 50] ]

def draw(game_window):
    for pos in body:
        pygame.draw.rect(game_window, game.green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

def move():
    grow = False
    
    body.insert(0, list(position))
    body.pop()

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10

    #TODO
    # grow = eat()

    # if grow == False:
    #     #TODO
    # else:
    #     #TODO

# def eat():
#     #TODO
#         return True
#     else:
#         return False