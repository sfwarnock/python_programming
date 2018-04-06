# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 06:08:37 2018

@author: Scott Warnock
"""

# changne.py
# A program to calculate the of pocket change.

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type: ")
    q = eval(input("Quarters: "))
    d = eval(input("Dimes: "))
    n = eval(input("Nickels: "))
    p = eval(input("Pennies: "))
    t = q * .25 + d * .10 + n *.05 + p * .01
    print()
    print("Total value of your change is", t)
    
main()