import math 


factNum = int(input("Give a number to factorial  "))


def calculate_fact(n):
    if n == 1:
        return n
    else:
        return n*calculate_fact(n-1)

solution = calculate_fact(factNum)
print(str(solution))


fibNum = int(input("Give a number  "))

def calculate_fib(n):
    if n <= 1:
        return n
    else:
       output = calculate_fib(n-1) + calculate_fib(n-2)
       return output
    
print(str(calculate_fib(fibNum)))


firstNum = int(input("Give the first number:  "))
secondNum = int(input("Give the second number:  "))

def GCD_calc(n1, n2):
    if n2 > n1:
        if n2 % n1 == 0:
            return n1
        else:
            return GCD_calc(n2%n1,n1)
    else:
        if n1 % n2 == 0:
            return n2
        else:
            return GCD_calc(n2,n1%n2)

GCDoutput = GCD_calc(firstNum,secondNum)
print(GCDoutput)
