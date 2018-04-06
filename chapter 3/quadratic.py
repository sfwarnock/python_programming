# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 06:30:55 2018

@author: Scott Warnock
"""

# quadratic.py
#   A program that computes the real roots of a quadratic equation.
#   Illustrates use of the math library.
#   Note: this program crashed is the equation has no real roots.

import math # Makes the math library avaliable.

def main():
    print("This program finds the real solutions to a quadratic")
    print()
    
    a, b, c, = eval(input("Please enter the coefficients (a, b, c,): "))
    
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    
    print()
    print("The solutions are: ", root1, root2)

main()