#CALCULATING BMR FOR BOTH MEN AND WOMEN
#calculate bmr for male
def calculate_bmr_male(weight, height, age):
    maleBMR = (13.7516 * weight) + (5.0033 * height)-(6.755 * age) + 66.473
    return maleBMR

weight = 50
height = 170
age = 35
sum = maleBMR = (13.7516 * weight) + (5.0033 * height)-(6.755 * age) + 66.473
print(sum)

#calculate bmr for female
def calculate_bmr_female(weight, height, age):
    femaleBMR = (9.5634 * weight) + (1.8496 * height)-(4.6756 * age)+ 655.0955
    return femaleBMR

weight = 79
height = 150
age = 30
sum1 = femaleBMR = (9.5634 * weight) + (1.8496 * height)-(4.6756 * age)+ 655.0955
print(sum1)


#CONVERTING TEMPERATURE
celsius = float(input("What is the temperature in degrees Celsius?\n"))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit is:")
print(fahrenheit)


#CONVERTING TIME
time = int(input("Enter time in seconds: "))
day = time // (24 * 3600)
time = time - (24 * 3600)
hour = time // 3600
minutes = time // 60
seconds = time

print("Day {} Hour {} Minute(s) {} Second(s) {}".format(day,hour, minutes,seconds))
