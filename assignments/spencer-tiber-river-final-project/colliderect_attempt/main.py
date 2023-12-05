import pygame
import sys
import random
import enemy
import time
import math
import environment
import game_logic
import pygame.mixer as mixer

def main():
    pygame.init()

 
        

    
    
    screen = pygame.display.set_mode(game_logic.window_size)
    bg_img = pygame.image.load('img/sky.png')
    bg_img = pygame.transform.scale(bg_img, (1400,900))

    #making the character a little julius cesar
    character_image = pygame.image.load('img/julius cesar.png')  # Replace 'character.png' with the file path of your character's image
    #establishing character dimensions and scaling the image accordingly
    character_width = 30  
    character_height = 40  
    character_image = pygame.transform.scale(character_image, (character_width, character_height))  
    

    enemy_image = pygame.image.load('img/roman_soldier.png')
    enemy_width = 20
    enemy_height = 30
    enemy_image = pygame.transform.scale(enemy_image, (enemy_width,enemy_height))
    bullet_dimension = 15


    tile_size = 25

    #calling classes
    worldmap = environment.WorldMap(game_logic.map_1,tile_size)
    main_character = environment.Character(character_image,game_logic.player_pos)
    
    #establishing bad_guys
   
    level_1_walkers = pygame.sprite.Group()
    level_1_shooters = pygame.sprite.Group()
    bad_guy1 = enemy.BadGuy(100, 545, enemy_width,enemy_height, enemy_image)
    bad_guy2 = enemy.BadGuy(375,625,enemy_width,enemy_height,enemy_image)
    bad_guy3 = enemy.BadGuy(325,545,enemy_width,enemy_height,enemy_image)
    bad_guy4 = enemy.BadGuy(675,295,enemy_width,enemy_height,enemy_image)
    bad_guy5 = enemy.BadGuy(725,320,enemy_width,enemy_height,enemy_image)
    bad_guy6 = enemy.BadGuy(800,320,enemy_width,enemy_height,enemy_image)
    bad_guy7 = enemy.BadGuy(800,220,enemy_width,enemy_height,enemy_image)
    bad_guy8 = enemy.BadGuy(1375,370,enemy_width,enemy_height,enemy_image)
    bad_guy9 = enemy.BadGuy(1375,495,enemy_width,enemy_height,enemy_image)
    bad_guy10 = enemy.BadGuy(1100,625,enemy_width,enemy_height,enemy_image)

    level_1_walkers.add(bad_guy2,bad_guy5,bad_guy6,bad_guy7,bad_guy10)
    level_1_shooters.add(bad_guy1, bad_guy3,bad_guy4,bad_guy8,bad_guy9)

    #calling level class to build levels 
    level_1 = environment.Level(game_logic.map_1,level_1_walkers,level_1_shooters, tile_size)

    #creating list of levels to feed to game class
    levels = [level_1]

    all_sprites = pygame.sprite.Group()
    walking_sprites = pygame.sprite.Group()
    shooting_sprites = pygame.sprite.Group()

    all_sprites.add()
    walking_sprites.add()
    shooting_sprites.add()


    start_screen = environment.StartScreen()
    running = False

    gameover = environment.GameOver(game_logic.window_size[0],game_logic.window_size[1])

   #main characters shot bullets
    bullet_group = pygame.sprite.Group()
   
   #game class calling
    game = environment.Game(levels)

    #music stuff
    mixer.init()
    title_music = pygame.mixer.Sound('img/title_music.mp3')
    pygame.mixer.music.set_volume(0.5)
    
    running = False
    playing_title_music = True 

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

        if playing_title_music:
            title_music.play(loops=-1)
        
        # Update the display
        pygame.display.flip()
            
        title_music.stop()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        

        game.load_level(screen,shooting_sprites,walking_sprites)

        main_character.update(worldmap.col_collide, worldmap.col_top, worldmap.col_bot, worldmap.col_single)
    
        
    
        

        #this is a background image
        screen.blit(bg_img, (0,0))

    


        #drawing the tile map
        #worldmap.draw(screen)

            
        #drawing the player
        screen.blit(environment.character_image, game_logic.player_pos)  

        current_time = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds
        for man in shooting_sprites:
            man.timer(current_time, main_character.rect, bullet_dimension, bullet_dimension)


        #all_sprites.draw(screen)

     
        for man in shooting_sprites:
            for bullet in man.bullets:
                bullet.draw(screen)
        
        for man in shooting_sprites:
                # Update bullets
            for bullet in man.bullets:
                bullet.update()   
        

    #trying to handle the shooting detection
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            main_character.shoot(bullet_group, bullet_dimension, bullet_dimension)

        # Update and draw bullets
        bullet_group.update()
        bullet_group.draw(screen)
        for man in walking_sprites:
            man.update(worldmap.col_collide)
        for man in shooting_sprites:
            man.bullet_detect_env(worldmap.bullet_col)
        main_character.bullet_detect_env(bullet_group, worldmap.bullet_col)
        main_character.kill_enemy(bullet_group, all_sprites, shooting_sprites)

        for man in shooting_sprites:
            man.shoot_kill_character(main_character.rect, gameover)
        for man in all_sprites:
            man.walk_kill_character(main_character.rect, gameover)
        pygame.display.flip()

            # Maintain game at 60 frames per second.
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()  # Start the program