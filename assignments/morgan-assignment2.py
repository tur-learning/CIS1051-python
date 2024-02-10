def input_number():
    number = int(input("Input Number:"))
    return number#Define function

# Initialize variables 
n = input_number ()

for i in range(5):
    number = input_number ()
    if number > n:
        highest_number=number
        n = highest_number
        # To Complete

print (f"The highest number was ...", {n})

import random

def input_number():
    guessed = int(input("Guess a Number:"))
    guess_number(guessed)

def guess_number(guess):
    if number == guess:
        print ('You Win')
        return
    elif number < guess:
        print ('Too High')
        guess = input_number()
    elif number > guess:
        print ('Too Low, Go Higher')
        guess = input_number()

guess = input_number()
number = random.randint(1,100)


    


