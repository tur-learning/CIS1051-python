import pygame

pygame.init()
fps = pygame.time.Clock()

# Set up the game window
window_width = 640
window_height = 480
game_window = pygame.display.set_mode((window_width, window_height))

# Load the background image
background_image = pygame.image.load("Space_Background_03.png").convert()

# Set the initial position of the crop rectangle
crop_x = 100
crop_y = 100
crop_width = 200
crop_height = 200
crop_rect = pygame.Rect(crop_x, crop_y, crop_width, crop_height)

# Game loop
while True:
    fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the crop rectangle to the right
    crop_x += 5
    crop_rect = pygame.Rect(crop_x, crop_y, crop_width, crop_height)

    # Get a new subsurface of the background image using the updated crop rectangle
    cropped_image = background_image.subsurface(crop_rect)

    # Blit the cropped image onto the game window
    game_window.blit(cropped_image, (0, 0))

    # Update the display
    pygame.display.update()
