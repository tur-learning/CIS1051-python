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
crop_x = 0
crop_y = 0
crop_rect_r = pygame.Rect(crop_x, crop_y, window_width, window_height)
crop_rect_l = pygame.Rect(0, crop_y, 0, window_height)

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
    crop_rect_r.move_ip(crop_speed, 0)
    crop_rect_l.move_ip(crop_speed, 0)
    crop_rect_r.width = crop_rect_r.left + window_width - background_image.get_width()
    crop_rect_l.width = window_width - crop_rect_r.width

    if crop_rect_r.width == 0: crop_rect_r = crop_rect_l

    # # Check if the right edge of the crop rectangle is greater than the width of the background image
    # if crop_rect.right > background_image.get_width():
    #     # If it is, subtract the width of the background image from the x-coordinate to wrap around to the left side
    #     crop_rect.left -= background_image.get_width()

    # Get a new subsurface of the background image using the crop rectangle
    cropped_image_r = background_image.subsurface(crop_rect_r)
    cropped_image_l = background_image.subsurface(crop_rect_l)

    # Blit the cropped image onto the game window
    game_window.blit(cropped_image_r, (0, 0))
    game_window.blit(cropped_image_l, (crop_rect_l.width, 0))

    # Update the display
    pygame.display.update()
