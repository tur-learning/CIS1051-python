# Snake
## Introduction

The snake game is subdivided in different _code modules_ (the files with the _.py_ extension), each of which is imported in the `main.py` file which contains the game loop and is used for web deployment via **pygbag**.
- The `game.py` module contains initialization of some game functionalities, mainly related to the `pygame` module. You can disregard it for the moment.
- The `snake.py` module includes the declaration and initialization of the snake blocks. It also contains the definition of the `draw` and `move` functions.
- The `fruit.py` module contains a few commented lines of code, that are intended to be used as a guide for the assignment .
- The `main.py` script, finally, is the main core of the program, and contains the relevant module _imports_, both from python and from _user-defined_ modules. It also includes the pygame _events handling_, some conditionals to _change the snake direction_ on the event of a key being pressed, the call to the `draw` and `move` functions from snake and/or fruit modules and the _game over_ conditions.

## Lab session 2

In order to complete the assignment, follow these steps. After each step, test your solution by running the game (try to test edge cases as well). If you need help, you can always have a look at the codes included in the next level_xx directories:

1. Add the _game over conditions_ when the snake touches itself in the `main.py` file. At the moment, the game ends only when the snake touches the boundaries of the game window:
  ```
  # Game Over conditions
  if snake.position[0] < 0 or snake.position[0] > game.window_x-10:
    game.game_over(game_window)
  if snake.position[1] < 0 or snake.position[1] > game.window_y-10:
    game.game_over(game_window)
  ```
You should add a condition to call the `game.game_over` function also when the snake touches itself.

3. Add a way to  _spawn fruits_ to be eaten by the snake in the separate module called `fruit.py`, which must be imported in the `main.py` file. Initialize the fruit position in a random place inside the game window in the `main.py` file (use the _random_pos_ function defined in the `game.py` module), and draw it using the pygame built-in functions.
4. Decrease the initial snake size to 4 blocks and add the ability to _eat fruits_. You should design this function by yourself, but some suggestions are already included in the above mentioned modules. First, check for the position to understand if the fruit and the snake collided. If yes, the snake must grow. If the fruit is eaten, increase the game score by 10 and spawn a new fruit in a random position.
