def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)

print("This program calculates the factorial of n.")
number = int(input("Give me a number n (integer): "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")



def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("This program calculates the n-th number of the Fibonacci sequence")
number = int(input("Give me a number n (integer): "))

result = fibonacci(number)
print(f"The {number}-th of the Fibonacci sequence is {result}")



def GCD(a, b):
    a, b = max(a, b), min(a, b)

if b == 0:
    return a

else: 
    return GCD(b, a % b)

number1 = int(input("Write the first number: "))
number2 = int(input("Write the second number"))

result = GCD(number1, number2)
print(f"The GCD of {number1} and {number2} is: {result}")