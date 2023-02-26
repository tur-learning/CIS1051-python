import numpy as np
import snake
import fruit

def find_path(default):

    direction = list(np.array(fruit.position) - np.array(snake.position))
    # direction = [1, 3]

    print(fruit.position)
    print(snake.position)
    print(direction)

    if   direction[1] > 0:
        return 'UP'
    elif direction[1] < 0:
        return 'DOWN'
    elif direction[0] > 0:
        return 'RIGHT'
    elif direction[0] < 0:
        return 'LEFT'
    else:
        return default
