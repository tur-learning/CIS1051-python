import pygame
import sys
import asyncio 
from objects import Boat, GameManager, Trash, Rock, Coin
import time
import random


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

    width = tile_size * len(tiles[0])
    height = tile_size * len(tiles)
    screen = pygame.display.set_mode((width, height))
    screen_width = tile_size * len(tiles[0])
    screen_width = screen.get_width()


    water_tile = pygame.image.load("objects/waterimg.jpeg")
    rock_tile = pygame.image.load("objects/rock_tile.png")

    
    trash_group = pygame.sprite.Group()
    rock_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()

    trash_counters = 0
    trash_threshold = 30

    sprite1 = Trash(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    sprite2 = Trash(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    sprite3 = Trash(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    sprite4 = Trash(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    sprite5 = Trash(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)

    
    trash_group.add(sprite1, sprite2, sprite3, sprite4, sprite5)

    rock1 = Rock(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    rock2 = Rock(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    rock3 = Rock(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    rock_group.add(rock1, rock2, rock3)

    coin1 = Coin(random.uniform(tile_size, (len(tiles[0]) - 2)*tile_size),
                    random.uniform(tile_size, (len(tiles) - 2)*tile_size), screen_width, tile_size, tiles)
    coin_group.add(coin1)


    boat_pos = [0,200]
    boat_width = 50
    boat_height= 25


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
        boat.move(keys, tiles, rock_group, coin_group)
        trash_counters = 0

        screen.fill((0, 0, 255))

        for y, row in enumerate(tiles):
            for x, tile_type in enumerate(row):
                if tile_type == 0:
                    screen.blit(rock_tile, (x * tile_size, y * tile_size))
                elif tile_type == 1:
                    screen.blit(water_tile, (x * tile_size, y * tile_size))

        trash_group.update()
        trash_group.draw(screen)
        
        rock_group.update()
        rock_group.draw(screen)
        
        coin_group.update()
        coin_group.draw(screen)

        trash_collisions = pygame.sprite.spritecollide(boat, trash_group, False)

        for trash in trash_collisions:
            trash.update_counter()
            trash.generate_trash()
            boat.handle_collision()

        rock_collisions = pygame.sprite.spritecollide(boat, rock_group, False)
        
        for rock in rock_collisions:
            boat.handle_collision_rock()
            

        font = pygame.font.Font(pygame.font.get_default_font(), 36)

        points_text = font.render(f'Points:{boat.points}', True, (255,255,255))
        screen.blit(points_text, (10,10))

        for trash in trash_group:
            trash_counters += trash.trash_counter
            if trash_counters > trash_threshold:
                boat.game_over = True
                
        print(trash_counters)
            
        

        if boat.game_over:
            boat.display_game_over_screen(boat.points, trash_counters, trash_threshold)
            pygame.display.flip()
            pygame.time.delay(3000)
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


