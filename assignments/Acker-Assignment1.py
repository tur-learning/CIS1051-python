import math

weight = int(input("what is your weight?"))
height = int(input ("what is your height?"))
age = int(input("what is your age?"))


def maleBMR(weight,height):
    BMR=(13.7516 * weight) + (5.0033 * height) - (6.755 * age) + 66.473
    chocBar1= BMR/214
    return chocBar1

finalBarsmale = maleBMR(weight,height)
print("if you are Male you need " + str(finalBarsmale) + " chocolate bars.")



def femaleBMR(weight,height):
    BMR=(9.5634 * weight) + (1.8496 * height) - (4.6756 * age) + 655.0955
    chocBar2= BMR/214
    return chocBar2

finalBarsfemale = femaleBMR(weight,height)
print("if you are Female you need " + str(finalBarsfemale) + " chocolate bars.")


Celsius = int(input("What is the temp in Celsius?"))

def CtoF(Celsius):
    Fahrenheit = Celsius * (9/5) + 32
    return Fahrenheit

ConvertTemp = CtoF(Celsius)
print("The tempature " + str(Celsius) + " Celsius is equal to " + str(ConvertTemp) + " in Fahrenheit.")


totalSeconds = int(input("What is the total time in seconds?"))

def timeHours(totalSeconds):
    valueHours = int(totalSeconds/60/60)
    return valueHours

def timeMinutes(totalSeconds):
    valueMinutes = int((totalSeconds%3600)/60)
    return valueMinutes

def timeSeconds(totalSeconds):
    valueSeconds = int(totalSeconds%60)
    return valueSeconds

hours = timeHours(totalSeconds)
minutes = timeMinutes(totalSeconds)
seconds = timeSeconds(totalSeconds)

print(str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds")