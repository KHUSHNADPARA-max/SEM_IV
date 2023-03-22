import random

num=random.randint(0,1000)
print("Random Num is :",num)

sum = 0
while num>0:
    digit=num%10
    sum += digit
    num //= 10

print("Sum Of Random Num's Digit",sum)