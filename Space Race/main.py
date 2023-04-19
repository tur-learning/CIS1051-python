import math
import pygame
import pygame_menu
import random
import time
import game
import GameObject
from GameObject import Planet, Enemy, Spaceship, Crosshair, Shot, Wormhole
import shelve


'''
    Load in miscellaneous game features and handle other
    constraints (e.g. extending background, re-establishing
    game window dimensions, etc.).
'''
# Load the extended background image and its dimensions
extended_background = pygame.image.load("background1v2.png").convert_alpha()
new_width, new_height = extended_background.get_size()
background = pygame.transform.scale(extended_background, (new_width, new_height))
map = ["background1v2.png"]
moving_objects_surface = pygame.Surface((new_width, new_height), pygame.SRCALPHA)

# Load in planet image, establish object, and spawn
planet_image_path = "planet.png"
earth = Planet(200, 200, 200, planet_image_path)
earth.respawn()

# Load in wormhole image, establish object, and spawn
wormhole_image_path = "wormhole.png"
wormhole = Wormhole(200, 200, 100, wormhole_image_path)
wormhole.respawn()

# Load in enemy image, and establish object
enemy_image_path = "enemy.png"
alien = Enemy(600, 600, 50, enemy_image_path)

# Load in music and sounds
pygame.mixer.init()
shot_sound = pygame.mixer.Sound('Shot.mp3')
gameover_sound = pygame.mixer.Sound('GameOver.mp3')
wormhole_sound = pygame.mixer.Sound('Wormhole.mp3')
music = pygame.mixer.music.load('Music.mp3')
# Play the background music on loop
pygame.mixer.music.play(-1)

'''
    Use the following two functions to update
    the game background based on the user's
    selection when presented options in the
    main menu.
'''
def update_background(image_path):
    # Declare global variables to be modified within the function
    global background, new_width, new_height, bg_frame
    # Load the image from the given path and convert its pixel format for better performance
    background = pygame.image.load(image_path).convert_alpha()
    background = pygame.transform.scale(background, (new_width, new_height))
    # Get the rectangular area (frame) of the scaled background image
    bg_frame = background.get_rect()
    # Update the new width and height values with the dimensions of the scaled image
    new_width = background.get_width()
    new_height = background.get_height()

def set_map(_, value):
    # Update the map with the given value (user-selected)
    map[0] = value
    # Call the update_background function to load and scale the new background image based on user selection
    update_background(value)

# Zooms used to scale images to reasonable size and offset spaceship to follow crosshair better
zoom_1 = 1
zoom_2 = 0.1
zoom_3 = 0.04
zoom_4 = 0.02
tip_offset = 75

background = pygame.image.load(map[0]).convert_alpha()
update_background(map[0])
background = pygame.transform.scale(background, (new_width, new_height))
bg_frame = background.get_rect()
new_width = background.get_width()
new_height = background.get_height()

# Load in heart image for heart icon that will represent the user's lives
heart = pygame.image.load("heart.png").convert_alpha()

# Create spaceship object and set attributes
spaceship = Spaceship(630, 330, 50, "spaceship.png")

# Set crosshair attributes and create crosshair object
crosshair_width = int(game.window_x * zoom_3)
crosshair_height = int(game.window_y * zoom_3)
crosshair = Crosshair(0, 0, crosshair_width, crosshair_height, "crosshair.png")

# Set shot attributes and create shot object
shot_width = int(game.window_x * zoom_4)
shot_height = int(game.window_y * zoom_4)
shot = Shot(750, 750, shot_width, shot_height, "shot.png")

# Declare necessary movement variables
movement = [0, 0]
speed = 15


x1 = game.window_x / 2
y1 = game.window_y / 2

enemy_group = pygame.sprite.Group()

# Periodicity code
def show_periodic_background(x1, y1, background_with_objects):
    x1 = (new_width  + x1 + movement[0]) % new_width
    y1 = (new_height + y1 + movement[1]) % new_height

    v1 = (x1, y1)
    v2 = ( 0, y1)
    v3 = ( 0,  0)
    v4 = (x1,  0)

    window_frame = pygame.Rect(v1, (game.window_x, game.window_y))

    w2 = max(0, window_frame.right - new_width)
    w1 = window_frame.width - w2
    w3 = w2 ; w4 = w1

    h4 = max(0, window_frame.bottom - new_height)
    h1 = window_frame.height - h4
    h2 = h1 ; h3 = h4

    quad_1 = pygame.Rect(v1, (w1, h1))
    quad_2 = pygame.Rect(v2, (w2, h2))
    quad_3 = pygame.Rect(v3, (w3, h3))
    quad_4 = pygame.Rect(v4, (w4, h4))

    game.game_window.blit(background_with_objects, (0,0), quad_1)
    game.game_window.blit(background_with_objects, (w1,0), quad_2)
    game.game_window.blit(background_with_objects, (w1,h1), quad_3)
    game.game_window.blit(background_with_objects, (0,h1), quad_4)

    return x1, y1


# Initialization
pygame.init()

# Use shelve module to save game state
def save_game():
    # Open a file called SavedGame as a data dictionary
    with shelve.open('SavedGame') as data:
        # Create key / value pairs between game objects and sub dictionaries containing their data
        data['player'] = spaceship.to_dict()
        data["x1"]=x1
        data["y1"]=y1
        data['shot'] = shot.to_dict()
        data['planet'] = earth.to_dict()
        data['wormhole'] = wormhole.to_dict()
        # Do the same with enemy group
        data['enemies']=[]
        enemies=[]
        for enemy in enemy_group:
            enemies.append(enemy.to_dict())
        data["enemies"]=enemies
   
# Use shelve to open saved game data and re-assign game object attributes to the data stored
def load_game():
    global x1,y1
    with shelve.open('SavedGame') as data:
        spaceship.load(data['player'])
        shot.load(data['shot'])
        earth.load(data["planet"])
        wormhole.load(data['wormhole'])
        x1=data["x1"]
        y1=data["y1"]

        enemy_group.empty()
        for enemy in data["enemies"]:
            e=Enemy(600, 600, 50, enemy_image_path)
            e.load(enemy)
            enemy_group.add(e)

        
# Set up fonts, texts, and draw the score, health, and heart icon on the game window
def draw_score_health():
     font = pygame.font.Font(None, 38)
     text = font.render(str(spaceship.score), True, "white")
     game.game_window.blit(text,(game.game_window.get_width()/2,20))
     game.game_window.blit(heart,(20,20))
     text = font.render(str(spaceship.health), True, "white")
     game.game_window.blit(text,(80,35))

# Start with saved game
def start_saved():
    start(True)

# By default start a new game unless start parameter overriden with load = True
def start(load=False):
    global x1,y1
    enemy_group.add(alien)
    alien.respawn()
    shot_speed = 50
    
    x1 = game.window_x / 2
    y1 = game.window_y / 2

    fps = pygame.time.Clock()

    # Scrolling variable
    scroll = 0

    # Amount of maximum contemporary repetitions of the background
    # over the game window
    tiles = math.ceil(game.window_x / background.get_width()) + 1

    # Initialize the shot position and shot_active flag
    shot_pos = [0, 0]
    shot_active = False

    alien_active = True

    spaceship_pos = [630, 330]  # Adjust this to match the spaceship's initial position
    background_with_objects = background.copy()
    
    # Load saved game if load parameter is True
    if load:
        load_game()

    # Main game loop execution
    while spaceship.health>0:
        # Setting the fps
        fps.tick(30)
        # Make mouse not appear on screen
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

        # Handle user movement requirements
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            movement[0] = speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            movement[0] = -speed
        else:
            movement[0] = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            movement[1] = -speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            movement[1] = speed
        else:
            movement[1] = 0

        crosshair.x_coordinate, crosshair.y_coordinate = pygame.mouse.get_pos()
        x1, y1 = show_periodic_background(x1, y1, background_with_objects)

        # Save game key is P, handle save if clicked
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            save_game()

        # If user chooses to quit, quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            # Handle shot positional movement when user clicks down
            if not shot_active and (event.type == pygame.MOUSEBUTTONDOWN):
                shot_active = True
                shot_sound.play()
                tip_x = spaceship_pos[0] + spaceship.get_width() / 2 + math.cos(angle_rad) * tip_offset
                tip_y = spaceship_pos[1] + spaceship.get_height() / 2 + math.sin(angle_rad) * tip_offset
                shot.x_coordinate, shot.y_coordinate = tip_x, tip_y
                crosshair_pos = pygame.mouse.get_pos()
                shot.set_direction((tip_x, tip_y), crosshair_pos)

        # Get the angle between the spaceship and the mouse position
        mouse_pos = pygame.mouse.get_pos()
        angle_rad = math.atan2(mouse_pos[1] - (spaceship_pos[1] + spaceship.get_height() / 2),
                               mouse_pos[0] - (spaceship_pos[0] + spaceship.get_width() / 2))
        angle_deg = math.degrees(angle_rad) - 90

        # Handle spaceship rotation following mouse
        spaceship.rotate(*pygame.mouse.get_pos())
        spaceship.draw(game.game_window)

        # Handle shot display
        if shot_active:
            shot.move(shot_speed)
            shot_pos = [shot.x_coordinate, shot.y_coordinate]
            game.game_window.blit(shot.image, shot_pos)

        # Handle alien movement and display if alive
        if alien.alive:
            alien.move(30)
            alien.draw(moving_objects_surface)

        # Used to fix infinite enemy trail when moving in circles
        background_with_objects = background.copy()
        background_with_objects.blit(moving_objects_surface, (0, 0))
        moving_objects_surface.fill((0, 0, 0, 0))
        alien.move(30)
        earth.draw(moving_objects_surface)
        wormhole.draw(moving_objects_surface)

        # Check if spaceship collides with planet and handle
        spaceship.handle_planet_collision(earth,x1,y1)

        if spaceship.handle_wormhole_collision(wormhole,x1,y1):
            wormhole_sound.play()
            new_background = random.randint(1,5)
            if map[0] == "background1v2.png":
                if new_background == 1:
                    update_background("background2v2.png")
                if new_background == 2:
                    update_background("background3v2.png")
                if new_background == 3:
                    update_background("background4v2.png")
                if new_background == 4:
                    update_background("background5v2.png")
            elif map[0] == "background2v2.png":
                if new_background == 1:
                    update_background("background1v2.png")
                if new_background == 2:
                    update_background("background3v2.png")
                if new_background == 3:
                    update_background("background4v2.png")
                if new_background == 4:
                    update_background("background5v2.png")
            elif map[0] == "background3v2.png":
                if new_background == 1:
                    update_background("background2v2.png")
                if new_background == 2:
                    update_background("background1v2.png")
                if new_background == 3:
                    update_background("background4v2.png")
                if new_background == 4:
                    update_background("background5v2.png")
            elif map[0] == "background4v2.png":
                if new_background == 1:
                    update_background("background2v2.png")
                if new_background == 2:
                    update_background("background3v2.png")
                if new_background == 3:
                    update_background("background1v2.png")
                if new_background == 4:
                    update_background("background5v2.png")
            elif map[0] == "background5v2.png":
                if new_background == 1:
                    update_background("background2v2.png")
                if new_background == 2:
                    update_background("background3v2.png")
                if new_background == 3:
                    update_background("background4v2.png")
                if new_background == 4:
                    update_background("background1v2.png")

        # Check if shot collides with shot and handle
        for enemy in enemy_group:
            enemy.move(30)
            enemy.draw(moving_objects_surface)
            if shot_active:
                enemy.handle_shot_collision(shot, x1, y1)
            
            # Check if spaceship collides with enemy and handle
            enemy.handle_ship_collision(spaceship,x1,y1)
            if not enemy.is_alive:
                 spaceship.score+=5
                 enemy.respawn()

                 # Most enemies present at a time is 10, continuously add enemies for every planet until 10
                 if len(enemy_group)<10:
                      new = Enemy(600, 600, 50, enemy_image_path)
                      enemy_group.add(new)
                      new.respawn()

        # Fixed game object bugs
        background_with_objects = background.copy()
        background_with_objects.blit(moving_objects_surface, (0, 0))

        # Kill the shot when it leaves the game window
        if shot.is_out_of_bounds(game.window_x, game.window_y):
            shot_active = False

        # Display the crosshair
        crosshair.draw(game.game_window)

        # Display score and health
        draw_score_health()
        pygame.display.update()

    gameover_menu(spaceship.score)
    pygame.quit()


def mainmenu():
    # Create a menu object
    menu = pygame_menu.Menu('SPACE RACE', game.window_x, game.window_y, theme=pygame_menu.themes.THEME_DARK.copy())
    
    # Adding features to the menu
    menu.add.button('Play', start)
    menu.add.button('Load Saved Game', start_saved)
    menu.add.selector('Map: ', [('1', "background1v2.png"), ('2', "background2v2.png"), ('3', "background3v2.png"), ('4', "background4v2.png"), ('5', "background5v2.png")], onchange=set_map)
    menu.add.text_input('Name: ')
    menu.add.button('Quit', pygame_menu.events.EXIT)

    # Handle menu selection
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
                
        if menu.is_enabled():
            menu.update(events)
            menu.draw(game.game_window)
        
        pygame.display.update()

# Handle game over outcome
def gameover_menu(score):
    gameover_sound.play()
    menu = pygame_menu.Menu('SPACE RACE', game.window_x, game.window_y, theme=pygame_menu.themes.THEME_DARK.copy())
    
    # Display final score to user
    menu.add.label("Your Score")
    menu.add.label(str(score))

    # Add option for user to quit game
    menu.add.button('Quit', pygame_menu.events.EXIT)

    # Handle menu selection
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
                
        if menu.is_enabled():
            menu.update(events)
            menu.draw(game.game_window)
        
        pygame.display.update()

mainmenu()