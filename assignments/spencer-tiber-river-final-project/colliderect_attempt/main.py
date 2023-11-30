import pygame
import sys
import random
import enemy
import time
import math
import environment
import game_logic

def main():
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
    bullet_dimension = 15


    tile_size = 50


    #calling classes
    worldmap = environment.WorldMap(game_logic.map,tile_size)
    main_character = environment.Character(character_image,game_logic.player_pos)
    
    #establishing bad_guys
    all_sprites = pygame.sprite.Group()
    walking_sprites = pygame.sprite.Group()
    shooting_sprites = pygame.sprite.Group()
    bad_guy1 = enemy.BadGuy(game_logic.enemy1_pos[0], game_logic.enemy1_pos[1], enemy_width,enemy_height, enemy_image)
    bad_guy2 = enemy.BadGuy(500,450,enemy_width,enemy_height,enemy_image)
    bad_guy3 = enemy.BadGuy(150,350,enemy_width,enemy_height,enemy_image)
    all_sprites.add(bad_guy1, bad_guy2, bad_guy3)
    walking_sprites.add(bad_guy2)
    shooting_sprites.add(bad_guy1, bad_guy3)


    start_screen = environment.StartScreen()
    running = False

    gameover = environment.GameOver(game_logic.window_size[0],game_logic.window_size[1])

   #main characters shot bullets
    bullet_group = pygame.sprite.Group()

    


    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle events specific to the start screen
        if start_screen.handle_events(event):
            running = True

        # Draw the start screen
        start_screen.draw(screen)

        # Update the display
        pygame.display.flip()
        pygame.time.Clock().tick(60)


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

            
        #drawing the player
        screen.blit(environment.character_image, game_logic.player_pos)  

        current_time = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds
        bad_guy1.timer(current_time, main_character.rect, bullet_dimension, bullet_dimension)
        bad_guy3.timer(current_time, main_character.rect, bullet_dimension, bullet_dimension)

       
        

        all_sprites.draw(screen)

     

        for bullet in bad_guy1.bullets:
            bullet.draw(screen)

             # Update bullets
        for bullet in bad_guy1.bullets:
            bullet.update()
        
        for bullet in bad_guy3.bullets:
            bullet.draw(screen)

             # Update bullets
        for bullet in bad_guy3.bullets:
            bullet.update()
        

    #trying to handle the shooting detection
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                main_character.shoot(bullet_group, bullet_dimension, bullet_dimension,screen)

        # Update and draw bullets
        bullet_group.update()
        bullet_group.draw(screen)
        
        bad_guy2.update(walking_sprites, worldmap.col_collide)
        
        bad_guy1.bullet_detect_env(worldmap.bullet_col)
        bad_guy3.bullet_detect_env(worldmap.bullet_col)
        main_character.bullet_detect_env(bullet_group, worldmap.bullet_col)
        main_character.kill_enemy(bullet_group, all_sprites, shooting_sprites)

        bad_guy1.shoot_kill_character(main_character.rect, gameover)
        bad_guy3.shoot_kill_character(main_character.rect, gameover)
        bad_guy2.walk_kill_character(main_character.rect, gameover)

    
        pygame.display.flip()

            # Maintain game at 60 frames per second.
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()  # Start the program