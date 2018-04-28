# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 06:41:33 2018

@author: Scott Warnock
"""

# change2.py
#
#   A program to calculate the value of some change in dallars.
#   This version represents the total cach in cents.

def main():
    print("Change counter\n")
    
    print("Please enter the count of each coin type.")
    q = eval(input("Quarters: "))
    d = eval(input("Dimes: "))
    n = eval(input("Nickles: "))
    p = eval(input("Pennies: "))
    
    t = (q * 25) + (d * 10) + (n * 5) + (p * 1)
    
    print("The total value of your change is ${0}.{1:0>2}"
         .format(t//100, t%100))
    
main()