import pygame

class Map:
    def __init__(self, x, y, dim_x, dim_y, zoom, image_path):
        self.x = x
        self.y = y
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.surface = pygame.image.load(image_path).convert()
        self.zoom = zoom
        #self.scaled_surface = pygame.image.load(image_path).convert_alpha()
        self.scaled_surface = pygame.transform.scale(self.surface, (self.dim_x*self.zoom, self.dim_y*self.zoom))
        # Get the rect for the scaled surface
        self.rect = self.scaled_surface.get_rect()
    
    def draw(self, surface):
        surf_rect = surface.get_rect()

        self.rect.left   = (surf_rect.width  + self.rect.left) % surf_rect.width
        self.rect.top    = (surf_rect.height + self.rect.top) % surf_rect.height

        v1 = (self.rect.left, self.rect.top)
        v2 = (0, self.rect.top)
        v3 = (0, 0)
        v4 = (self.rect.left, 0)

        w2 = max(0, self.rect.right - surf_rect.right)
        w1 = self.rect.width - w2
        w3 = w2 ; w4 = w1

        h4 = max(0, self.rect.bottom - surf_rect.bottom)
        h1 = self.rect.height - h4
        h2 = h1 ; h3 = h4
            
        quad_1 = pygame.Rect((0,0), (w1, h1))
        quad_2 = pygame.Rect((w1,0), (w2, h2))
        quad_3 = pygame.Rect((w1,h1), (w3, h3))
        quad_4 = pygame.Rect((0,h1), (w4, h4))

        surface.blit(self.scaled_surface, v1, quad_1)
        surface.blit(self.scaled_surface, v2, quad_2)
        surface.blit(self.scaled_surface, v3, quad_3)
        surface.blit(self.scaled_surface, v4, quad_4)
