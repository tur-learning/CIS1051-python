import pygame
import random
import time

# initial score
score = 0

# defining snake velocity
speed = 15

# defining colors
black 	= pygame.Color(  0,   0,   0)
white 	= pygame.Color(255, 255, 255)
red 	= pygame.Color(255,   0,   0)
green 	= pygame.Color(  0, 255,   0)

# Window size
window_x = 720 ; window_y = 480

# FPS (frames per second) controller
# object to help track time
fps = pygame.time.Clock()


def init():
    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snakes')
    game_window = pygame.display.set_mode((window_x, window_y))

    return game_window


def update(game_window):
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20, game_window)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(speed)

def random_int():
	n = random.randint(0,1)*2 -1
	return n

def random_pos():
    pos = [random.randrange(1, (window_x//10)) * 10,
           random.randrange(1, (window_y//10)) * 10]
    return pos

def fill(game_window):
    game_window.fill(black)

# displaying Score function
def show_score(choice, color, font, size, game_window):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)


# game over function
def game_over(game_window):

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()