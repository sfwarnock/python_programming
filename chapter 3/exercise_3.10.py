# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16, 2018

@author: Scott Warnock
"""

# Exercise 3.10
#
#   Wrtie a program to determine the length of a ladder required to reach a given height
#   when leaned against a house.  The height and angle of the ladder are given inputs. To
#   compute the length use
#
#   length = height / sin angle
#
#   Note: The angle must be in radians.  Prompt for an angle in degrees and use this formula to convert:
#
#   radians = (pi / 180) * degrees

import math

def main():
    a = eval(input("What is the desired angle of your ladder? "))
    h = eval(input("What is the height of the house? "))
    
    r = (math.pi / 180) * a
    
    l = h / math.sin(r)
    
    print()
    print("The proper length of the ladder should be ", round(l,2),"feet.")
    
main()