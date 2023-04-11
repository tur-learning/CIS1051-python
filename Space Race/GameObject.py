import pygame
import math
import time

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.radius = radius
        self.image = pygame.image.load(image_path).convert_alpha()

    def draw(self, surface):
        surface.blit(self.image, (self.x_coordinate - self.radius, self.y_coordinate - self.radius))
    
    def move():
        pass
    
    def collide():
        pass
    
    def handle_collision(self, other):
        pass
    
    def save(self, file_name, object_data):
        object_data = shelve.open("file_name")
        object_data["x_coordinate"] = self.x_coordinate
        object_data["y_coordinate"] = self.y_coordinate
        object_data["radius"] = self.radius
        object_data.close()


class Planet(GameObject):
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        super().__init__(x_coordinate, y_coordinate, radius, image_path)
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))

class Enemy(GameObject):
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        super().__init__(x_coordinate, y_coordinate, radius, image_path)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(self.image, (radius * 4, radius * 2))
        self.rect = self.image.get_rect()
        self.center_x = x_coordinate
        self.center_y = y_coordinate
        self.angle = 0

    def move(self, dt):
        self.angle += 0.01 * dt
        self.angle %= 2 * math.pi
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)
        self.rect.center = (self.x, self.y)

    def collide(self, other, x, y):
        abs_rect = other.rect.copy()
        abs_rect.x += x
        abs_rect.y += y
        print("recta:", abs_rect)
        print("alien:", self.rect.topleft)
        if pygame.Rect.colliderect(self.rect, abs_rect):
            print("Handling collision")
            self.handle_collision(other)

    def handle_collision(self, other):
        if isinstance(other, Shot):
            self.kill()
        if isinstance(other, Spaceship):
            time.sleep(2)
            pygame.quit()
            other.kill()
    
    def save(self, file_name, object_data):
        super().save(self, file_name, object_data, center_x, center_y, angle)
        object_data = shelve.open("file_name")
        object_data["center_x"] = self.center_x
        object_data["center_y"] = self.center_y
        object_data["angle"] = self.angle
        object_data.close()


    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)


class Spaceship(GameObject):
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        super().__init__(x_coordinate, y_coordinate, radius, image_path)
        self.image = pygame.transform.scale(self.image, (radius * 4, radius * 2))
        self.rect = self.image.get_rect()
        self.angle = 0

    def rotate(self, target_x, target_y):
        dx = target_x - (self.x_coordinate + self.image.get_width() / 2)
        dy = target_y - (self.y_coordinate + self.image.get_height() / 2)
        self.angle = math.atan2(dy, dx)

    def get_rotated_image(self):
        rotated_image = pygame.transform.rotate(self.image, -math.degrees(self.angle))
        return rotated_image
    
    def get_height(self):
        return self.image.get_height()
    
    def get_width(self):
        return self.image.get_width()

    def save(self, file_name, object_data):
        super().save(self, file_name, object_data, angle)
        object_data = shelve.open("file_name")
        object_data.close()

    def draw(self, surface):
        rotated_image = self.get_rotated_image()
        rect = rotated_image.get_rect(center=(self.x_coordinate + self.image.get_width() / 2, self.y_coordinate + self.image.get_height() / 2))
        surface.blit(rotated_image, rect.topleft)


class Crosshair(GameObject):
    def __init__(self, x_coordinate, y_coordinate, width, height, image_path):
        super().__init__(x_coordinate, y_coordinate, 0, image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
    
    def save(self, file_name, object_data):
        super().save(self, file_name, object_data, width, height)
        object_data = shelve.open("file_name")
        object_data["width"] = self.width
        object_data["height"] = self.height
        object_data.close()


class Shot(GameObject):
    def __init__(self, x_coordinate, y_coordinate, width, height, image_path):
        super().__init__(x_coordinate, y_coordinate, 0, image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.direction = pygame.math.Vector2(0, 0)

    def set_direction(self, start_pos, target_pos):
        self.direction = pygame.math.Vector2(target_pos) - pygame.math.Vector2(start_pos)
        self.direction = self.direction.normalize()

    def move(self, speed):
        self.x_coordinate += self.direction.x * speed
        self.y_coordinate += self.direction.y * speed
        self.rect.topleft = (self.x_coordinate, self.y_coordinate)

    def is_out_of_bounds(self, window_width, window_height):
        return self.x_coordinate < 0 or self.x_coordinate > window_width or self.y_coordinate < 0 or self.y_coordinate > window_height

    def save(self, file_name, object_data):
        super().save(self, file_name, object_data, width, height, direction)
        object_data = shelve.open("file_name")
        object_data["width"] = self.width
        object_data["height"] = self.height
        object_data["direction"] = self.direction
        object_data.close()

'''

- Implement collision check with collide method and handle collision with the other method    " alien.collide(shot) "
        - Define a group of sprites

- Use a list to serialize
- Deserialization (be able to load in data), means we have to add a new option to the menu called load

'''