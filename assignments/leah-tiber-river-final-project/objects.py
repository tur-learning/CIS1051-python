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

    def move(self, keys, tiles):
        self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x > self.screen_width:
            self.rect.x = 0
	
        #check for collision with rocks
        tile_size = 100
        tile_x = int(self.rect.x / tile_size)
        tile_y = int(self.rect.y / tile_size)
        
        if 0 <= tile_y < len(tiles) and 0 <= tile_x < len(tiles[0]) and tiles[tile_y][tile_x] == 0:
            self.display_game_over_screen()
    
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



class MySprite(pygame.sprite.Sprite):
    def __init__(self, trash_group, x, y, screen_width, tile_size):
        super().__init__()
        self.image = pygame.image.load("objects/bottle.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.trash_group = trash_group
        self.trash_types = ["objects/bottle.png", "objects/cig.png", "objects/twig.png"]
        self.screen_width = screen_width
        self.tile_size = tile_size
        
    def generate_trash(self, tiles):
        trash_types = ["objects/bottle.png", "objects/cig.png", "objects/twig.png"]
        for _ in range(5):
            x = random.randint(0, len(tiles[0]) - 1)
            y = random.randint(0, len(tiles) - 1)
            if tiles[y][x] == 1:
                trash_image_path = random.choice(trash_types)
                trash = MySprite(self.trash_group, x, y, self.screen_width, self.tile_size)
                self.trash_group.add(trash)
                
    def update(self, tiles):
        self.rect.x += 5
        if self.rect.x > self.screen_width:
            self.rect.x = 0
            self.generate_trash(tiles)
            
            