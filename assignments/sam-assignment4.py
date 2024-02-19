import math

one = float(input('enter a number to square root:'))
two = float(input('enter a guess:'))

def herons_number(x):
    output = (1/2) * (x+(one/x))
    return output

def answer(x):
    counter = 0
    while abs(math.sqrt(one) - x) >= 10**-12:
        counter = counter + 1
        call_answer = herons_number(x)
        x = call_answer
    return x, counter

program_output = answer(two)[0]
print("the square root calculated by the program is " + str(program_output))

number = answer(two)[1]
print("the number of iterations it took to calculate is " + str(number))

error_percent = abs((program_output / math.sqrt(one)) -1) *100
print("the error rate based off of the actual square root is " + str(error_percent))


