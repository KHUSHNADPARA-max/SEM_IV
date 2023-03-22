amount = float(input("Enter an amount in dollar : "))
cents = (amount * 100)
dollars = cents // 100
remaining_cents = cents % 100

quarter = remaining_cents//25
remaining_cents = cents % 25

dimes = remaining_cents// 10
remaining_cents = cents % 10

nickel = remaining_cents // 5
remaining_cents = cents % 5

pennies = remaining_cents // 1
remaining_cents = cents % 1 

print("Your amount", amount, "consists of")
print(dollars, "dollars")
print(quarter,"quarter")
print(dimes,"dimes")
print(nickel,"nickel")
print(pennies,"pennies")