def factorial (n): 
    if n == 1 :
        return 1
   
    else :
        return n * factorial(n-1) 


number = int(input("Input Number (integer): "))
result = factorial(number)
print(f"The factorial of {number} is {result}")



def fib(n):

    if n <= 1 :
        return n
    else :
        return fib(n-1) + fib(n-2)    

number = int(input("Input Number (integer): "))
result = fib(number)
print(f"Number {number} of the Fibonacci sequence is: {result}")



def gcd(a, b):
    a, b = max(a, b), min(a, b)

    if b == 0 :
        return a
        
    else :
        return gcd(b, a % b)


number1 = int(input("Input the first number: "))
number2 = int(input("Input the second number: "))


result = gcd(number1, number2)
print(f"The GCD of {number1} and {number2} is: {result}")