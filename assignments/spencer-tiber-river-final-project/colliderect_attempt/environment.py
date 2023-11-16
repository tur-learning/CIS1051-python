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
character_image = pygame.image.load('img/red.png')  # Replace 'character.png' with the file path of your character's image

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
        self.collision = False
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]
        
    def player_collide(self, column, top):
            dummy_rect = pygame.Rect(game_logic.dummy_x,game_logic.dummy_y,30,40)
            for tile in column:
                for i in top:
                    if dummy_rect.colliderect(tile):
                        self.collision = True
                        if game_logic.dummy_y + 37 < i.y:
                            game_logic.delta_y = 0
                            game_logic.jumping = False
                            game_logic.player_pos[1] = i.y - 40.01
                        else:
                            game_logic.delta_x = 0
                            

            

    # Update the sprite's position
    def update(self, column, top):
        
        self.collision = False
        game_logic.delta_x = 0
        game_logic.delta_y = 0
        game_logic.dummy_x = game_logic.player_pos[0]
        game_logic.dummy_y = game_logic.player_pos[1]
          #player movement
        keys = pygame.key.get_pressed()
  
        if keys[pygame.K_a]:
            game_logic.delta_x -= 3
        if keys[pygame.K_d]:
            game_logic.delta_x += 3
        #if the space bar is hit and the player is not jumping, set the player the jumping state and run the function to jump
        if (keys[pygame.K_SPACE]or keys[pygame.K_w]) and game_logic.jumping == False:
            game_logic.jumping = True
        
        if game_logic.jumping == True:
            if game_logic.jump_counter > 0:
                game_logic.delta_y -= 5
                game_logic.jump_counter -=5

        if self.collision == False:
            if game_logic.player_pos[1] < 465:
                game_logic.delta_y += game_logic.gravity
            
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

       
       
        game_logic.dummy_x = game_logic.dummy_x + game_logic.delta_x
        game_logic.dummy_y = game_logic.dummy_y + game_logic.delta_y

        self.player_collide(column, top)

        game_logic.player_pos[0] = game_logic.player_pos[0] + game_logic.delta_x
        game_logic.player_pos[1] = game_logic.player_pos[1] + game_logic.delta_y
        


        
        

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
        self.col_collide = []
        self.col_top = []
        self.bullet_col = []

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
                if tile == 4:
                    img = pygame.transform.scale(colbod_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.col_collide.append(img_rect)
                    self.bullet_col.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(coltop_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                    self.col_collide.append(img_rect)
                    self.col_top.append(img_rect)
                    self.bullet_col.append(tile)
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
    


                   
   