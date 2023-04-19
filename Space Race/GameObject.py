import pygame
import math
import time
from random import randint
import shelve
pygame.mixer.init()

'''
    GameObject is a base class for all game objects in the game
    (spaceship, enemy, planet, crosshair, and shot), and it inherits
    from pygame.sprite.Sprite. This class allows us to consolidate
    repeating code into one parent class, saving us time and redundnacy.
'''
class GameObject(pygame.sprite.Sprite):
    # Initialize the GameObject with coordinates, radius, and an image path
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.radius = radius
        self.image = pygame.image.load(image_path).convert_alpha()

    # Draw the GameObject on a given surface
    def draw(self, surface):
        surface.blit(self.image, (self.x_coordinate - self.radius, self.y_coordinate - self.radius))
    
    # Placeholder method for moving the GameObject (overridden in subclasses)
    def move():
        pass

    # Placeholder method for serializibg GameObjects in dictionaries (overridden in subclasses)
    def to_dict():
        pass
    
    # Load the object's state from the given data
    def load(self,data):
        # Iterate through key/value pairs
        for k, v in data.items():
            # Assign data dictionary items to actual object attributes
            setattr(self, k, v)


'''
    Planet is an inheriting class for the planet game object, and it 
    inherits from GameObject.py. This class allows us to create Planet
    objects, and implement specific funtions of the planet object, such
    as respawning, and converting object details into a dictionary for 
    serialization.
'''
class Planet(GameObject):
    # Initialize the planet with coordinates, radius, and an image path
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        super().__init__(x_coordinate, y_coordinate, radius, image_path)
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_coordinate, self.y_coordinate)

    # Respawn the planet at a random location within the specified range
    def respawn(self):
        self.x_coordinate=randint(300,2700)
        self.y_coordinate=randint(300,2900)
        self.rect.center = (self.x_coordinate, self.y_coordinate)

    # Convert the planet's state information to a dictionary    
    def to_dict(self):
        # Create dictionary that stores planet's current game state
        status = {
            "x_coordinate":self.x_coordinate,
            "y_coordinate":self.y_coordinate,
        }
        return status


'''
    Enemy is an inheriting class for the enemy game object, and it 
    inherits from GameObject.py. This class allows us to create Enemy
    objects, and implement specific funtions of the enemy object, such
    as respawning, moving, checking for a collision with a shot, checking
    for a collision with the user spaceship, and converting object details
    into a dictionary for serialization.
'''
class Enemy(GameObject):
    # Initialize the enemy object with coordinates, radius, and an image path
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        super().__init__(x_coordinate, y_coordinate, radius, image_path)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(self.image, (radius * 4, radius * 2))
        self.rect = self.image.get_rect()
        self.center_x = x_coordinate
        self.center_y = y_coordinate
        self.angle = 0
        self.is_alive = True

    # Respawn the enemy at a random location within the specified range
    def respawn(self):
        self.center_x=randint(300,2700)
        self.center_y=randint(300,2900)
        self.is_alive=True

    # Update the enemy's position based on its angle and radius.
    def move(self, dt):
        self.angle += 0.01 * dt
        self.angle %= 2 * math.pi
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)
        self.rect.center = (self.x, self.y)

    # Check if the enemy collides with a shot
    def handle_shot_collision(self, shot, x, y):
        enemy_killed_sound = pygame.mixer.Sound('Enemy.mp3')
        abs_rect = shot.rect.copy()
        abs_rect.x = (3000  + x + abs_rect.x) % 3000
        abs_rect.y = (3000  + y + abs_rect.y) % 3000
        if self.rect.colliderect(abs_rect) and self.is_alive:
            enemy_killed_sound.play()
            self.is_alive=False
    
    # Check if the enemy collides with the ship
    def handle_ship_collision(self, ship, x, y):
        damage_sound = pygame.mixer.Sound('Damage.mp3')
        abs_rect = ship.rect.copy()
        abs_rect.x = (3000  + x + abs_rect.x) % 3000
        abs_rect.y = (3000  + y + abs_rect.y) % 3000
        if self.rect.colliderect(abs_rect) and self.is_alive:
            damage_sound.play()
            self.respawn()
            ship.take_damage()

    # Convert the enemy's state information to a dictionary
    def to_dict(self):
        # Create dictionary that stores enemy's current game state
        status = {
            "center_x":self.center_x,
            "center_y":self.center_y,
            "is_alive":self.is_alive,
            "x":self.x,
            "y":self.y
        }
        return status

    # Draw the Enemy on a given surface
    def draw(self, surface):
        if self.is_alive:
            surface.blit(self.image, self.rect.topleft)


'''
    Spaceship is an inheriting class for the spaceship game object, 
    and it inherits from GameObject.py. This class allows us to create
    spaceship objects, and implement specific funtions of the spaceship
    object, such as rotating the object, rotating the image, getting the
    height and width of the object, taking damage, checking for a collision
    with a planet, and converting object details into a dictionary for
    serialization.
'''
class Spaceship(GameObject):
    # Initialize the spaceship object with coordinates, radius, and an image path
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        super().__init__(x_coordinate, y_coordinate, radius, image_path)
        self.image = pygame.transform.scale(self.image, (radius * 4, radius * 2))
        self.rect = self.image.get_rect()
        self.angle = 0
        self.health=3
        self.score=0

    # Define a method to rotate the spaceship towards a target point
    def rotate(self, target_x, target_y):
        # Calculate the difference in x and y coordinates between the target and the spaceship
        dx = target_x - (self.x_coordinate + self.image.get_width() / 2)
        dy = target_y - (self.y_coordinate + self.image.get_height() / 2)
        self.angle = math.atan2(dy, dx)

    # Return rotated image to be drawn as the object rotates
    def get_rotated_image(self):
        rotated_image = pygame.transform.rotate(self.image, -math.degrees(self.angle))
        return rotated_image
    
    # Self explanatory
    def get_height(self):
        return self.image.get_height()
    
    # Self explanatory
    def get_width(self):
        return self.image.get_width()

    # If called, takes away a heart from the spaceship's health
    def take_damage(self):
        self.health-=1
        if self.health<1:
            print("GameOver")
    
    # Check if the spaceship collides with planet
    def handle_planet_collision(self, planet, x, y):
        planet_visited_sound = pygame.mixer.Sound("PlanetVisited.mp3")
        abs_rect = self.rect.copy()
        abs_rect.x = (3000  + x + abs_rect.x) % 3000
        abs_rect.y = (3000  + y + abs_rect.y) % 3000  
        if abs_rect.colliderect(planet.rect):
            planet_visited_sound.play()
            planet.respawn()
            self.score+=20
    
    def handle_wormhole_collision(self, wormhole, x, y):
        abs_rect = self.rect.copy()
        abs_rect.x = (3000  + x + abs_rect.x) % 3000
        abs_rect.y = (3000  + y + abs_rect.y) % 3000  
        if abs_rect.colliderect(wormhole.rect):
            wormhole.respawn()
            return True

    # Convert the spaceship's state information to a dictionary
    def to_dict(self):
        # Create dictionary that stores spaceship's current game state
        status = {
            "health":self.health,
            "score":self.score,
            "x_coordinate":self.x_coordinate,
            "y_coordinate":self.y_coordinate,
            "angle":self.angle
        }
        return status

    # Draw the spaceship on a given surface
    def draw(self, surface):
        rotated_image = self.get_rotated_image()
        self.rect = rotated_image.get_rect(center=(self.x_coordinate + self.image.get_width() / 2, self.y_coordinate + self.image.get_height() / 2))
        surface.blit(rotated_image, self.rect.topleft)


'''
    Crosshair is an inheriting class for the crosshair game object, 
    and it inherits from GameObject.py. This class allows us to create
    a crosshair object, though there are not any specific methods
    that we implement, as we implement simple crosshair functionality
    in the main program (simply follows the user's mouse).
'''
class Crosshair(GameObject):
    def __init__(self, x_coordinate, y_coordinate, width, height, image_path):
        # Initialize the crosshair object with coordinates, radius, width, height, and an image path
        super().__init__(x_coordinate, y_coordinate, 0, image_path)
        self.image = pygame.transform.scale(self.image, (width, height*2))


'''
    Shot is an inheriting class for the shot game object, and it
    inherits from GameObject.py. This class allows us to create shot
    objects, and implement specific funtions of the shot object,
    such as setting its direction, moving it, checking if it is out
    of bounds, and converting object details into a dictionary for
    serialization.
'''
class Shot(GameObject):
    # Initialize the shot object with coordinates, width, height, and an image path
    def __init__(self, x_coordinate, y_coordinate, width, height, image_path):
        super().__init__(x_coordinate, y_coordinate, 0, image_path)
        self.image = pygame.transform.scale(self.image, (width, height*2))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.direction = pygame.math.Vector2(0, 0)

    # Set direction of the shot
    def set_direction(self, start_pos, target_pos):
        self.direction = pygame.math.Vector2(target_pos) - pygame.math.Vector2(start_pos)
        self.direction = self.direction.normalize()

    # Move the shot across the screen
    def move(self, speed):
        self.x_coordinate += self.direction.x * speed
        self.y_coordinate += self.direction.y * speed
        self.rect.topleft = (self.x_coordinate, self.y_coordinate)

    # Check if the shot is out of bounds and return True or False
    def is_out_of_bounds(self, window_width, window_height):
        return self.x_coordinate < 0 or self.x_coordinate > window_width or self.y_coordinate < 0 or self.y_coordinate > window_height

    # Convert the shot's state information to a dictionary
    def to_dict(self):
        # Create dictionary that stores shot's current game state
        status = {
            "direction":self.direction,
            "x_coordinate":self.x_coordinate,
            "y_coordinate":self.y_coordinate
        }
        return status

'''
    Wormhole is an inheriting class for the wormhole game object, and it 
    inherits from GameObject.py. This class allows us to create wormhole
    objects, and implement specific funtions of the planet object, such
    as respawning, and converting object details into a dictionary for 
    serialization.
'''
class Wormhole(GameObject):
    # Initialize the planet with coordinates, radius, and an image path
    def __init__(self, x_coordinate, y_coordinate, radius, image_path):
        super().__init__(x_coordinate, y_coordinate, radius, image_path)
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_coordinate, self.y_coordinate)

    # Respawn the planet at a random location within the specified range
    def respawn(self):
        self.x_coordinate=randint(300,2700)
        self.y_coordinate=randint(300,2900)
        self.rect.center = (self.x_coordinate, self.y_coordinate)

    # Convert the planet's state information to a dictionary    
    def to_dict(self):
        # Create dictionary that stores planet's current game state
        status = {
            "x_coordinate":self.x_coordinate,
            "y_coordinate":self.y_coordinate,
        }
        return status
