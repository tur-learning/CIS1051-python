# importing libraries
import pygame
import asyncio
import math

# importing project modules
import game

async def main():
	# Initialising game
    game_window = game.init()
    background = pygame.image.load('background.png').convert()

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("spaceship.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = (game.window_x / 2, game.window_y - 50)

        def update(self):
            self.rect.center = pygame.mouse.get_pos()

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, center_x, center_y, radius):
            super().__init__()
            self.image = pygame.image.load("enemy.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, 
                                                (self.image.get_width() * 0.2, 
                                                self.image.get_height() * 0.2))
            self.rect = self.image.get_rect()
            self.rect.center = (center_x, center_y)
            self.center_x = center_x
            self.center_y = center_y
            self.radius = radius
            self.angle = 0

        def update(self):
            self.angle += 2
            self.rect.x = self.center_x + math.cos(math.radians(self.angle)) * self.radius
            self.rect.y = self.center_y + math.sin(math.radians(self.angle)) * self.radius


    # Load the player character image
    spaceship = pygame.image.load('spaceship.png').convert_alpha()

    # Gruppi di sprite
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    enemy = Enemy(game.window_x / 4, game.window_y / 2, 100)
    all_sprites.add(enemy)
    enemies.add(enemy)

    game_over = False
    while not game_over:
        # RGB - Red, Green, Blue
        game_window.fill((0, 0, 0))

        # Background Image
        game_window.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        all_sprites.update()
        all_sprites.draw(game_window)

        if pygame.sprite.spritecollide(player, enemies, False):
            print("Game Over")
            game_over = True

        game.update(game_window)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())