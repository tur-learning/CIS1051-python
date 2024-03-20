import math

def sq_rt(s, x_0) :
    accuracy = 1e-12
    diff = 1

    while abs(diff) > accuracy:
        x = 0.5 * (x_0 + s/x_0)
        diff = x_0 - x
        x_0 = x
    return x


s = float(input("Input a positive real number: "))
x_0 = float(input("Input an estimate of the square root: "))

square_root = math.sqrt(s)
result_heron = sq_rt(s, x_0)

error = (result_heron - square_root)
print(f"The square root of {s} is: {square_root}. The error of Heron's algorithm was {error}.")
