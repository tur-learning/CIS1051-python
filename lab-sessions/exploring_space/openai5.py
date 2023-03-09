import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Load your left and right surfaces
left_surface = pygame.Surface((400, 600))
left_surface.fill((255, 0, 0))
right_surface = pygame.Surface((400, 600))
right_surface.fill((0, 255, 0))

# Create a larger surface to hold both surfaces
combined_surface = pygame.Surface((800, 600))

# Blit the left and right surfaces onto the larger surface
combined_surface.blit(left_surface, (0, 0))
combined_surface.blit(right_surface, (500, 0))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Blit the combined surface onto the screen
    screen.blit(combined_surface, (0, 0))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
