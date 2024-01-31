def calculate_BMR_female(w,  h, a):
    value = ((9.5634*w)+(1.8496*h)-(4.6756*a)+655.0955)//214
    return value

def calculate_BMR_male(w, h, a):
        value = ((13.7516*w)+(5.0033*h)-(6.755*a)+655.473)//214
        return value 

weight = 74
height = 171
age = 19
sum1 = calculate_BMR_female(weight, height, age)
sum2 = calculate_BMR_male(weight, height, age)
print ("number of chocolate bars (female, male):",sum1, sum2)



def convert_temp(c):
    f = c*(9/5)+32
    return f 

temperature_in_celcius = 100
sum = convert_temp(temperature_in_celcius)
print(sum)


def find_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    rem_seconds = seconds % 60
    print(f"{hours} hours {minutes} minutes {rem_seconds} seconds")

seconds = 10000
find_time(seconds)