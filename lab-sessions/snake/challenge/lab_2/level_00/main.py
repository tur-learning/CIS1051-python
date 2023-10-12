# importing libraries
import pygame
import asyncio

# importing project modules
import game
import snake
import fruit

async def main():
	# Initialising game
	game_window = game.init()

	# setting default snake direction towards right
	direction = 'RIGHT'
	change_to = direction

	# Setup fruit
	# #TODO
	fruit.init()

	# Main Function
	while True:
		
		# handling key events
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					change_to = 'UP'
				if event.key == pygame.K_s:
					change_to = 'DOWN'
				if event.key == pygame.K_a:
					change_to = 'LEFT'
				if event.key == pygame.K_d:
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
		#if the fruit is eaten, despawn the fruit so that the below if statement can respawn it properly. 
		snake.move()
		if snake.position == fruit.posi:
			fruit.spawn = False
			snake.eat()
			
	

		#if the fruit is not spawned, spawn the fruit and call the set the position to the locate function
		if fruit.spawn == False: 
			fruit.spawn = True
			fruit.posi = fruit.locate()
		# 	#TODO
		# 	#TODO
			
		# Fill the game background
		game.fill(game_window)
		
		# Move the snake body
		snake.draw(game_window)

		# Spawn the fruit randomly. This function draws the fruit in a random position on the board.
		fruit.draw(game_window)
		
			

		# Game Over conditions
		if snake.position[0] < 0 or snake.position[0] > game.window_x-10:
			game.game_over(game_window)
		if snake.position[1] < 0 or snake.position[1] > game.window_y-10:
			game.game_over(game_window)

		# Touching the snake body
		# Implement game over conditions if the snake touches itself #TODO
		for block in snake.body[1:]:
			if snake.position == block:
				game.game_over(game_window)


		# Refresh game
		game.update(game_window)
		await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())