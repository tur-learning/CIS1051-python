def calculate_BMR_Male(w,h,a):
   value=((13.7516*w)+(5.0033*h)-(6.755*a)+66.473)/214
   return value
def calculate_BMR_Female(w,h,a):
    value=((9.5634*w)+(1.8496*h)-(4.6756*a)+655.0955)/214
    return value
weight = 60
height =70
age=16

sum = calculate_BMR_Male(weight,height,age)
#sum = calculate_BMR_Female(weight,height,age)
print("males number of chocolate bars to be consumed is",sum)
sum = calculate_BMR_Female(weight, height, age)
print("females number of chocolate bars to be consumed is",sum)


def calculate_degrees(c):
    value=c*(9/5)+32
    return value
c=int(input("degrees in celsius"))
answer=calculate_degrees(c)
print("the temperature is", answer,"fahrenheit")


seconds=int(input("What is the total number of seconds"))
def calculate_Hours(seconds):
    value=int(seconds/3600)
    return value

def calculate_minutes(seconds):
    value=int((seconds%3600)/60)
    return value

def calculate_seconds(seconds):
    value=(seconds%60)
    return value

hours=calculate_Hours(seconds)
minutes=calculate_minutes(seconds)
seconds=calculate_seconds(seconds)

print("HOURS:",hours,"MINUTES:",minutes,"SECONDS:",seconds)

    
