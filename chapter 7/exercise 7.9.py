# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2018

@author: Scott Warnock
"""

# exercise 7.9.py
#
# A formula for computing Easter in the years 1982-2048, inclusive, is as follows:
#   let a = year%19, b = year%4, c = year%7, d = (19a + 24)%30, c = (2b + 4c + 6d +5)%7.
#   The date of Easter is March 22 + d + e (which could be in April).  Write a program
#   that inputs a year, verfies that it is in the proper range, then prints out the date
#   of Easter that year.

def main():
    year = eval(input("Enter a year between 1982 and 2048: "))
    
    a = year % 19
    
    b = year % 4
    
    c = year % 7
    
    d = ((19 * a) + 24) % 30
    
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

    
    if year >= 1982 and year <= 2048:
        date = (22 + d + e) -31
        if date >= 22:
            print ("The date of Easter is March", date, year)
        elif date <= 23:
            print("The date of Easter is April", date, year)
                 
main()