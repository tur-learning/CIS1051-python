import pygame

# Initialize pygame
pygame.init()

# Set the display size
display_width = 800
display_height = 600

# Create the display surface
screen = pygame.display.set_mode((display_width, display_height))

# Load the image
image = pygame.image.load("background.png").convert()

# Get the width and height of the image
width, height = image.get_size()

# Create a new surface with double width and height
new_width, new_height = width * 2, height * 2
new_surface = pygame.Surface((new_width, new_height), pygame.SRCALPHA)

# Paste the original image on the top-right corner of the new surface
new_surface.blit(image, (width, 0))

# Flip the image horizontally and paste it on the top-left corner
mirrored_image = pygame.transform.flip(image, True, False)
new_surface.blit(mirrored_image, (0, 0))

# Flip the image both horizontally and vertically and paste it on the bottom-left corner
mirrored_image = pygame.transform.flip(image, True, True)
new_surface.blit(mirrored_image, (0, height))

# Flip the image vertically and paste it on the bottom-right corner
mirrored_image = pygame.transform.flip(image, False, True)
new_surface.blit(mirrored_image, (width, height))

# Save the new surface as an image
pygame.image.save(new_surface, "./your_new_image.png")

# Quit pygame
pygame.quit()
