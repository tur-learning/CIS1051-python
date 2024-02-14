#calculate the factorial of an integer

def factorial (n):
   if n == 1:
        return n
   else:
      result = n*factorial(n-1)
      return result

print("This program calculates the factorial of n.")
number = int(input("Input a number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")


#Fibonacci sequence

def fibonacci (n):
    if n < 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)
    

number = int(input("Give me a number: "))
result = fibonacci(number)
print(f"The {number}-th of Fiboonacci sequence is {result}")


#Finding the Greatest Common Divisor (GCD)

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


a = int(input("Input a number for a: "))
b = int(input("Input a number for b: "))

print("This program calculates the GCD of a and b.\n")
number = a, b   
result = gcd(a, b)
print(f"The Greatest Common Divisor (GCD) of {number} is: {result}")