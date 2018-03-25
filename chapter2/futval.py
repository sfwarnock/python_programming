# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:41:07 2018

@author: Scott Warnock
"""

# futbal.py
#   A program to compute the value of an investment carried 10 years into the future.

def main():
    print("This program calculate the future value of a 10-year investment.")
    
    p = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate:"))
    
    for i in range(10):
        p = p * (1 + apr)
        
    print("The value in 10 years is: ", p)
main()