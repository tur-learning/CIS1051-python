def calculate_BMR_female(w, h, a):
    value = ((9.5634*w)+(1.8496*h)-(4.6756*a)+655.0955)//214
    return value

def calculate_BMR_male(w, h, a):
    value = ((13.7516*w)+(5.0033*h)-(6.755*a)+655.473)//214
    return value

weight = 52
height = 160 
age = 18
sum = calculate_BMR_female(weight, height, age), calculate_BMR_male(weight, height, age)
print ("number of chocolate bars (female, male) :", sum)



def convert_temp(C):
    F = C*(9/5)+32
    return F

temperature_in_celsius = 10
sum = convert_temp(temperature_in_celsius)
print(sum)



def find_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    rem_seconds = seconds % 60
    return (f"{hours} hours {minutes} minutes {rem_seconds} seconds")

# prompt user
input_sec = 10000 

# calculate 
sum = find_time(input_sec)

# display result
print(input_sec, "seconds =", sum)
