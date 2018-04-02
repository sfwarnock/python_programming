# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:41:07 2018

@author: Scott Warnock
"""

# futval_2.7.py
#   A program to compute the value of an investment carried 10 years into the future as the user enters.

def main():
    print("This program calculate the future value of a investment over a user selected duration.")
    
    p = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    a = eval(input("Enter the number of periods per year intrest is compounded: "))
    
    for i in range(10 * a):
        p = p * (1 + (apr / a))
        
    print("The value in 10 years is:", p)
    
main()