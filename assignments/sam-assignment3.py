def factorial(n):
    if n == 0:
     return 1
    else:
        return n * factorial(n-1)

try:
    number = int(input('enter a positive integer to calculate its factorial:'))
    if number < 0:
     print('enter a non-negative number')
    else:
     result = factorial(number)
     print(f"the factorial of {number} is {result}")
except ValueError:
    print('invalid input')


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    n = int(input('enter a positive integer to calculate its fibonacci number:'))
    if n < 0:
        print('enter a non-negative number')
    else: 
        result = fibonacci(n)
        print(f'the {n}-th fibonacci number is {result}')
except ValueError:
    print('invalid input')

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

try:
    number1 = int(input('enter the first integer:'))
    number2 = int(input('enter the second integer'))

    a = max(number1, number2)
    b = min(number1, number2)

    result = gcd(a, b)
    print(f'the greatest common denominator of {number1} and {number2} is: {result}')

except ValueError:
    print('invalid input')
