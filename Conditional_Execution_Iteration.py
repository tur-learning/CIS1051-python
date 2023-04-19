# Pyramid Problem
def draw_pyramid(height):
    for row in range(height):
        for space in range(height - row - 1):
            print(' ', end='')
        for block in range(row + 1):
            print('#', end='')
        print(' ', end='')
        for block in range(row + 1):
            print('#', end='')
        print('')

user_height = int(input("\nHeight of pyramid: "))

draw_pyramid(user_height)