import pygame
import random
import math
import time

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, center_x, center_y, image_path):
        super().__init__()
        self.radius = radius
        self.surface = pygame.image.load(image_path).convert_alpha()
        # Scale the planet surface to the appropriate size
        self.scaled_surface = pygame.transform.scale(self.surface, (1000/self.radius, 1000/self.radius))
        # Get the rect for the scaled surface
        self.rect = self.scaled_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.center_x = center_x
        self.center_y = center_y
        self.angle = 0
    
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

    def randomize_position(self, screen_width, screen_height):
        self.rect.x = random.randint(self.radius, screen_width - self.radius)
        self.rect.y = random.randint(self.radius, screen_height - self.radius)

    def move_around(self, speed):
        # Update the angle
        self.angle += speed % (2*math.pi)
        # Calculate the new x and y position based on the angle and radius
        self.rect.centerx = int(self.center_x + 10*self.radius * math.cos(math.radians(self.angle)))
        self.rect.centery = int(self.center_y + 10*self.radius * math.sin(math.radians(self.angle)))

    def collide(self, other, x, y):
        abs_rect = other.rect.copy()
        abs_rect.x += x
        abs_rect.y += y
        #print("x1 = ", x, ",  y1 = ", y)
        #print("recta: ",abs_rect)
        #print("alien: ", self.rect.topleft)
        if pygame.Rect.colliderect(self.rect, abs_rect):
            self.handle_collision(other)

    def destroy(self, other):
        pass

    def handle_collision(self, other):
        pass # Do nothing by default

class Planet(GameObject):
    def __init__(self, x, y, radius, center_x, center_y, image_path):
        super().__init__(x, y, radius, center_x, center_y, image_path)

    def handle_collision(self, other):
        pass # Do nothing

class Enemy(GameObject):
    def __init__(self, x, y, radius, center_x, center_y, image_path):
        super().__init__(x, y, radius, center_x, center_y, image_path)

    def handle_collision(self, other):
        if isinstance(other, Bullet):
            self.kill()
        if isinstance(other, Spaceship):
            time.sleep(2)
            pygame.quit()
            other.kill()

class Spaceship(GameObject):
    def __init__(self, x, y, radius, center_x, center_y, image_path, center):
        super().__init__(x, y, radius, center_x, center_y, image_path)
        self.rect.center = center
        self.rect.left = self.rect.centerx - 0.5*self.rect.width
        self.rect.top = self.rect.centery - 0.5*self.rect.height
        self.points = 0

    def add_points(self, points):
        self.points += points

    def draw(self, surface):
        surface.blit(self.surface, (self.rect.left, self.rect.top))

    def handle_collision(self, other):
        if isinstance(other, Planet):
            self.add_points(self.points)

class Bullet(GameObject):
    def __init__(self, x, y, radius, center_x, center_y, image_path):
        super().__init__(x, y, radius, center_x, center_y, image_path)
        self.moving = False
        self.speed = 1
        self.dt = 30.
        self.end_pos = (0,0)
        self.direction = (0,0)

    def fire(self, position):
        self.moving = True
        start_pos = self.rect.center
        self.end_pos = position
        self.direction = pygame.math.Vector2(self.end_pos) - pygame.math.Vector2(start_pos)

    def draw(self, surface):
        if self.moving:
            # Move the shot toward the clicked position over time
            distance = self.direction.normalize() * self.speed * self.dt
            self.rect.move_ip(distance)
            surface.blit(self.scaled_surface, self.rect)

        # Check if the shot has reached the clicked position
        if self.rect.collidepoint(self.end_pos):
            self.moving = False
            self.rect.center = surface.get_rect().center

class Crosshair(GameObject):
    def __init__(self, x, y, radius, center_x, center_y, image_path):
        super().__init__(x, y, radius, center_x, center_y, image_path)
        self.left = self.surface.get_rect().left
        self.bottom = self.surface.get_rect().bottom

    def draw(self, surface, position):
        # Center the target sprite at the mouse position
        self.rect.center = position
        surface.blit(self.scaled_surface, self.rect)