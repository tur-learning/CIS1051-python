import main
import pygame
import time
import math
import game_logic


#DISREGARD THIS SCRIPT SO FAR. IT IS SOME HOT GARBAGE. 
class BadGuy():
	def __init__(self,image,bad_pos):
		# Load the enemy's image
		self.image = image
		# Create a Rect for the enemy and set its initial position
		self.rect = self.image.get_rect()
		self.rect.topleft = bad_pos
	

	







#firing a bullet if two seconds have passed
#	if time.time() - last_fire >= 2:  # Check if 2 seconds have passed
	#	bullet_slope = enemy_shoot(game_logic.player_pos, game_logic.enemy_pos)
	#	last_fire = time.time()
		
		
		
	
	#iterating through the bullets list to change the position based on the velocity
	#for item in bullets:
		#item[0] -= (bullet_slope[0] * 3)
	#	item[1] -= (bullet_slope[1] * 3)

    #TODO
    #fix bullet spawn on screen
   
        #filter the bullets list to only draw bullets that are on the screen
	def is_bullet_on_screen(bullet, window_size):
		x, y = bullet
		return 0 <= x <= window_size[0] and 0 <= y <= window_size[1]

	#this attempts to filter the bullets list to only keep bullets that are on the screen
	#bullets = [bullet for bullet in bullets if is_bullet_on_screen(bullet, game_logic.window_size)]
        
       



#a list used to show what bullets appear and are drawn on the screen
bullets = []




def enemy_shoot(player_pos, enemy_pos):
    bullets.append([700,700])
    slope = [(enemy_pos[0] - player_pos[0]),(enemy_pos[1] - player_pos[1])]
    length = max(1, math.sqrt(slope[0] ** 2 + slope[1] ** 2))
    normalized_direction = [slope[0] / length, slope[1] / length]
    return [normalized_direction[0], normalized_direction[1]]
   


last_fire = time.time()
  




# game over function
def game_over(game_window):

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is not real ' , True, [255,0,0])
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (main.window_size[0]/2, main.window_size[1]/4)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()  








