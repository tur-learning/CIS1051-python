import pygame

class WorldMap():
    def __init__(self, map, tile_size):
        # Load images
        brick_img = pygame.image.load('img/brick.png')
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')

        # Initialize empty tile list
        self.tile_list = []

        # Loop over each map element and 
        # assing it the correct image
        row_count = 0
        for row in map:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(brick_img, (tile_size, tile_size))
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
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = [img, img_rect]
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])