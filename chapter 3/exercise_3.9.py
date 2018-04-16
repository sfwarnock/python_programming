# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16, 2018

@author: Scott Warnock
"""

# Exercise 3.9
#
#   Wrtie a program to calculate the area of a triangle given the length of its
#   three side a, b, and c using these formulas.
#
#   s = a + b + c / 2
#
#   a = sqrt(s(s-a)(s-b)(s-c)))

import math

def main():
    
    a, b, c, = eval(input("Enter the lengths of each side of the given triangle: "))
    
    s = (a + b + c) / 2
    
    a = math.sqrt(s * (s - a) * (s - b) * (s-c))
    
    print()
    print("The area of the given triangle is:", round(a,2))
    
main()