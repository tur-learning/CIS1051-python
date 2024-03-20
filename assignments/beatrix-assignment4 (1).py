import math

num = float(input("Enter a number to sqaure root: "))

two = float(input("Enter a guess: "))

def heron(x): #implements Heron's method to approximate the square root
    output=(1/2)*(x+num/x)
    return output

def answer(x): #iteratively applies the heron function until the desired error threshold is reached
    counter=0
    while abs(math.sqrt(num)-x)>=(10**-12):
        counter=counter+1
        call_function=heron(x)
        x=call_function
    return x, counter

calculate = answer(two)[0]
calculate1=answer(two)[1]
error=abs(((calculate)/(math.sqrt(num))-1)*100)



print("The square root calculated by the program is " +(str(calculate)))
print("It took " +str((calculate1)) +" iterations to reach the desired error threshold")
print("The error of the calculated value of the sqaure root is "+(str(error))+" percent")












