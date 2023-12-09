import main
import pygame
import time
import math
import game_logic
import enemy
import main
from itertools import cycle
import sys
import subprocess

    
    #making the character a little julius cesar
character_image = pygame.image.load('img/julius cesar.png')  # Replace 'character.png' with the file path of your character's image

    #establishing character dimensions and scaling the image accordingly
character_width = 25  
character_height = 40 
character_image = pygame.transform.scale(character_image, (character_width, character_height))
char_rect = character_image.get_rect()


class Character():
    def __init__(self, image, initial_position):
        super().__init__()

        # Load the sprite's image
        self.image = image

        # Create a Rect for the sprite and set its initial position
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.collision = False
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]
        self.bullets = []
        self.last_shoot = 0
        #player collision logic for hitting the columns.
    def player_collide(self, column, top, bot,single):
            dummy_rect = pygame.Rect(game_logic.dummy_x,game_logic.dummy_y,20,40)
            for tile in column:
                if tile in top:
                    if dummy_rect.colliderect(tile):
                        self.collision = True
                        if game_logic.dummy_y + 37.1 < tile.y:
                            game_logic.delta_y = 0
                            game_logic.player_pos[1] = tile.y - 40.01
                            if tile.x <= self.dummy_rect.centerx <= tile.x+25:
                                game_logic.jumping = False
                                game_logic.jump_counter = game_logic.jump_height
                                game_logic.falling = False
                        else:
                            game_logic.delta_x = 0
                            if game_logic.jump_counter <= 0:
                                game_logic.falling = True
                elif tile in bot:
                    if dummy_rect.colliderect(tile):
                        self.collision = True
                        if game_logic.dummy_y > tile.y:#off set for bottom corner
                            game_logic.jump_counter = 0
                            game_logic.falling = True
                            
                        else:
                            game_logic.delta_x = 0
                elif tile in single:
                    if dummy_rect.colliderect(tile):
                        self.collision = True
                        if game_logic.dummy_y > tile.y:
                            game_logic.jump_counter = 0
                            game_logic.falling = True
                        elif game_logic.dummy_y + 37.1 < tile.y:
                            game_logic.delta_y = 0
                            game_logic.player_pos[1] = tile.y - 40.01
                            if tile.x <= self.dummy_rect.centerx <= tile.x+25:
                                game_logic.jumping = False
                                game_logic.jump_counter = game_logic.jump_height
                                game_logic.falling = False
                        else:
                            game_logic.delta_x = 0

                elif dummy_rect.colliderect(tile):
                    game_logic.delta_x = 0

#handling the players jumping so the delta_y can be modified after collision is detected
    def player_jump(self):
        keys = pygame.key.get_pressed()
        #if the space bar is hit and the player is not jumping, set the player the jumping state and run the function to jump
        if (keys[pygame.K_SPACE]or keys[pygame.K_w]) and game_logic.jumping == False:
            game_logic.jumping = True
    
        if game_logic.jumping == True and game_logic.falling == False:
            if game_logic.jump_counter > 0:
                game_logic.delta_y -= 5
                game_logic.jump_counter -=5
                
    #shooting mechanics for the player that point at the mouse and initiate when the mouse is clicked                   
    def shoot(self, bullet_group, bullet_width, bullet_height):
        if time.time()-self.last_shoot >= 1.5:
            mouse_pos = pygame.mouse.get_pos()
            direction = pygame.math.Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
            if direction.length() != 0:
                direction.normalize_ip()

            # Calculate the starting position of the bullet based on the player's current position
            bullet_start_x = self.rect.centerx - (bullet_width // 2)
            bullet_start_y = self.rect.centery - (bullet_height // 2)

            bullet = enemy.Bullet(bullet_start_x, bullet_start_y, bullet_width, bullet_height, direction,pygame.image.load('img/knife.png') )
            bullet_group.add(bullet)
            self.last_shoot = time.time()
        
    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    #detecting player bullets hitting the environment
    def bullet_detect_env(self, bullet_group, bullet_col): 
        bullets_to_remove = []
        for bullet in bullet_group.sprites():  # Iterate over sprites in the group
            for tile in bullet_col:
                if bullet.rect.colliderect(tile[1]):  # Assuming tile is a pair (image, rect)
                    bullets_to_remove.append(bullet)
        for bullet in bullets_to_remove:
            bullet_group.remove(bullet)

    #logic to kill enemies if bullets hit them
    def kill_enemy(self, bullet_group, enemy_group,shooting_sprite):
        for bullet in bullet_group.sprites():
            for badguy in enemy_group.sprites():
                if bullet.rect.colliderect(badguy):
                    if badguy in shooting_sprite:
                            badguy.disable_shooting()
                    badguy.not_alive()
                    badguy.kill()
                    bullet.kill()
                
                    
                    

    # Update the sprite's position
    def update(self, column, top, bot,single):
        #detecting if the player is falling so that they cannot jump when falling. This was an issue when falling off the columns. The 1.9 value comes from the normal difference between values being 2
        if game_logic.player_pos[1] - game_logic.y_detect > 1.99:
            game_logic.falling = True
        
        game_logic.y_detect = game_logic.player_pos[1]

        #setting variables to base values so 
        self.collision = False
        game_logic.delta_x = 0
        game_logic.delta_y = 0
        game_logic.dummy_x = game_logic.player_pos[0]
        game_logic.dummy_y = game_logic.player_pos[1]


          #player movement
        keys = pygame.key.get_pressed()
  
        if keys[pygame.K_a]:
            game_logic.delta_x -= 2
        if keys[pygame.K_d]:
            game_logic.delta_x += 2


        if self.collision == False:
            if game_logic.player_pos[1] < 615:
                game_logic.delta_y += game_logic.gravity
            
            else:
                # Character has landed, reset fall speed
                game_logic.fall = 0
                game_logic.jumping = False
                game_logic.falling = False
                game_logic.jump_counter = game_logic.jump_height


        
        #Stopping the player from falling through the floor.
        if game_logic.player_pos[1] >= 615:
            game_logic.player_pos[1] = 615
        
        #placing wall boundaries 
        if game_logic.player_pos[0] >= 1370:
            game_logic.player_pos[0] = 1370
        
        if game_logic.player_pos[0] <= 0:
            game_logic.player_pos[0] = 0

    
        

       
        game_logic.dummy_x = game_logic.dummy_x + game_logic.delta_x
        game_logic.dummy_y = game_logic.dummy_y + game_logic.delta_y

        self.player_collide(column, top, bot,single) 

        self.player_jump()

        game_logic.player_pos[0] = game_logic.player_pos[0] + game_logic.delta_x
        game_logic.player_pos[1] = game_logic.player_pos[1] + game_logic.delta_y
        self.dummy_rect = pygame.Rect(game_logic.dummy_x,game_logic.dummy_y,30,40)
        #update rectangle position
        self.rect = character_image.get_rect()
        self.rect.x = game_logic.player_pos[0]
        self.rect.y = game_logic.player_pos[1]


        
        

class WorldMap():
    def __init__(self, map, tile_size):

        # Load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grassblock.jpg')
        colbase_img = pygame.image.load('img/col_base.png')
        colbod_img = pygame.image.load('img/col_body.png')
        coltoprt_img = pygame.image.load('img/col_top_right.png')
        coltoplt_img = pygame.image.load('img/col_top_left.png')
        coltopmid_img = pygame.image.load('img/col_mid_top.png')
        wave_1 = pygame.image.load('img/wave1.png')
        wave_2 = pygame.image.load('img/wave2.png')
        wave_3 = pygame.image.load('img/wave3.png')
        water_img = pygame.image.load('img/water.png')
        door_img = pygame.image.load('img/door.png')



        water_images = [
            pygame.transform.scale(pygame.image.load('img/wave1.png'), (tile_size, tile_size)),
            pygame.transform.scale(pygame.image.load('img/wave2.png'), (tile_size, tile_size)),
            pygame.transform.scale(pygame.image.load('img/wave3.png'), (tile_size, tile_size)),
        ]

        self.waves_iter = iter(cycle(water_images))

        
        # Initialize empty tile list
        self.tile_list = []

        #make a list of columns to deal with side and top collision
        self.col_collide = []
        self.col_top = []
        self.bullet_col = []
        self.col_bot = []
        self.col_single = []
        self.door = []

        # Loop over each map element and 
        # assing it the correct image
        row_count = 0
        for row in map:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.bullet_col.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(colbase_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.col_collide.append(img_rect)
                    self.bullet_col.append(tile)
                    self.col_bot.append(img_rect)
                if tile == 4:
                    img = pygame.transform.scale(colbod_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.col_collide.append(img_rect)
                    img1 = pygame.transform.scale(colbod_img, (tile_size-7, tile_size)) #used to offset the image but maintain the rect collision
                    img1_rect = img1.get_rect()
                    img1_rect.x = col_count * tile_size + 3.5
                    img1_rect.y = row_count * tile_size
                    tile = [img1, img1_rect]
                    self.tile_list.append(tile)
                    self.bullet_col.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(coltoprt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.col_collide.append(img_rect)
                    self.col_top.append(img_rect)
                    self.bullet_col.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(coltoplt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.col_collide.append(img_rect)
                    self.col_top.append(img_rect)
                    self.bullet_col.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(coltopmid_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.col_collide.append(img_rect)
                    self.col_top.append(img_rect)
                    self.bullet_col.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(wave_1, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                if tile == 9:
                    img = pygame.transform.scale(water_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                if tile == 10:
                    img = pygame.transform.scale(coltopmid_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.col_collide.append(img_rect)
                    self.col_single.append(img_rect)
                    self.bullet_col.append(tile)
                if tile == 11:
                    img = pygame.transform.scale(door_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.door.append(img_rect)
    
                col_count += 1
            row_count += 1

    


    def draw(self,screen):
        for tiles in self.tile_list:
            #if tile == 6:
                # Use the next image from the cyclic iterator
             #   tiles[0] = next(self.waves_iter)
            screen.blit(tiles[0], tiles[1])


#creating a starting screen with a button
class StartScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 55)
        self.title_font = pygame.font.Font(None, 72)
        self.title_text = self.title_font.render("Cesar's Scramble!", True, (255, 0, 0))
        self.start_button_rect = pygame.Rect(game_logic.window_size[0]/2-100, game_logic.window_size[1]/2-25, 200, 50)
        self.start_button_text = self.font.render("Start Game", True, (255, 255, 255))
        self.start_background = pygame.image.load('img/background.jpeg')
        self.start_background = pygame.transform.scale(self.start_background,(game_logic.window_size[0],game_logic.window_size[1]))
    def draw(self, screen):
        screen.blit(self.start_background, (0,0))
        screen.blit(self.title_text, (500, 100))
        pygame.draw.rect(screen, (0, 128, 255), self.start_button_rect)
        screen.blit(self.start_button_text, self.start_button_rect.topleft)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.start_button_rect.collidepoint(x, y):
                return True
        return False
    


class GameOver():
    def __init__(self,screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.Font(None, 36)
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.restart_text = self.font.render("Press R to restart", True, (255, 255, 255))
        self.quit_text = self.font.render("Press Q to quit", True, (255, 255, 255))
        self.clock = pygame.time.Clock()

    def show_game_over_screen(self):
        while True:
            pygame.mixer.music.stop()
            play_lose_sound_effect()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        subprocess.run(["python3", "main.py"])
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.game_over_text, (self.screen_width // 2 - self.game_over_text.get_width() // 2, 100))
            self.screen.blit(self.restart_text, (self.screen_width // 2 - self.restart_text.get_width() // 2, 200))
            self.screen.blit(self.quit_text, (self.screen_width // 2 - self.quit_text.get_width() // 2, 250))

            pygame.display.flip()
            self.clock.tick(60)


class Level:
    def __init__(self, map, walkers,shooters):
        self.world_map = map
        self.walkers = walkers
        self.shooters = shooters
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(walkers.sprites())
        self.all_sprites.add(shooters.sprites())

class Game:
    def __init__(self,levels,tile_size):
        self.levels = levels
        self.current_level = 0
    
        self.level_shown = self.levels[self.current_level]
        self.current_map = WorldMap(self.level_shown.world_map,tile_size)
        self.has_switched_level = False

    def load_level(self,screen,shooters,walkers,all):
        self.level_shown.all_sprites.draw(screen)
        shooters.add(self.level_shown.shooters)
        walkers.add(self.level_shown.walkers)
        all.add(self.level_shown.all_sprites)
        
    def update(self,player,door,shooters,walkers,all,screen, tile_size,youwin):
        door_collision_flag = False
        
        # Check for door collision
        for open in door:
            if open.colliderect(player):
                door_collision_flag = True
                break

        # Switch level if door collision detected and flag is not already set
        if door_collision_flag and not self.has_switched_level:
            if self.current_level+1 == len(self.levels):
                youwin.show_you_win_screen()
            else: 
                self.current_level = self.current_level + 1
            
            # Kill all sprites in the groups
            for shooter in shooters:
                shooter.kill()

            for walker in walkers:
                walker.kill()

            for sprite in all:
                sprite.kill()
            # Update self.level_shown to point to the new level object
            self.level_shown = self.levels[self.current_level]
            self.current_map = WorldMap(self.level_shown.world_map,tile_size)
            # Set flag to prevent multiple level switches
           
            self.load_level(screen,shooters,walkers,all)

            self.has_switched_level = False
            

class YouWin:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.Font(None, 36)
        self.you_win_text = self.font.render("You Win!", True, (255, 255, 255))
        self.quit_text = self.font.render("Press Q to quit", True, (255, 255, 255))
        self.clock = pygame.time.Clock()

    def show_you_win_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.you_win_text, (self.screen_width // 2 - self.you_win_text.get_width() // 2, 100))
            self.screen.blit(self.quit_text, (self.screen_width // 2 - self.quit_text.get_width() // 2, 200))

            pygame.display.flip()
            self.clock.tick(60)

def init_music():
    pygame.mixer.init()
    game_music = pygame.mixer.music.load('img/title_music.mp3')
    pygame.mixer.music.play(-1)  # Play music in a loop
   

def play_lose_sound_effect():
    sound = pygame.mixer.Sound('img/womp-womp.mp3')
    sound.set_volume(0.5)  # Adjust volume as desired
    sound.play()


class Star():
    def __init__(self,x, y, width, height, image):
        super().__init__()
        self.star_sprite = enemy.Characters(x, y, width, height, image)
        self.rect = self.star_sprite.rect