# Lab session 3

4. Add the _periodicity_ to the frame. If the snake exits from one boundary of the frame it must re-enter from the opposite boundary.
5. Add _random wall generation_. Each time a fruit gets eaten by the snake, create a new block and add it to the _wall body_, a variable initialized in a new `wall.py` module that comprehends all the wall blocks. The wall must be colored in red and the game should display _game over_ on the collision of the snake with a wall block. Beware that the new fruit position does not overlap with previous walls.
6. Modify the wall generation in order to create a corner composed of three wall blocks.