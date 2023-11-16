import pygame
import sys
import asyncio
import random
import enemy
import time
import math
import environment
import game_logic

async def main():
    pygame.init()



    
    
    screen = pygame.display.set_mode(game_logic.window_size)
    bg_img = pygame.image.load('img/sky.png')
    bg_img = pygame.transform.scale(bg_img, (1000,900))

    #making the character a little julius cesar
    character_image = pygame.image.load('img/julius cesar.png')  # Replace 'character.png' with the file path of your character's image
    #establishing character dimensions and scaling the image accordingly
    character_width = 30  
    character_height = 40  
    character_image = pygame.transform.scale(character_image, (character_width, character_height))  
    

    enemy_image = pygame.image.load('img/roman_soldier.png')
    enemy_width = 40
    enemy_height = 50
    enemy_image = pygame.transform.scale(enemy_image, (enemy_width,enemy_height))
    bullet_dimension = 10


    tile_size = 50

#For debugging
    n_tiles = game_logic.window_size[0]//tile_size
    

    def draw_grid():
        for n in range(0, n_tiles):
            pygame.draw.line(screen, (255, 255, 255), (0, n * tile_size), (game_logic.window_size[0], n * tile_size))
            pygame.draw.line(screen, (255, 255, 255), (n * tile_size, 0), (n * tile_size, game_logic.window_size[1]))



    #calling classes
    worldmap = environment.WorldMap(game_logic.map,tile_size)
    main_character = environment.Character(character_image,game_logic.player_pos)
    bad_guy = enemy.BadGuy(game_logic.enemy_pos[0], game_logic.enemy_pos[1], enemy_width,enemy_height, enemy_image)
   



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        main_character.update(worldmap.col_collide, worldmap.col_top)
    


        

        #this is a background image
        screen.blit(bg_img, (0,0))

    


        #drawing the tile map
        worldmap.draw(screen)

        enemy.all_sprites.update()
        #TODO
        #create collision between character and pillar top
        #figure out enemy shooting
            
        #drawing the player
        screen.blit(environment.character_image, game_logic.player_pos)  

        current_time = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds
        bad_guy.timer(current_time, game_logic.player_pos, 2, bullet_dimension, bullet_dimension)

        enemy.all_sprites.draw(screen)

       # bad_guy.update(enemy.walking_sprites,)

        for bullet in bad_guy.bullets:
            bullet.draw(screen)

             # Update bullets
        for bullet in bad_guy.bullets:
            bullet.update()
        
        bad_guy.bullet_detect_env(worldmap.bullet_col)
        
        draw_grid()

        pygame.display.flip()

            # Maintain game at 60 frames per second.
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())  # Start the program