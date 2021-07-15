import sys
import datetime

def yearOfPerson(old):
    current_time = datetime.datetime.now()
    age=int(old)
    if age<0 or age>100:
        return -1
    numberOfYear = 100-age
    current_year= int(current_time.year)
    current_year+=numberOfYear
    return current_year
    
  
name = input("Give me your name: ")
print("Your name is: "+name)
old = input("Give me your old: ")
age= int(old)
print("Your age: "+str(age))
current_year =  yearOfPerson(age)
if current_year ==-1:
    print("Age is not right!!!")
else: print(current_year)


