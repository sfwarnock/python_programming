# -*- coding: utf-8 -*-
"""
Created on Mon May 21 2018

@author: Scott Warnock
"""

# exercise 7.7.py
#
# A babysitter charges $2.50 an hour until 9:00PM when the rate drops to $1.75 an hour
#   (the children are in bed).  Wrtie a program that accepts a starting time and ending time
#   in hours and mintues and calcualtes the total babysitting bill.  You may assume that the 
#   starting and ending times are in a single 24-hour period.  Partial hours should be
#   appropriately prorated.

def main():
    starTime = eval(input("Enter start time (hour.min): "))
    
    endTime = eval(input("Enter finish time (hour. min): "))
    
    if endTime <= 21.00:
        totalCost = (endTime - starTime) * 60 * .042
        print("$", round(totalCost,2))
    
    elif endTime > 21.00:
        beforeNine = (21.00 - starTime) * 60 * .042
        afterNine = (endTime - 21.00) * 60 * .030
        totalCost = beforeNine + afterNine
        print("$", round(totalCost,2))

main()