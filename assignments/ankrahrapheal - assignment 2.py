# Finding the highest number in loop
def input_number():
    n = int(input("Input a number: "))
    return n

highest_number = 0
 
for i in range(5):
    number = input_number()
    if number > highest_number:
        highest_number = number
    
print(f"The highest number was..." + str(highest_number))




#creating a random guess game with number
import random

def input_number():
   n=int(input("Guess a number: "))
   guess_number(n)


def guess_number(guess):
    if number == guess:
        print('Yey, you finally did it!')
        return
    elif guess > number:
        print('Number is too high, guess again!')
        guess = input_number()
    elif guess < number:
        print('Number is too small, guess again!')
        guess = input_number()

number = random.randint(1,100)
guess = input_number()