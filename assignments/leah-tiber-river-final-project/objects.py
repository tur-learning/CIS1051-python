import pygame
import random

class Boat():

    def __init__(self, boat, x, y, game_manager, boat_width, boat_height, screen_width):
        original_image = pygame.image.load(boat)
        self.boat = pygame.transform.scale(original_image, (boat_width, boat_height))
        self.rect = self.boat.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game_manager = game_manager
        self.screen_width = screen_width
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.game_over_font_render = pygame.font.Font(pygame.font.get_default_font(), 100)
        self.game_over = False
        self.points = 0

    def move(self, keys, tiles, rock_group):
        self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x > self.screen_width:
            for rock in rock_group:
                rock.regenerate()
            self.rect.x = 0
	
        #check for collision with trash
        tile_size = 100
        tile_x = int(self.rect.x / tile_size)
        tile_y = int(self.rect.y / tile_size)
        
        if 0 <= tile_y < len(tiles) and 0 <= tile_x < len(tiles[0]) and tiles[tile_y][tile_x] == 0:
            self.game_over = True
    
    def handle_collision(self):
        self.points += 10
        print(f"Trash collected! Points: {self.points}")
    
    def handle_collision_rock(self):
        self.game_over = True
        self.game_manager.game_over = True       
    
    def display_game_over_screen(self):
        self.game_manager.display_game_over_screen()        
   
    def draw (self, screen):
        screen.blit(self.boat, self.rect)



class GameManager:
    def __init__(self, screen, screen_width):
        self.screen = screen
        self.screen_width = screen_width
        
    def display_game_over_screen(self):
        game_over_font_render = pygame.font.Font(pygame.font.get_default_font(), 100)
        game_over_text = game_over_font_render.render("Game Over", True, (255, 255, 255))

        self.screen.fill((0, 0, 0))  # Fill the screen with black
        self.screen.blit(game_over_text, (self.screen_width // 2 - 200, self.screen_width // 2 - 50))
        pygame.display.flip()
            
    
            
class Trash(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width, tile_size, tiles):
        super().__init__()
        self.trash_types = ["objects/bottle.png", "objects/cig.png", "objects/twig.png"]
        original_image = pygame.image.load(random.choice(self.trash_types))
        self.image = pygame.transform.scale(original_image, (0.5*tile_size, 0.5*tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_width = screen_width
        self.tiles = tiles
        self.tile_size = tile_size
        self.trash_counter = 0
        
    
            
    def generate_trash(self):
        x = 0
        y = random.uniform(self.tile_size, (len(self.tiles) - 2)*self.tile_size)
        self.__init__(x, y, self.screen_width, self.tile_size, self.tiles)

          
                
    def update(self):
        self.rect.x += 5
        if self.rect.x > self.screen_width:
            self.rect.x = 0
            self.generate_trash()

            
class Rock(pygame.sprite.Sprite):
    def __init__ (self, x, y, screen_width, tile_size, tiles):
        super().__init__()
        original_image = pygame.image.load("objects/rock.png")
        self.image = pygame.transform.scale(original_image, (int(0.5 * tile_size), int(0.5 * tile_size)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_width = screen_width
        self.tiles = tiles
        self.tile_size = tile_size
        
    def regenerate(self):
        x = random.uniform(0, self.screen_width)
        y = random.uniform(self.tile_size, (len(self.tiles) - 2)*self.tile_size)
        self.__init__(x, y, self.screen_width, self.tile_size, self.tiles)
        
    def update(self):
        pass 
        #self.rect.x += 5
        #if self.rect.x > self.screen_width:
            #self.rect.x = 0
            
            #tile_x = int(self.rect.x / self.tile_size)
            #tile_y = int(self.rect.y / self.tile_size)
            #if 0 <= tile_y < len(self.tiles) and 0 <= tile_x < len(self.tiles[0]) and self.tiles[tile_y][tile_x] == 0:
                #self.game_manager.game_over = True
                                       
    
          
