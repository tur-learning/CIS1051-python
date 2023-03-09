import pygame

pygame.init()
fps = pygame.time.Clock()

# Set up the game window
window_width = 400
window_height = 400
game_window = pygame.display.set_mode((window_width, window_height))

# Load the background image
background_image = pygame.image.load("Space_Background_03.png").convert()

# Crop a portion of the background image
crop_rect = pygame.Rect(0, 0, window_width, window_height)  # x, y, width, height
cropped_image = background_image.subsurface(crop_rect)

# Set the initial x-position of the cropped image
cropped_x = 0

# Set the speed of the cropped image
cropped_speed = 5

# Game loop
while True:
    fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the cropped image to the right
    cropped_x += cropped_speed

    # Blit the cropped image onto the game window
    game_window.blit(cropped_image, (cropped_x, 0))

    # Update the display
    pygame.display.update()
