def input_number():
    number = int(input("Input an integer number: "))
    return number 
    # define function

# initialize variables
n = input_number()

for i in range(5):
    number = input_number()
    if number > n:
        n = number
        # to complete

print(f'the highest number was... {n}')


import random

rannum = int(random.randint(1,101))
guess = 0

while guess != rannum:
    guess = int(input("Input an integer number: "))
    if guess == rannum:
        continue
    elif guess < rannum:
        print("{} is less than the generated number. Guess again".format(guess))
    elif guess > rannum:
        print("{} is greater than the generated number. Guess again".format(guess))
    else:
        print("what did you do something broke")


print("Congrats, {} is the generated number".format(guess))