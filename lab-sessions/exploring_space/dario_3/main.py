import pygame
import random
import entities
import map
import game
import time
import shelve

def show_periodic_background(x1, y1, bkg):
    x1 = (bg_frame.width  + x1 + movement[0]) % bg_frame.width
    y1 = (bg_frame.height + y1 + movement[1]) % bg_frame.height
  
    v1 = (x1, y1)
    v2 = ( 0, y1)
    v3 = ( 0,  0)
    v4 = (x1,  0)

    window_frame = pygame.Rect(v1, (session.window_x, session.window_y))

    w2 = max(0, window_frame.right - bg_frame.right)
    w1 = window_frame.width - w2
    w3 = w2 ; w4 = w1

    h4 = max(0, window_frame.bottom - bg_frame.bottom)
    h1 = window_frame.height - h4
    h2 = h1 ; h3 = h4
        
    quad_1 = pygame.Rect(v1, (w1, h1))
    quad_2 = pygame.Rect(v2, (w2, h2))
    quad_3 = pygame.Rect(v3, (w3, h3))
    quad_4 = pygame.Rect(v4, (w4, h4))

    session.game_window.blit(bkg, (0,0), quad_1)
    session.game_window.blit(bkg, (w1,0), quad_2)
    session.game_window.blit(bkg, (w1,h1), quad_3)
    session.game_window.blit(bkg, (0,h1), quad_4)

    return x1, y1

# Initialization
session = game.Session(1000., 1000.)
zoom_1 = 10*0.6
zoom_2 = 20
speed = 8
end_pos = (-1, -1)

# Creating the map
bkg_map = map.Map(0., 0., session.window_x, session.window_y, zoom_1, "background.png")

# Initializing objects
spaceship = entities.Spaceship(0, 0, 20, "spaceship.png",
                               session.game_window.get_rect().center)
target = entities.Crosshair(0., 0., zoom_2, "target.png")
shot   = entities.Bullet(0, 0, zoom_2, "shot.png")

x1 = random.randint(0, session.window_x)
y1 = random.randint(0, session.window_y)

x2 = random.randint(0, session.window_x)
y2 = random.randint(0, session.window_y)

# Create planets
earth = entities.Planet(x2, y2, 2, 10, "earth.png")
ice = entities.Planet(2000, 2000, 2, 10, "ice.png")
gas = entities.Planet(1000, 3000, 2, 10, "gas.png")
moon = entities.Planet(x2 + 800, y2, 6, 0, "moon.png")
planets = [earth, ice, gas]

# Create enemies and group them
enemy_group = pygame.sprite.Group()  # Create sprite group for enemies
for planet in planets:
    for enemy in planet.aliens:
        enemy_group.add(enemy)  # Add enemies to sprite group

# Create gem and group them
gem_group = pygame.sprite.Group()
for planet in planets:
    for gem in planet.gems:
        gem_group.add(gem)

# Create a black surface background to blit surfaces on
background = bkg_map.scaled_surface.copy()
background.fill('black')
bg_frame = background.get_rect()

load = input("Do you want to restart from a previously saved game? (y|n)\n")
#load = 'n'
if load == "y":
    db = session.load()
    [x1, y1] = db["position"]
    spaceship.load(db["spaceship"])
    earth.load(db["earth"])
    ice.load(db["ice"])
    gas.load(db["gas"])
    moon.load(db["moon"])
    target.load(db["target"])
    shot.load(db["shot"])
    db.close()

# Main loop
while True:
    # Setting the fps
    session.fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not shot.moving:
            # Start moving the shot to the mouse position on click
            shot.fire(pygame.mouse.get_pos())

    movement = [0, 0]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        movement[0] =   speed
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        movement[0] = - speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        movement[1] = - speed
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        movement[1] =   speed
    if keys[pygame.K_LCTRL] and keys[pygame.K_z]: 
        save = shelve.open(session.filename)
        save['position']  = [x1, y1]
        save['spaceship'] = spaceship.save()
        save['earth']     = earth.save()
        save['ice']       = ice.save()
        save['gas']       = gas.save()
        save['moon']      = moon.save()
        save['target']    = target.save()
        save['shot']      = shot.save()
        save.close()
        pygame.quit()

    x1, y1 = show_periodic_background(x1, y1, background)

    # Draw the map on top of the black background
    bkg_map.draw(background)

    # Draw the planets on top of the map
    earth.draw(background)
    ice.draw(background)
    gas.draw(background)

    # Draw the moon on top of the map
    moon.move_around(1)
    moon.draw(background)

    # Draw the alien on top of the map
    for alien in enemy_group:
        alien.collide(shot, x1, y1)
        alien.collide(spaceship, x1, y1)
        alien.move_around()
        alien.draw(background)
        

    # Draw the gem on top of the map
    for gem in gem_group:
        gem.collide(spaceship, x1, y1)
        gem.move_around()
        gem.draw(background)

    # Draw the spaceship on the game window center)
    spaceship.rotate(*pygame.mouse.get_pos())
    spaceship.draw(session.game_window)

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw the target sprite on the game window
    target.draw(session.game_window, mouse_pos)

    # Draw the shot on the game window
    shot.draw(session.game_window)

    # disegna il testo del punteggio sulla schermata
    session.draw_score()
    if spaceship.killed:
        session.game_over()
        pygame.display.update()
        time.sleep(10)
        pygame.quit()

    pygame.display.update()
  
pygame.quit()