# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:41:07 2018

@author: Scott Warnock
"""

# futval_2.6.py
#   A program to compute the value of an investment carried as many years into the future as the user enters.

def main():
    print("This program calculate the future value of a investment over a user selected duration.")
    
    p = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter the number of years of our investment: "))
    a = eval(input("Enter the yearly contrubution after year one: "))
    
    for i in range(x):
        p = (p * (1 + apr)) + ((a * (1 + apr)) - a) / apr
        
    print("The value in",x, "years is:", p)
    
main()