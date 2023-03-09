import pygame

pygame.init()
fps = pygame.time.Clock()

# Set up the game window
window_width = 400
window_height = 400
game_window = pygame.display.set_mode((window_width, window_height))

# Load the background image
background_image = pygame.image.load("Space_Background_03.png").convert()

# Set the initial position and size of the crop rectangle
crop_x = 100
crop_y = 100
crop_width = 400
crop_height = 400
crop_rect = pygame.Rect(crop_x, crop_y, crop_width, crop_height)

# Set the speed of the crop rectangle
crop_speed = 5

# Game loop
while True:
    fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the crop rectangle to the right
    crop_rect.move_ip(crop_speed, 0)

    # Check if the right edge of the crop rectangle is greater than the width of the background image
    if crop_rect.right > background_image.get_width():
        # If it is, subtract the width of the background image from the x-coordinate to wrap around to the left side
        crop_rect.left -= background_image.get_width()

    # Get a new subsurface of the background image using the crop rectangle
    cropped_image = background_image.subsurface(crop_rect)

    # Blit the cropped image onto the game window
    game_window.blit(cropped_image, (0, 0))

    # Update the display
    pygame.display.update()
