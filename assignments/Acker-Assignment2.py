import math
import random

def input_number():
    numberGiven = int(input("Please give a number  "))
    return numberGiven

highestNumber = 0

for i in range(5):
    number = input_number() 
    if number > highestNumber:
        highestNumber = number

  
print(f"The highest number was " + str(highestNumber))

number = random.randint(1,100)

print(number)

def input_number():
    numInput = int(input("Please guess a number between 1 and 100"  ))
    guess_number(numInput)

def guess_number(guess):
    if guess == number:
        print("You Win!")
        return
    elif guess > number:
        print("Too High!")
        guess=input_number()
    elif guess < number:
        print("Too Low!")
        guess=input_number()

guess = input_number()