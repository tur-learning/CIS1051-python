import pygame
import fruit
import game
# import fruit #TODO

# defining snake default position
position = [100, 50]

# defining first 4 blocks of snake body
body = [ [100, 50],
         [ 90, 50],
         [ 80, 50],
         [ 70, 50]]

def draw(game_window):
    for pos in body:
        pygame.draw.rect(game_window, game.green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

def move():
    grow = False
    
    #body.insert(0, list(position))
    #body.pop()

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    body.insert(0, list(position))
    #TODO
    grow = eat()
#the growth mechanism where if growth is true, the fruit will despawn then respawn in a different place and then the score should go up by ten.
    if grow == False:
        fruit.spawn = True
        body.pop()
    else:
        fruit.spawn = False
        game.score += 10
    #     #TODO
    #     #TODO

def eat():
    if position == fruit.posi:
        print('om nom nom')
        return True
    else:
        return False
#     #TODO
#         return True
#     else:
#         return False
