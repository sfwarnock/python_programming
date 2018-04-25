# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 2018

@author: Scott Warnock
"""

# month2.py
#
#   A program to print the month abbreveation, given its number.

def main():
    
    #   month is a list used as a lookip table.
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Nov", "Dec"]
    
    n = eval(input("Enter a month number(1-12): "))
    
    print("The month abbreviation is", months[n-1] + ".")
    
main()