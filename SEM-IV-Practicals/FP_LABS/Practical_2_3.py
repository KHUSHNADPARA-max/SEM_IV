import random

ran_num = str(random.randint(0,100))
gs_num = 0 

while gs_num != ran_num :
    gs_num = str(input("Guess a magic number between 0 and 100 : "))

    if gs_num > ran_num :
        print("your guess is too high")
    elif gs_num < ran_num :
        print("your guess is too low")
    else :
        print("yes,the number is : ",ran_num)