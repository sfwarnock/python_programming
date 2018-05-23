# -*- coding: utf-8 -*-
"""
Created on Wed May 23 2018

@author: Scott Warnock
"""

# exercise 7.11
#
# A year is a leap year if it is divisible by 4, unless it is a century year that is not
#       divisible by 400. (1800 and 1900 are not leap years while 1600 and 2000 are.)
#       Write a program that calculates whether a year is a leap year.

def main():
    leapYear = input("Enter four digit year: ")
    
    if leapYear.endswith('00') and int(leapYear) % 400 == 0:
        print ("The year you entered is a leap year.")
    elif leapYear.endswith('00') and int(leapYear) % 400 != 0:
        print ("The year you entered is not a leap year.")   
    elif int(leapYear) % 4 == 0:
        print ("The year you entered is a leap year.")
    else:
        print ("The year you entered is not a leap year.")

main()