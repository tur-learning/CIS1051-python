import random

def input_number(args) :
    guess = int(input("Guess the Number: "))

    if guess > number :
        print("Too high, guess again!")
        input_number(args)

    elif guess < number :
        print("Too low, guess again!")
        input_number(args)

    else:
        print(f"Yay! You guessed the number: {number}")

number = random.randint(1,100)       
guess = input_number(int)

