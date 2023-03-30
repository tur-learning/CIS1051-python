import pygame
import random
import math

class Planet:
    def __init__(self, x, y, radius, center_x, center_y, image_path):
        self.x = x
        self.y = y
        self.radius = radius
        self.surface = pygame.image.load(image_path).convert_alpha()
        self.angle = 0
        self.center_x = center_x
        self.center_y = center_y
    
    def draw(self, surface):
        # Scale the planet surface to the appropriate size
        scaled_surface = pygame.transform.scale(self.surface, (self.radius*2, self.radius*2))
        # Get the rect for the scaled surface
        rect = scaled_surface.get_rect()
        # Set the rect's center to the planet's position
        rect.center = (self.x, self.y)
        # Blit the scaled surface onto the given surface
        surf_rect = surface.get_rect()

        rect.left   = (surf_rect.width  + rect.left) % surf_rect.width
        rect.top    = (surf_rect.height + rect.top) % surf_rect.height

        v1 = (rect.left, rect.top)
        v2 = (0, rect.top)
        v3 = (0, 0)
        v4 = (rect.left, 0)

        w2 = max(0, rect.right - surf_rect.right)
        w1 = rect.width - w2
        w3 = w2 ; w4 = w1

        h4 = max(0, rect.bottom - surf_rect.bottom)
        h1 = rect.height - h4
        h2 = h1 ; h3 = h4
            
        quad_1 = pygame.Rect((0,0), (w1, h1))
        quad_2 = pygame.Rect((w1,0), (w2, h2))
        quad_3 = pygame.Rect((w1,h1), (w3, h3))
        quad_4 = pygame.Rect((0,h1), (w4, h4))

        surface.blit(scaled_surface, v1, quad_1)
        surface.blit(scaled_surface, v2, quad_2)
        surface.blit(scaled_surface, v3, quad_3)
        surface.blit(scaled_surface, v4, quad_4)
    
    def randomize_position(self, screen_width, screen_height):
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)

    def move_around_circle(self, speed):
        # Update the angle
        self.angle += speed % (2*math.pi)
        # Calculate the new x and y position based on the angle and radius
        self.x = int(self.center_x + 6*self.radius * math.cos(math.radians(self.angle)))
        self.y = int(self.center_y + 6*self.radius * math.sin(math.radians(self.angle)))


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def randomize_position(self, screen_width, screen_height):
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
