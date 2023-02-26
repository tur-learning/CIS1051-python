def check(height):
    if height > 0:
        return True
    else:
        return False


height = int(input("Height :  "))
is_positive = check(height)
while is_positive == False:
    height = int(input("Height (positive value):  "))
    is_positive = check(height)

for i in range(height):
    print(" "*(height - i - 1)+"#"*(i+1)+"  "+"#"*(i+1)+" "*(height-i-1))
