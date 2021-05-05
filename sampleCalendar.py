"""
Creating sample calendar with data now
Author = Francisco Junior
"""

#Importing libraries
import datetime


#Creating variable with data now
dateNow = datetime.datetime.now()


#Printing date
print(dateNow.strftime("%Y-%m-%d"))
