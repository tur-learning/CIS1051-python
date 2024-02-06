def input_number():
    n=int(input("input number:"))
    return n


highest_number=0  
 
for i in range(5):
    number = input_number()
    if number>highest_number:
        highest_number=number
    

print(f"The highest number was..."+str(highest_number))


import random
number=random.randint(1,100)



def input_number():
    n=int(input("guess a number 1-100:"))
    guess_number(n)
    
def guess_number(guess):
    if guess==number:
        print('Congratulations You Win!')
        return
    elif guess<number:
        print('Too Low')
        guess=input_number()
    elif guess>number:
        print('Too High')
        guess=input_number()
    
    

guess=input_number()




