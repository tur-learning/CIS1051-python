# importing libraries
import pygame

# importing project modules
import game
import snake
import fruit
import wall

boundaries = False
walls = False

input1 = input("\nWould you like to have boundaries? (Y / N) : ")
if input1.lower() == "y" or input1.lower() == "yes":
	boundaries = True

input2 = input("\nWould you like to have wall generation? (Y / N) : ")
if input2.lower() == "y" or input2.lower() == "yes":
	walls = True

# Initialising game
game_window = game.init()

# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# Setup fruit
fruit.init()

fruit_start_time = 0
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

	# Check if the fruit was eaten #TODO
	snake.move()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		game.speed += 5
	else:
		game.speed = 15

	if not fruit.spawn or pygame.time.get_ticks() - fruit_start_time > 5000:
		game.score += 10
		fruit.position = fruit.locate()
		fruit_start_time = pygame.time.get_ticks()
		if walls == False:
			continue
		else:
			wall.newWall()
			for i in wall.body:
				while fruit.position == i:
					fruit.position = fruit.locate()

	# Fill the game background
	game.fill(game_window)
		
	# Move the snake body
	snake.draw(game_window)

	# Spawn the fruit randomly #TODO
	fruit.draw(game_window)

	wall.draw(game_window)

	# Game Over conditions
	for block in snake.body[1:]:
		if snake.position == wall.position:
			game.game_over(game_window)

	if boundaries == False:
		if snake.position[0] < 0:
			snake.position[0] = game.window_x-10
		if snake.position[0] > game.window_x-10:
			snake.position[0] = 0
		if snake.position[1] < 0:
			snake.position[1] = game.window_y-10
		if snake.position[1] > game.window_y-10:
			snake.position[1] = 0
	else:
		if snake.position[0] < 0 or snake.position[0] > game.window_x or snake.position[1] < 0 or snake.position[1] > game.window_y:
			game.game_over(game_window)

	# Touching the snake body
	# Implement game over conditions if the snake touches itself #TODO
	for block in snake.body[1:]:
		if snake.position == block:
			game.game_over(game_window)

	for block in wall.body[1:]:
		if snake.position == block:
			game.game_over(game_window)

	# Refresh game
	game.update(game_window)