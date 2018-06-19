# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 2018

@author: Scott Warnock
"""

# exercise8.9.py
#
#   Write a program that computes the fuel efficiency of a multi-leg journey.
#   The program will first prompt the for the starting odometer reading and then
#   get information about a series of legs.  For each leg, the user enters the odometer
#   reading and the amount of gas used (separated by a space).  The user signals the end
#   of the trip with a blank line.  The program should print out the miles per gallon
#   achived on each leg and the total MPG for the trip.

def main():
    
    gasTankEmpty = eval(input("Please enter the total volume in gallons of your gas tank: "))
    
    lastFillUp = eval(input("Enter the volume, in gallons, of your last fill up: "))
    
    odometerStart = eval(input("Please enter the starting odometer reading: "))
    
    odometerFinish = eval(input("Enter the ending odometer reading: "))
        
    mpg = (odometerStart - odometerFinish) / (lastFillUp - gasTankEmpty) 
    
    print(mpg)
    
main()