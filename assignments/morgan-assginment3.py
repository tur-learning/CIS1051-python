print('This program calculates the factorial of n.')
number = int(input('Give me a number:'))

def factorial(n):
    if n == 1:
        return 1
    else:
        result = factorial (n-1)*n
        return result

answer = factorial(number)

print ('Factorial of',number, 'is',answer)

print('This program calculates the n-th number of the Fibonacci sequence.')
number=int(input('Give me a number:'))

def Fibonacci(n):
    if n < 2:
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)

answer = Fibonacci(number)
print(f"The {number}-th of the Fibonacci sequence is {answer}")

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


num1 = int(input("Give me one number:"))
num2 = int(input("Give me a second number:"))
result = gcd(num1, num2)

print(f"The Greatest Common Divisor of {num1} and {num2} is {result}")