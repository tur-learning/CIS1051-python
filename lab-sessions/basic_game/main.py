# importing libraries
import pygame
import asyncio

# importing project modules
import game

async def main():
	# Initialising game
    game_window = game.init()
    background = pygame.image.load('background.png').convert()

    # Load the player character image
    spaceship = pygame.image.load('spaceship.png').convert_alpha()

    # Spaceship position
    spaceship_x = 100
    spaceship_y = 100
    spaceship_change_x = 0
    spaceship_change_y = 0

    while True:
        # RGB - Red, Green, Blue
        game_window.fill((0, 0, 0))

        # Background Image
        game_window.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check keystroke is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spaceship_change_x = -5
                if event.key == pygame.K_RIGHT:
                    spaceship_change_x = 5
                if event.key == pygame.K_UP:
                    spaceship_change_y = -5
                if event.key == pygame.K_DOWN:
                    spaceship_change_y = 5
            
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    spaceship_change_x = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    spaceship_change_y = 0

        # Update spaceship position
        spaceship_x += spaceship_change_x
        spaceship_y += spaceship_change_y

        # Enforce screen boundaries for the spaceship
        spaceship_x = max(spaceship_x, 0)
        spaceship_x = min(spaceship_x, game.window_x - spaceship.get_width())
        spaceship_y = max(spaceship_y, 0)
        spaceship_y = min(spaceship_y, game.window_y - spaceship.get_height())

        game_window.blit(spaceship, (spaceship_x, spaceship_y))

        game.update(game_window)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
