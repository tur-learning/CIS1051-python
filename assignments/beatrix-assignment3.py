def factorial (x):
    if x==1:
        return 1 
    else:
        return (x*factorial(x-1))
num = int(input("Enter an integer: "))
print("The factorial of", num,"is", factorial(num))


def fib(number):
    if number<2:
        return 1
    else:
        return fib(number-1)+fib(number-2)

number = int(input("Enter a number: "))
print(fib(number), "is the", number, "fibonacci number")





def gcd(a, b):
  a,b = max(a,b), min(a,b)
  if b == 0:
    return a
  else:
    return gcd(b, (a % b))


a= int(input("Enter a number: "))
b = int(input("Enter a number: "))


result = gcd(a, b)
print("The Greatest Common Divisor of", a, "and", b, "is:", result)