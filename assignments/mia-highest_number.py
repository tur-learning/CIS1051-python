def input_numbers():
    numbers = int(input("Input Number: "))
    return numbers

n = input_numbers()

for i in range(5):
    number = input_numbers()
    if number > n:
        highest_number = number
        n = highest_number

print(f"The highest number was: {n}")


