# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 06:05:13 2018

@author: Scott Warnock
"""

# Exercise 3.6
#   Two points in a plave are specified using the coordinates (x1,y1) and (x2,y2).
#   Write a program that calculates the slope of a line through two (non-vertical)
#   points entered by the user.
#
#   slope = y2 - y1 / x2 - x1

def main():
    x1, y1 = eval(input("Enter the two cordinates of the first point with a commma in between: "))
    x2, y2 = eval(input("Enter the two cordinates of the second point with a commma in between: "))
    
    s = (y2 - y1) / (x2 - x1)
    
    print("The slope of the line through the two given coordinates is: ",s)
    
main()