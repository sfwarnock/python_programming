# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 06:33:18 2018

@author: Scott Warnock
"""

# Exercise 3.7
#
#   Write a program that accepts two points and determines the distance between them.
#
#   distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

import math

def main():
    
    x1, y1 = eval(input("Enter the coordinates of the first point: "))
    x2, y2 = eval(input("Enter the coordinates of the second point: "))
    
    z = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    
    d = math.sqrt(z)
    
    print()
    print("The distance between the two give points is: ",round(d,2))
    
main()