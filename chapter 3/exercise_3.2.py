# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 06:18:51 2018

@author: Scott Warnock
"""

#3.2
#   Write a progam the calculates the cost per square inch of a circular pizza, given its diameter and price.
#   The formula for area is A = pir^2

import math

def main():
    r = eval(input("Enter the size of your pizza pie in inches: "))
    c = eval(input("Enter the cost of your pizza pie in dollars: "))
    p = math.pi
    a = p * (r**2)
    ac = a / c
    print ("The total area of your pizza is", round(a), "inches squared")
    print ("The cost of pizza per square inch is: $",round(ac))
main()