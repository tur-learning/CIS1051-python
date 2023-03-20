# Lab session 4

7. Add random rotation to the previously generated _corner walls_.
8. Add a basic *Menu* that works with user inputs, using python `input()` function. The following options must be available to the player at the game start:
- Whether to add periodicity or not to the frame boundaries;
-  Whether to play with random walls generation;
9. Add the possibility to _change the speed_ of the snake at runtime, by pressing a key. Use the pygame built-in function `pygame.key.get_pressed()` to check for the event to happen. Look at the pygame documentation online. Add _fruits lifetime_. After 5000 ms they will be replaced if they do not get eaten. Use the `pygame.time.get_ticks()`
10. Replace the previously designed menu with a `menu` object from the pygame_menu library.