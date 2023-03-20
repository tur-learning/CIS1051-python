# Lab session 2

1. Add the _game over conditions_ when the snake touches itself in the `main.py` file.
2. Add a way to  _spawn fruits_ to be eaten by the snake in a separate module called `fruit.py`, which must be imported in the `main.py` file. Initialize the fruit position in the `main.py` file, and draw it using the pygame built-in functions.
3. Decrease the initial snake size to 4 blocks and add the ability to _eat fruits_. First, check for the position to understand if the fruit and the snake collide. If yes, the snake must grow. If the fruit is eaten, increase the game score by 10 and spawn a new fruit in a random position.