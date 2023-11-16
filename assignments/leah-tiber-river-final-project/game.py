import pygame
import sys
import asyncio 
from objects import Boat, GameManager, MySprite
import time


async def main():
    pygame.init()
    tile_size = 100
    tiles = [
    [0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0]
]

    screen = pygame.display.set_mode((tile_size * len(tiles[0]), tile_size * len(tiles)))
    screen_width = tile_size * len(tiles[0])


    water_tile = pygame.image.load("objects/waterimg.jpeg")
    rock_tile = pygame.image.load("objects/rock_tile.png")

    sprite1 = MySprite("objects/bottle.png", 30, 30, screen_width, tile_size)
    sprite2 = MySprite("objects/cig.png", 30, 20, screen_width, tile_size)
    sprite3 = MySprite("objects/twig.png", 30, 20, screen_width, tile_size)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(sprite1, sprite2, sprite3)



    boat_pos = [0,200]
    boat_width = 50
    boat_height= 50


    game_manager = GameManager(screen, screen_width)
    boat = Boat("objects/boat.png", boat_pos[0], boat_pos[1], game_manager, boat_width, boat_height, screen_width)
                                   

    running = True
    exit_game = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        boat.move(keys, tiles)

        screen.fill((0, 0, 255))

        for y, row in enumerate(tiles):
            for x, tile_type in enumerate(row):
                if tile_type == 0:
                    screen.blit(rock_tile, (x * tile_size, y * tile_size))
                elif tile_type == 1:
                    screen.blit(water_tile, (x * tile_size, y * tile_size))

        all_sprites.update(tiles)
        all_sprites.draw(screen)


        if boat.game_over:
            boat.display_game_over_screen()
            pygame.display.flip()
            pygame.time.delay(5000)
            running = False
            time.sleep(2)
            pygame.quit()
            quit()
        else:
            boat.draw(screen)

        
        pygame.display.flip()
        
        
           
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()


