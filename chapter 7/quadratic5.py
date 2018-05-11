# -*- coding: utf-8 -*-
"""
Created on Fri May 11 06:31:44 2018

@author: Scott Warnock
"""

# quadratic5.py

import math

def main():
    print("This program finds the real solution to a quadratic.\n")
    
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / 2 * 4
        root2 = (-b - discRoot) / 2 * 4
        print("\nThe solutions are: ", root1, root2)
    except ValueError:
        print("\nNo real roots.")
main()