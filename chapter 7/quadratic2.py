# -*- coding: utf-8 -*-
"""
Created on Tue May  8 2018

@author: Scott Warnock
"""

#   quadratic2.py

import math

def main():
    print("This program finds the real solutions to a quadratic\n")
    
    a, b, c = eval(input("Please enter the coefficients (a,b,c): "))
    
    discrim = (b * b) - 4 - (a * c)
    if discrim >= 0:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", round(root1,3), round(root2,3))

main()