import pygame
import sys
import asyncio

async def main():
    pygame.init()

    window_size = (1600, 900)
    screen = pygame.display.set_mode(window_size)

    # Load tile images. TODO
    # tiles = 

    # Initialize player position TODO
    # player_pos = 
    current_tile = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()

        # TODO
        # Handle player movement, cycling through tiles when 
        # reaching the window's edge.
        if keys[pygame.K_LEFT]:
            # player_pos[0] -= ...

            # if player_pos[0] < 0:
            #     ...

        if keys[pygame.K_RIGHT]:
            
        if keys[pygame.K_UP]:
             
        if keys[pygame.K_DOWN]:

        # Render current tile and player on the screen. TODO
        # screen.blit(appropriate_tile, (0, 0))
        # pygame.draw.circle(screen, (0, 0, 200), player_pos, 10)

        pygame.display.flip()

        # Maintain game at 60 frames per second.
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())  # Start the program
