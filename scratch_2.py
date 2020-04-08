import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
end = ("..!" )
print ("Hello  " + fname.capitalize()+ " " + lname.capitalize() + end)

