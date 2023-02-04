# importing libraries
import pygame

# importing project modules
import game
import snake
import fruit

# Initialising game
game_window = game.init()

# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

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

	if fruit.spawn == False: # fruit eaten
		game.score+=10
		fruit.position = fruit.locate()		
		
	# Fill the game background
	game.fill(game_window)
	
	# Move the snake body
	snake.draw(game_window)

	# Spawn the fruit randomly
	fruit.draw(game_window)

	# Game Over conditions
	if snake.position[0] < 0 or snake.position[0] > game.window_x-10:
		game.game_over(game_window)
	if snake.position[1] < 0 or snake.position[1] > game.window_y-10:
		game.game_over(game_window)

	# Touching the snake body
	for block in snake.body[1:]:
		if snake.position[0] == block[0] and snake.position[1] == block[1]:
			game.game_over(game_window)

	# Refresh game
	game.update(game_window)