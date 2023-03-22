fname=str(input("Enter First Name : "))
lname=str(input("Enter Last Name : "))
dob=str(input("Enter Your Date Of Birth(DD/MM/YYYY) : "))
add=str(input("Enter Your Address : "))

print("Filled Details")
print("First Name",fname)
print("Last Name",lname)
print("Date Of Birth",dob)
print("Address",add)

from datetime import datetime
time=datetime.now()
etime=time.strftime("%H:%M:%S")
print("Last edited",etime)



