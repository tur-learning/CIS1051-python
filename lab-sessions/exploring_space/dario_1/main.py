import math
import pygame
import pygame_menu
import random
import game

def show_periodic_background(x1, y1, movement):
    import assets
    x1 = (assets.bg_frame.width  + x1 + movement[0]) % assets.bg_frame.width
    y1 = (assets.bg_frame.height + y1 + movement[1]) % assets.bg_frame.height

    v1 = (x1, y1)
    v2 = ( 0, y1)
    v3 = ( 0,  0)
    v4 = (x1,  0)

    window_frame = pygame.Rect(v1, (game.window_x, game.window_y))

    w2 = max(0, window_frame.right - assets.bg_frame.right)
    w1 = window_frame.width - w2
    w3 = w2 ; w4 = w1

    h4 = max(0, window_frame.bottom - assets.bg_frame.bottom)
    h1 = window_frame.height - h4
    h2 = h1 ; h3 = h4
        
    quad_1 = pygame.Rect(v1, (w1, h1))
    quad_2 = pygame.Rect(v2, (w2, h2))
    quad_3 = pygame.Rect(v3, (w3, h3))
    quad_4 = pygame.Rect(v4, (w4, h4))

    game_window.blit(assets.background, (0,0), quad_1)
    game_window.blit(assets.background, (w1,0), quad_2)
    game_window.blit(assets.background, (w1,h1), quad_3)
    game_window.blit(assets.background, (0,h1), quad_4)

    # Adding an image on top of the background
    game_window.blit(assets.ship, ((game.window_x-assets.ship.get_width())/2, 
                                    (game.window_y-assets.ship.get_height())/2))
    
    return x1, y1

def start():
    import assets
    x1 = random.randint(0, game.window_x)
    y1 = random.randint(0, game.window_y)
    assets.shot_rect.center = game_window.get_rect().center
    shot_moving = False
    end_pos = (-1, -1)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not shot_moving:
                # Start moving the shot to the mouse position on click
                shot_moving = True
                start_pos = assets.shot_rect.center
                end_pos = pygame.mouse.get_pos()
                print(end_pos)
                direction = pygame.math.Vector2(end_pos) - pygame.math.Vector2(start_pos)
                print(pygame.math.Vector2(end_pos))
                print(pygame.math.Vector2(start_pos))
                print(direction)
                assets.shot_speed = 1

        movement = [0, 0]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            movement[0] =   assets.ship_speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            movement[0] = - assets.ship_speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            movement[1] = - assets.ship_speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            movement[1] =   assets.ship_speed
        
        x1, y1 = show_periodic_background(x1, y1, movement)

        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Center the target sprite at the mouse position
        assets.target_rect.center = mouse_pos
        
        # Draw the target sprite on the game_window
        game_window.blit(assets.target, assets.target_rect)

        if shot_moving:
            # Move the shot toward the clicked position over time
            delta_time = 2
            distance = direction.normalize() * assets.shot_speed * delta_time
            assets.shot_rect.move_ip(distance)

        # Check if the shot has reached the clicked position
        if assets.shot_rect.collidepoint(end_pos):
            shot_moving = False
            assets.shot_rect.center = game_window.get_rect().center

        if shot_moving:
            game_window.blit(assets.shot, assets.shot_rect)

        pygame.display.update()
  
def mainmenu():
	# Create a menu object
	menu = pygame_menu.Menu('The Space Race', game.window_x, game.window_y, theme=game.theme)
	
	# Adding features to the menu
	menu.add.button('Play', start)
	menu.add.selector('Choose Map: ', [('Yes', True), ('No', False)], onchange=game.set_periodic)
	menu.add.button('Quit', pygame_menu.events.EXIT)
	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
				
		if menu.is_enabled():
			menu.update(events)
			menu.draw(game_window)
		
		pygame.display.update()

# Initialising game
game_window = game.init()

mainmenu()
