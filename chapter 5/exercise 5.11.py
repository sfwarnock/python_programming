# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:00:41 2018

@author: 175272
"""

# exercise 5.11.py
#
# Write an imporved version of the Chaos program from Chpater 1.  The new program prints a nicely
#   formatted table showing how the values change over time.


def main():
    print("This progam illustrates a chotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("How many numbers should the program print? "))
    
    dash = '-' * 25
    
    print ('{:10}{:10}'.format(x,y))
    print (dash)
    
    for i in range(n):
        x = 3.9 * x * (1-x)
        y = 3.9 * (y - y * y)
        print ('{:10}{:10}'.format(round(x,4), round(y,4)))
main()