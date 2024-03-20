import math

def squareroot(a,b):
    accuracy = 10e-12
    difference = 1
    while abs(difference) > accuracy:
        new = (1/2)*(b+a/b)
        difference = b - new
        b = new
    return new

number = float(input("Give a number to calculate the square root of:"))
guess = float(input('Give me a guess of the square root:'))

answer = math.sqrt(number)
result = squareroot(answer,guess)
error = (answer - result)

print(f"The Square Root of{number}is{answer}and the error of Heron's algorithm is{error}.")