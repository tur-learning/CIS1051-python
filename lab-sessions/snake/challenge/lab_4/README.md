## Lab session 4

Starting from where you left after concluding level_06 of lab session 3, complete the following steps to fulfill the assignment:

7. Add **random rotation** to the previously generated _corner walls_. At the moment the _corner walls_ are generated such that their direction is always the same. Find a way to generate corners that _randomly_ point to one of the four possible directions (top-left, top-right, bottom-left, bottom-right). You should modify the function that generates the _corner_walls_ adding the least amount of parameters that are necessary to accomplish this task, without code repetitions.
8. Skip this step and go to step 9.
9. Add the possibility to **change the speed** of the snake at runtime, by pressing a key of your choice. Use the pygame built-in function `pygame.key.get_pressed()` to check for the event to happen. Look at the pygame [documentation](https://www.pygame.org/docs/) online. Add **fruits lifetime**. After 5000 ms of life, a fruit will be replaced if it does not get eaten. Use the pygame built-in function `pygame.time.get_ticks()`.
10. Skip this step. 
