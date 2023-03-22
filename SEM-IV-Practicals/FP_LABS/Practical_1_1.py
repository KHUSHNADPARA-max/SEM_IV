from datetime import date
import calendar
d,m,y=input("Enter D.O.B (DD/MM/YYYY) of shyam's grandfather :").split("/")
d=int(d)
m=int(m)
y=int(y)
today=date.today()
a=today.year-y
if today.month<m:
    a=a-1
elif today.month==m:
    if today.day<d:
        a=a-1
print(f"shyam's Grandfather's age is {a}")
print(f"calender of {m},{y} is :")
print(calendar.month(y,m))