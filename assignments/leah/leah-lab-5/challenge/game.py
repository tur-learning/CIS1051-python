import pygame
import sys
import asyncio

async def main():
    pygame.init()

    window_size = (1600, 900)
    screen = pygame.display.set_mode(window_size)

    # Load tile images. TODO
    tiles = [pygame.image.load("tile0.png"),
            pygame.image.load("tile1.png"),
            pygame.image.load("tile2.png"),
            pygame.image.load("tile3.png"),
            pygame.image.load("tile4.png"),
            pygame.image.load("tile5.png")]

    # Initialize player position TODO
    player_pos = [100, 100]
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
            player_pos[0] -= 20
            if player_pos[0] < 0:
                player_pos[0] = window_size[0] - 1
                current_tile = (current_tile + 1) % 6
                
        if keys[pygame.K_RIGHT]:
            player_pos[0] += 20
            if player_pos[0] >= window_size[0]:
                player_pos[0] = 0
                current_tile = (current_tile - 1) % 6
            
        if keys[pygame.K_UP]:
            player_pos[1] -= 20
             
        if keys[pygame.K_DOWN]:
            player_pos[1] += 20

        # Render current tile and player on the screen. TODO
        screen.blit(tiles[current_tile], (0, 0))

        pygame.draw.circle(screen, (0, 0, 200), player_pos, 10)

        pygame.display.flip()

        # Maintain game at 60 frames per second.
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())  # Start the program
