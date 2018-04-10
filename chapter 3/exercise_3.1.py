# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 06:14:39 2018

@author: Scott Warnock
"""

# 3.1
#   Write a program to calculate the volume and surface area of a sphere from its radius, given as input.
#   Here are some some formulas that might be useful.
#   V = 4/3pi^3
#   A = 4pir^2

import math

def main():
    r = eval(input("Enter the radius, in inches, of the sphere: "))
    p = math.pi
    v = (4/3) * p * (r **3)
    a = 4 * p * (r ** 2)    
    print("The volume of the given sphere is: ",round(v, 3),"inches cubed.  And the area of the given sphere is ", round(a, 3), "inches squared.")
main()