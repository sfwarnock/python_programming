# -*- coding: utf-8 -*-
"""
Created on Wed May 30 2018

@author: Scott Warnock
"""

# sum double.py
#
# Given two int values, return thier sum, unless the two values are the same, return
#   double their sum.

def main():
    x, y = eval(input("Enter two numbers: "))
    
    if x == y:
        solution = (x + y) * 2
    else:
        solution = x + y
    print(solution)
       
main()