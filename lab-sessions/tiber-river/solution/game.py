import pygame
import sys
import asyncio

async def main():
    pygame.init()

    window_size = (1600, 900)
    screen = pygame.display.set_mode(window_size)

    # Load tile images.
    tiles = [pygame.image.load(f'screenshot_{i}.png') for i in range(0, 6)]

    player_pos = [400, 300]
    current_tile = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()

        # Handle player movement.
        if keys[pygame.K_LEFT]:
            player_pos[0] -= 5
            # Cycle through tiles when reaching the window's edge.
            if player_pos[0] < 0:
                player_pos[0] = window_size[0] - 1
                current_tile = (current_tile + 1) % 6
        if keys[pygame.K_RIGHT]:
            player_pos[0] += 5
            if player_pos[0] >= window_size[0]:
                player_pos[0] = 0
                current_tile = (current_tile - 1) % 6
        if keys[pygame.K_UP]:
            player_pos[1] = max(player_pos[1] - 5, 0)
        if keys[pygame.K_DOWN]:
            player_pos[1] = min(player_pos[1] + 5, window_size[1] - 1)

        # Render current tile and player on the screen.
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
