# importing libraries
import pygame
import asyncio

# importing project modules
import game
import snake
import fruit
import wall


async def main():
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

		# Check if the fruit was eaten #TODO
		snake.move()

		if fruit.spawn == False:
			fruit.spawn = True
			fruit.position = fruit.locate()
			
		# Fill the game background
		game.fill(game_window)
		
		# Move the snake body
		snake.draw(game_window)

		# Spawn the fruit randomly
		fruit.draw(game_window)

		# Game Over conditions -- changing from game over to changing the position of the snake
		if snake.position[0] < 0:
    			snake.position[0] = game.window_x-10
		elif snake.position[0] > game.window_x-10:
    			snake.position[0] = 0

		if snake.position[1] < 0:
				snake.position[1] = game.window_y-10
		elif snake.position[1] > game.window_y-10:
				snake.position[1] = 0
	

		# Touching the snake body
		# Implement game over conditions if the snake touches itself 
		for block in snake.body[1:]:
			if snake.position == block:
					game.game_over(game_window)

		#if snake collides with wall then game over
		for block in wall.body:
			if snake.position == block:
				game.game_over(game_window)

		if snake.position == fruit.position:
    			new_position = locate()
    			while new_position in wall.body:
        			new_position = locate()
    			fruit.position = new_position


    # Generate a corner at a random position
    			new_corner_position = generate_corner_position(new_position[0], new_position[1])
    			generate_corner(new_corner_position[0], new_corner_position[1])


		# Refresh game
		game.update(game_window)
		await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())