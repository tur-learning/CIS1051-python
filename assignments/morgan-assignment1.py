def calculateBMRmale():
    BMR = (13.7516*weight)+(5.0033*height)-(6.755*age)+66.473
    bars = BMR/214
    return bars

def calculateBMRfemale():
    BMR = (9.53634*weight)+(1.8496*height)-(4.6756*age)+655.0955
    bars = BMR/214
    return bars

weight = 60
height = 2.55 
age = 18
sum = calculateBMRmale()
print('chocolate bars male = ', sum)
sum = calculateBMRfemale()
print('chocolate bars female = ', sum)

def calculatecelcius():
    F = C*(9/5)+32
    print (F)

def calculatefahrenheit():
    Fahrenheit = C*(9/5)+32
    return Fahrenheit

C = 25
sum = calculatefahrenheit()
print('Fahrenheit = ', sum)

def calculatehours():
    hours = seconds/3660
    return int(hours)

def calculateminutes():
    hourrem = seconds%3660
    minutes = hourrem/60
    return int(minutes) 

def calculatesec():
    hourrem = seconds%3660
    minuterem = hourrem%60
    return minuterem
seconds = 5000

sum = calculatehours()
print ('Hours = ', sum)
sum = calculateminutes()
print ('Minutes =', sum)
sum = calculatesec()
print ('Seconds = ', sum)