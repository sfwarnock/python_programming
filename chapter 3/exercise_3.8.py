# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 06:33:17 2018

@author: Scott Warnock
"""

# Exercise 3.8
#
#   The Gergorian epact is the number of days between January 1st and the previous new moon.
#   This value is used to figure out the date of Easter.  It is calculated by these formulas (using int arithmetic):
#
#   c = year // 100
#
#   epact = (8 + (c // 4) - c + ((8c + 13) // 25) + 11(year % 19)) % 30
#
#   Write a program that prompts the user for a four digit year and then outputs the value of the epact.

def main():
    y = eval(input("Enter the four digit year: "))
    
    c = y // 100
    
    ep = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (y % 19) % 30)
    
    print("The Gregorian epact is", ep, "days after January 1st in", y)
    
main()