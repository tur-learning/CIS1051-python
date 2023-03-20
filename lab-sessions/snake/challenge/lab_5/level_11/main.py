# importing libraries
import pygame
import pygame_menu

# importing project modules
import game
import snake
import fruit
import wall

def start():
	# setting default snake direction towards right
	direction = 'RIGHT'
	change_to = direction
	
	start_time = 0

	# Setup fruit
	fruit.init()

	# Main Function
	while True:

		# handling key events
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					change_to = 'UP'
				if event.key == pygame.K_DOWN:
					change_to = 'DOWN'
				if event.key == pygame.K_LEFT:
					change_to = 'LEFT'
				if event.key == pygame.K_RIGHT:
					change_to = 'RIGHT'
				if event.key == pygame.K_LSHIFT:
					mainmenu()

		# We don't want the new direction to be the
		# opposite of the current one
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'

		# Moving the snake
		if direction == 'UP':
			snake.position[1] -= 10
		if direction == 'DOWN':
			snake.position[1] += 10
		if direction == 'LEFT':
			snake.position[0] -= 10
		if direction == 'RIGHT':
			snake.position[0] += 10

		# Check if the fruit was eaten
		snake.move()

		lifetime = pygame.time.get_ticks() - start_time
		if fruit.spawn == False or lifetime > 5000:
			fruit.spawn = True
			fruit.position = fruit.locate()
			start_time += lifetime
			if game.random_walls[0]:
				wall.new_wall()
				for block in wall.body:
					while fruit.position == block:
						fruit.position = fruit.locate()

		# Fill the game background
		game.fill(game_window)

		# Move the snake body
		snake.draw(game_window)

		# Spawn the fruit randomly
		fruit.draw(game_window)

		if game.random_walls[0]:
			# Draw the walls
			wall.draw(game_window)
			# Touching the wall, game over condition
			for block in wall.body:
				if snake.position == block:
					game.game_over(game_window)

		# Periodic boundary conditions
		if game.periodic[0]:
			if snake.position[0] < 0:
				snake.position[0] = game.window_x-10
			if snake.position[0] > game.window_x-10:
				snake.position[0] = 0
			if snake.position[1] < 0:
				snake.position[1] = game.window_y-10
			if snake.position[1] > game.window_y-10:
				snake.position[1] = 0
		else:
			# Game Over conditions
			if snake.position[0] < 0 or snake.position[0] > game.window_x-10:
				game.game_over(game_window)
			if snake.position[1] < 0 or snake.position[1] > game.window_y-10:
				game.game_over(game_window)

		# Touching the snake body
		for block in snake.body[1:]:
			if snake.position == block:
				game.game_over(game_window)

		# Refresh game
		game.update(game_window)

def mainmenu():
	# Create a menu object
	menu = pygame_menu.Menu('SNAKE', game.window_x, game.window_y, theme=game.theme)
	
	# Adding features to the menu
	menu.add.button('Play', start)
	menu.add.selector('Periodic boundaries: ', [('Yes', True), ('No', False)], onchange=game.set_periodic)
	menu.add.selector('Random walls: ', [('Yes', True), ('No', False)], onchange=game.set_walls)
	menu.add.text_input('Name: ')
	menu.add.button('Quit', pygame_menu.events.EXIT)
	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
				
		if menu.is_enabled():
			menu.update(events)
			menu.draw(game_window)
		
		pygame.display.update()

# Initialising game
game_window = game.init()

mainmenu()