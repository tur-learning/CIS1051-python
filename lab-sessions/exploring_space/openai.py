import pygame

# Set up the display
pygame.init()
fps = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Background scrolling")

# Load the background image
background_image = pygame.image.load("Space_Background_03.png").convert()
background_rect = background_image.get_rect()

# Set up the initial position and size of the cropped region
crop_rect = pygame.Rect(0, 0, 400, 300)

# Set up the initial position of the background
background_x = 0

# Run the game loop
while True:
    fps.tick(30)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the background
    background_x -= 5
    if background_x < -background_rect.width:
        background_x = 0

    # Update the position of the cropped region
    crop_rect.x += 5
    if crop_rect.right > background_rect.right:
        crop_rect.left = 0

    # Blit the background and the cropped region
    screen.blit(background_image, (0, 0), area=crop_rect)
    
    # Update the display
    pygame.display.flip()
