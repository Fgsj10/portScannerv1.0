"importing libraries for pinrting calendar"
"Author = Francisco junior"

import calendar

#Variables and input user data

year = int(input("Enter a year, please: "))
month = int(input("Enter a month, please: "))


#Printing calendar reference of data inputed of user
print(calendar.month(year, month))