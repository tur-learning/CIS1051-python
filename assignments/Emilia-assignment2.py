def input_number():
   numbers = int(input("Input Number:"))
   return numbers

n = input_number()

for i in range(5):
    number = input_number()
    if number > n: 
        highest_number = number 
        n = highest_number

print(f"The highest number was: {n}")


import random 

def input_number(args):
    guess = int(input("Guess the number: "))

if guess < number: 
    print("The number you guessed is too low")
    input_number(args)

elif guess > number: 
    print("The number you guessed is too high")
    input_number(args)

else:
    print(f"The number you guessed is correct!")
   
number = random.randint(1,100)
guess = input_number(int)