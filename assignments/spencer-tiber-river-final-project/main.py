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
    collision = False
    
    tile_size = 50

   

    #calling classes
    worldmap = environment.WorldMap(game_logic.map,tile_size)
    main_character = environment.Character(character_image,game_logic.player_pos)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        main_character.update(collision)

        worldmap.collision_rt(main_character.char_rect)
        worldmap.collision_lt(main_character.char_rect)
        worldmap.collision_top(main_character.char_rect,collision)


        #this is a background image
        screen.blit(bg_img, (0,0))

        #drawing the tile map
        worldmap.draw(screen)

        #TODO
        #create collision between character and pillar top
        #figure out enemy shooting
            
        #drawing the player
        screen.blit(environment.character_image, game_logic.player_pos)  
    

        pygame.display.flip()

            # Maintain game at 60 frames per second.
        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())  # Start the program