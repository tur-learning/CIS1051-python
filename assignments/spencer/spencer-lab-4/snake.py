import pygame
import game
import fruit
import time
import wall
import main

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

    #allowing for speed increase and decrease with plus and minus keys. Speed increases by 1 to allow for fine tuning.
    keys = pygame.key.get_pressed()    	
    
    if keys[pygame.K_EQUALS]:
        game.speed += 1
    elif keys[pygame.K_MINUS]:
         game.speed -= 1
         
	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10

    body.insert(0, list(position))
    grow = eat()

    #if grow is false, subtract nothing from the list, if it is true, add score and despawn a fruit to rerun the fruit spawn code
    if grow == False:
        body.pop()
        fruit.spawn = True
    else:
        fruit.spawn = False
        game.score += 10

#function to determine if a fruit was eaten and add a new wall
def eat():
    if position == fruit.position:
        wall.add_wall()
        return True
    else:
        return False



