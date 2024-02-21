import math

#Prompting user to input a number for S "User input" and x0 "Guessed number"
S = float(input("Please, enter any positive real number: "))
x0 = float(input("Now, eneter the guess number for the esitmate: "))

def herons_method(S, x):
    #Output of Heron's method
    output = (1/2) * (x + (S / x))
    return output

def calculate_square_root(S, x0):
    x = x0
    while abs(math.sqrt(S) - x) >= 1e-12:
        x = herons_method(S, x)
    return x

#Calculating square root using Heron's method
approx_sqrt = herons_method(S, x0)

##Calculate square root using math module foor comparison
actual_sqrt = math.sqrt(S)

#Calculating the error
error = abs(actual_sqrt - approx_sqrt)


#Results
print(f"The answer for Heron's method: {approx_sqrt}")
print(f"The answer according to math module: {actual_sqrt}")
print(f"Error: {error}")

    



