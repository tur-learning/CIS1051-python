def calculateBMRmale():
    BMR = (13.7516*weight)+(5.0033*height)-(6.755*age)+66.473
    bar = BMR/214
    return bar

def calculateBMRfemale():
    BMR = (9.5634*weight)+(1.8496*height)-(4.6756*age)+655.0955
    bar = BMR/214
    return bar

weight = 60
height = 170
age = 25

sum = calculateBMRmale()
print(sum)

sum = calculateBMRfemale()
print(sum)


def calculate_temp():
    fahrenheit = (celcius*(9/5))+32
    return fahrenheit

celcius = int(input('what is the temp in celcius?'))
sum = calculate_temp()
print(sum)


seconds = int(input('what is the total time in seconds?'))
def calculate_time():
    hours = int(seconds/3600)
    minutes = int((seconds-(hours*3600))/60)
    seconds2 = int(seconds-(minutes*60)-(hours*3600))
    return hours, minutes, seconds2

sum = calculate_time()
print(sum)

    