# -*- coding: utf-8 -*-
"""
Created on Thu May 17 2018

@author: Scott Warnock
"""

# exersice 7.1.py
#
#   Many companies pay time-and-a-half for any hours worked above 40 in a given
#       week.  Wrtie a program to input the number of hours worked and the hourly
#       rate and calculate the total wages for the week.

def main():
    hours = eval(input("Enter number of hours worked: "))
    
    wage = eval(input("Enter hourly wage: "))
    
    if hours <= 40:
        totalwages = hours * wage
        print ("Your total wages for the week are $",totalwages)
    else:
        hoursOver = hours - 40
        overTime = hoursOver * (wage * 1.5)
        regTime = 40 * wage
        totalwages = overTime + regTime
        print ("Your total wages for the week are $",totalwages)
        
main()