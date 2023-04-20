import pygame
import random
import math
import game

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, image_path):
        super().__init__()
        self.radius = radius
        self.path = image_path
        self.surface = pygame.image.load(image_path).convert_alpha()
        # Compute ratio of height to width to scale a surface proportionally
        r = self.surface.get_height()/self.surface.get_width()
        # Scale the planet surface to the appropriate size
        self.scaled_surface = pygame.transform.scale(self.surface, (1000/self.radius, r*1000/self.radius))
        # Get the rect for the scaled surface
        self.rect = self.scaled_surface.get_rect()
        #self.rect.x = x
        #self.rect.y = y
        self.rect.center = (x, y)
        self.center_x = x
        self.center_y = y
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

    #def randomize_position(self, screen_width, screen_height):
    #    self.rect.x = random.randint(self.radius, screen_width - self.radius)
    #    self.rect.y = random.randint(self.radius, screen_height - self.radius)

    def move_around(self, speed, a=2, b=2):
        # Update the angle
        self.angle += speed % 360
        # Calculate the new x and y position based on the angle and radius
        self.rect.centerx = int(self.center_x + a*self.radius * math.cos(math.radians(self.angle)))
        self.rect.centery = int(self.center_y + b*self.radius * math.sin(math.radians(self.angle)))

    def collide(self, other, x, y):
        abs_rect = other.rect.copy()
        abs_rect.x += x
        abs_rect.y += y
        if pygame.Rect.collidepoint(self.rect, abs_rect.center):
            self.handle_collision(other)

    def destroy(self, other):
        pass

    def handle_collision(self, other):
        pass # Do nothing by default

    def save(self):
        data = {"radius"   : self.radius, 
                "rect"     : self.rect, 
                "path"     : self.path, 
                "center_x" : self.center_x, 
                "center_y" : self.center_y, 
                "angle"    : self.angle}
        return data

    def load(self, data):
        self.radius = data["radius"]
        self.rect = data["rect"]
        self.path = data["path"]
        self.center_x = data["center_x"]
        self.center_y = data["center_y"]
        self.angle = data["angle"]

class Planet(GameObject):
    def __init__(self, x, y, radius, n_enemies, image_path):
        super().__init__(x, y, radius, image_path)
        n_gems = 3
        self.aliens = [Enemy(x, y, 20, 360*i/10, "enemy.png") for i in range(n_enemies)]
        self.gems = [Gem(x, y, 20, 360*i/n_gems, "diamond.png") for i in range(n_gems)]

    def handle_collision(self, other):
        pass # Do nothing

    def save(self):
        data = super().save()
        # Adding aliens serialization
        for index, alien in enumerate(self.aliens):
            data["alien"+str(index)] = alien.save()
        return data

    def load(self, data):
        super().load(data)
        # Adding aliens de-serialization
        for index, alien in enumerate(self.aliens):
            alien.load(data["alien"+str(index)])

class Enemy(GameObject):
    def __init__(self, x, y, radius, angle, image_path):
        super().__init__(x, y, radius, image_path)
        self.speed = random.randint(1,4)
        self.a = random.randint(1,10)
        self.b = random.randint(1,10)
        self.angle = angle

    def move_around(self):
        super().move_around(self.speed, self.a, self.b)

    def handle_collision(self, other):
        if isinstance(other, Bullet):
            self.kill()
        if isinstance(other, Spaceship):
            other.kill()

class Gem(GameObject):
    def __init__(self, x, y, radius, angle, image_path):
        super().__init__(x, y, radius, image_path)
        self.speed = 1
        self.angle = angle

    def move_around(self):
        super().move_around(self.speed)

    def handle_collision(self, other):
        if isinstance(other, Spaceship):
            self.kill()
            game.Session.increase_score()

class Spaceship(GameObject):
    def __init__(self, x, y, radius, image_path, center):
        super().__init__(x, y, radius, image_path)
        self.rect.center = center
        self.rect.left = self.rect.centerx - 0.5*self.rect.width
        self.rect.top = self.rect.centery - 0.5*self.rect.height
        self.killed = False

    def rotate(self, target_x, target_y):
        dx = target_x - (self.rect.centerx)# + self.surface.get_width()) / 2
        dy = target_y - (self.rect.centery)# + self.surface.get_height()) / 2
        self.angle = math.atan2(dy, dx) + math.pi/2

    def get_rotated_image(self):
        rotated_image = pygame.transform.rotate(self.scaled_surface, -math.degrees(self.angle))
        return rotated_image

    #def draw(self, surface):
    #    surface.blit(self.scaled_surface, (self.rect.left, self.rect.top))
    def draw(self, surface):
        rotated_image = self.get_rotated_image()
        self.rect = rotated_image.get_rect(center=(self.rect.centerx, self.rect.centery))
        surface.blit(rotated_image, self.rect.topleft)

    def kill(self):
        self.killed = True

    def handle_collision(self, other):
        if isinstance(other, Planet):
            self.add_points(self.points)

class Bullet(GameObject):
    def __init__(self, x, y, radius, image_path):
        super().__init__(x, y, radius, image_path)
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
    def __init__(self, x, y, radius, image_path):
        super().__init__(x, y, radius, image_path)
        self.left = self.surface.get_rect().left
        self.bottom = self.surface.get_rect().bottom

    def draw(self, surface, position):
        # Center the target sprite at the mouse position
        self.rect.center = position
        surface.blit(self.scaled_surface, self.rect)