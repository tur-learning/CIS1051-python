import main
import pygame
import time
import math
import game_logic


#TODO
#make place for bad guy to stand
#make some sort of roman picture background that is light enough to see character
#I NEED TO FIX THE COLLISION WITH THE TOP OF THE COLUMN
    
    #making the character a little julius cesar
character_image = pygame.image.load('img/julius cesar.png')  # Replace 'character.png' with the file path of your character's image

    #establishing character dimensions and scaling the image accordingly
character_width = 30  
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
    

    # Update the sprite's position
    def update(self,collision):
       
        

          #player movement
        keys = pygame.key.get_pressed()
  
        if keys[pygame.K_a]:
            game_logic.player_pos[0] -= 5
                
        if keys[pygame.K_d]:
            game_logic.player_pos[0] += 5
     
        #if the space bar is hit and the player is not jumping, set the player the jumping state and run the function to jump
        if (keys[pygame.K_SPACE]or keys[pygame.K_w]) and not game_logic.jumping:
            game_logic.jumping = True
        
        if game_logic.jumping == True:
            if game_logic.jump_counter > 0:
                game_logic.player_pos[1] -= 5
                game_logic.jump_counter -=5


        if collision == False:
            if game_logic.player_pos[1] < 465:
                game_logic.player_pos[1] += game_logic.gravity
            
            else:
            # Character has landed, reset fall speed
                game_logic.fall = 0
                game_logic.jumping = False
                game_logic.jump_counter = game_logic.jump_height

        
        #Stopping the player from falling through the floor.
        if game_logic.player_pos[1] >= 465:
            game_logic.player_pos[1] = 465
        
        #placing wall boundaries 
        if game_logic.player_pos[0] >= 970:
            game_logic.player_pos[0] = 970
        
        if game_logic.player_pos[0] <= 0:
            game_logic.player_pos[0] = 0

       
        #update rectangle position
        self.char_rect = character_image.get_rect()
        self.char_rect.x = game_logic.player_pos[0]
        self.char_rect.y = game_logic.player_pos[1]




#I'm gonna tile map this whole fuckin thing
class WorldMap():
    def __init__(self, map, tile_size):

        # Load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grassblock.jpg')
        colbase_img = pygame.image.load('img/column_base.png')
        colbod_img = pygame.image.load('img/column_body.png')
        coltop_img = pygame.image.load('img/column_top.png')
        waves_img = pygame.image.load('img/water_00.gif')
        water_img = pygame.image.load('img/water.png')

        # Initialize empty tile list
        self.tile_list = []

        #make a list of columns to deal with side and top collision
        self.rt_side_col = []
        self.lt_side_col = []
        self.top_side_col = []

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
                    new_data_rt = [img_rect.x,img_rect.y],[img_rect.x,img_rect.y + tile_size]
                    new_data_lt = [img_rect.x + tile_size,img_rect.y],[img_rect.x + tile_size,img_rect.y + tile_size]
                    self.rt_side_col.append(new_data_rt)
                    self.lt_side_col.append(new_data_lt)
                if tile == 4:
                    img = pygame.transform.scale(colbod_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    new_data_rt = [img_rect.x,img_rect.y],[img_rect.x,img_rect.y + tile_size]
                    new_data_lt = [img_rect.x + tile_size,img_rect.y],[img_rect.x + tile_size,img_rect.y + tile_size]
                    self.rt_side_col.append(new_data_rt)
                    self.lt_side_col.append(new_data_lt)
                if tile == 5:
                    img = pygame.transform.scale(coltop_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    new_data_rt = [img_rect.x,img_rect.y],[img_rect.x,img_rect.y + tile_size]
                    new_data_lt = [img_rect.x + tile_size,img_rect.y],[img_rect.x + tile_size,img_rect.y + tile_size]
                    new_data_top = [img_rect.x+10,img_rect.y],[img_rect.x + tile_size-10,img_rect.y] #adjust the lists a little to stop the character from getting stuck on the way up
                    self.rt_side_col.append(new_data_rt)
                    self.lt_side_col.append(new_data_lt)
                    self.top_side_col.append(new_data_top)
                if tile == 6:
                    img = pygame.transform.scale(waves_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(water_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    


    def draw(self,screen):
        for tiles in self.tile_list:
            screen.blit(tiles[0],tiles[1])
    

    def collision_rt(self,character):
        for item in self.rt_side_col:
            for i in range(0, len(item), 2):
                pair1 = item[i]
                pair2 = item[i+1]
                if character.clipline(pair1,pair2):
                    game_logic.player_pos[0] = pair1[0]-30
    
    def collision_lt(self,character):
        for item in self.lt_side_col:
            for i in range(0, len(item), 2):
                pair1 = item[i]
                pair2 = item[i+1]
                if character.clipline(pair1,pair2):
                    game_logic.player_pos[0] = pair1[0]

    def collision_top(self,character,col):
        for item in self.top_side_col:
            for i in range(0, len(item), 2):
                pair1 = item[i]
                pair2 = item[i+1]
                if character.clipline(pair1,pair2):
                    game_logic.player_pos[1] = pair1[1]
                    col = True
                    return col
                   
                    