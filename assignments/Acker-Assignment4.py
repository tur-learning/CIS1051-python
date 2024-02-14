import math

givenNumber = float(input("Give number for square root:   "))

guess = float(input("Guess for Heron's:   "))


def HeronsForm(x):
    output = (1/2)*(x+(givenNumber/x))
    return output

def calculate_sqrt(x):
    counter = 0
    while abs(math.sqrt(givenNumber) - x) >= 10**-12:
        counter = counter + 1
        runloop = HeronsForm(x)
        x = runloop
    return x, counter



SquareRoot = calculate_sqrt(guess)[0]
NumberOfLoops = calculate_sqrt(guess)[1]
error_precentage = abs((((SquareRoot/math.sqrt(givenNumber))-1)*100))
correct_result = math.sqrt(givenNumber)


print("The square root calculated by the program is " + str(SquareRoot) + " and the 'correct' value from python is " + str(correct_result))
print("It took " + str(NumberOfLoops) + " iterations to reach the desired error threshold")
print("The error of the calcualted value of the square root expressed as a precentage is " + str(error_precentage) + "%")





