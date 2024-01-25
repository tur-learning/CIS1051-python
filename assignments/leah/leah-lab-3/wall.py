import game
import main
import fruit
import snake

#kinda just following the script from the fruit module

position = game.random_pos()

spawn = False

#creating a list for all wall positions
body = []

def init():
    spawn = True

def draw(game_window):
    for pos in body:
        pygame.draw.rect(game_window, game.red,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    for corner in corners: #trying to just add the corners in with the existing drawing of the wall
        for pos in corner:
            pygame.draw.rect(game_window, game.red,
                         pygame.Rect(pos[0], pos[1], 10, 10))


def walls():
    walls_on_screen = []

def add_wall():
    new_position = locate()
    body.append(new_position)
    if len(body) > 5: #no more than 5 walls at a time
        body.pop(0)

def position_overlaps_with_walls(pos): #walls dont overlap
    return pos in body

#creating a list of corner walls
corners = [
    [(x, y), (x + 10, y), (x + 20, y), (x, y + 10), (x, y + 20)], #adding blocks to make the corner shape?
]

def generate_corner(x,y):
    corner = [
    [(x, y), (x + 10, y), (x + 20, y), (x, y + 10), (x, y + 20)], #this might be redundant idk
]
    corners.append(corner)

    if len(corners) > 5: #no more than 5 corners at a time
        corners.pop(0)

def generate_corner_position():
    while True:
        x = random.randrange(1, (window_x // 10)) * 10
        y = random.randrange(1, (window_y // 10)) * 10
        new_position = (x, y)

        # Check if the new position overlaps with walls, corners, or fruit
        if not (
            position_overlaps_with_walls(new_position) or
            position_overlaps_with_corners(new_position) or
            new_position == fruit.position
        ):
            return new_position


def locate():
    return game.random_pos()
