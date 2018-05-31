# -*- coding: utf-8 -*-
"""
Created on Thu May 31 2018

@author: Scott Warnock
"""

# triangletype.py
#
#   Wrtie a program to check if a triangle is equalateral, isosceles, or scalene.

def main():
    print("This program checks whether a triangle is equilateral, isosceles, or scalene.")
    x = eval(input("Enter length of x: "))
    y = eval(input("Enter length of y: "))
    z = eval(input("Enter length of z: "))
    
    if x != y and x != z and z != y:
        print("The triangle is scalene.")
    elif x == y and x == z and y == z:
        print("The triangle is equilateral.")
    else:
        print("The triangles is isosceles.")

main()