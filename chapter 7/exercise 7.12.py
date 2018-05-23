# -*- coding: utf-8 -*-
"""
Created on Wed May 23 2018

@author: Scott Warnock
"""

# exercise 7.12.py
#
# Write a program that accepts a date in the form month/day/year and outputs whether
#   or not the date is vallid.  For example 5/24/1962 is valid, by 9/31/2000 is not.
#   (September has only 30 days.)

def main():
    date = input("Enter the month/day/year: ").split('/')
    
    month = date[0]
    
    day = date[1]
    
    month28 = 2
    
    month30 = [4, 6, 9, 11]
    
    month31 = [1, 3, 5, 7, 8, 10, 12]
    
    if int(month) == month28:
       print ("The date you entered is valid.")
    elif int(month) in month31 and int(day) <= 31:
        print ("The date you entered is valid.")
    elif int(month) in month30 and int(day) <= 30:
        print ("The date you entered is valid.")
    else:
        print("The date you entered is not valid.")
        
main()