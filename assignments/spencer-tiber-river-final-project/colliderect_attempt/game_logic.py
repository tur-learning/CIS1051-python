import pygame
import time
import math


window_size = [1000, 900]

#setting values for time
game_time = time.time()
fire_time = 0
can_shoot = True

#setting initial player position
player_pos = [450,450]
enemy_pos = [650,300]
ground_pos =[0, 465]
delta_x = 0
delta_y = 0

#dummy rect
dummy_x = player_pos[0]
dummy_y = player_pos[1]
dummy_rect = pygame.Rect(dummy_x,dummy_y, 30,40)

#gravity functions to make player stay on ground and not move up
gravity = 2.5 # Adjust the gravity value as needed
fall_speed = 0  # Initialize the character's fall speed


#Variables limit the time of jump
jump_counter = 100
jump_height = 350

#establishing a variable if the character is jumping or not
jumping = False
falling = False
y_detect = player_pos[1]

map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,5,0,0,0,0,0,0,5,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,0,0,0,0,0,0,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,3,0,0,0,0,0,0,3,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    ]