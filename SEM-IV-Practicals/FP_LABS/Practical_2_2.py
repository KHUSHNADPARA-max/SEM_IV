import random

lottery = str(random.randint(10,99))
user_input = input("Enter a two digit number :")
print(lottery)

if user_input==lottery:
    print("congratulation ! you have won $10,000")
elif sorted(user_input)==sorted(lottery):
    print("congratulation ! you have won $5,000")
elif any(i in lottery for i in user_input):
    print("congratulation ! you have won $2,000")
else :
    print("sorry, you have not won anything")
