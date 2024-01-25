# Problem 1
def calculate_bmr(weight, height, age):
    return (66 + (6.2 * weight) + (12.7 * height) - (6.76 * age))

print("\n\n---------- PROBLEM 1 - BMR & CHOCOLATE BARS ----------")
user_weight = int(input("\nEnter your weight: "))
user_height = int(input("Enter your height: "))
user_age = int(input("Enter your age: "))

user_bmr = calculate_bmr(user_weight, user_height, user_age)
chocolate_bars = user_bmr/214

print("You must eat", chocolate_bars, "chocolate bars to maintain your weight.")

# Problem 2
def celsius_to_fahrenheit(celsius):
    return (celsius * float(9/5) + 32)

print("\n\n---------- PROBLEM 2 - CELSIUS TO FAHRENHEIT ----------")
celsius_value = float(input("\nCelsius value: "))
fahrenheit_value = celsius_to_fahrenheit(celsius_value)
print(celsius_value, "in fahrenheit is", fahrenheit_value)

# Problem 3
def convert_seconds(seconds):
    hours = seconds // 3600 
    minutes = (seconds % 3600) // 60 
    remaining_seconds = seconds % 60 
    return hours, minutes, remaining_seconds

print("\n\n---------- PROBLEM 3 - CONVERTING SECONDS ----------")
user_seconds = int(input("\nNumber of seconds: "))
total_hours, total_minutes, total_seconds = convert_seconds(user_seconds)
print(total_hours, "hours,", total_minutes, "minutes,", total_seconds, "seconds")