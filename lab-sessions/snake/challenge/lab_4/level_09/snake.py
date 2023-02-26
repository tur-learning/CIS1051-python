import pygame
import game
import fruit

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        game.speed = 30
    else:
        game.speed = 15

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10

    body.insert(0, list(position))
    grow = eat()

    if grow == False:
        body.pop()
        fruit.spawn = True
    else:
        fruit.spawn = False
        game.score += 10

def eat():
    if position == fruit.position:
        return True
    else:
        return False