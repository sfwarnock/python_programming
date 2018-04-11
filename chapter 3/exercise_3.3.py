# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 06:05:07 2018

@author: Scott Warnock
"""

# Exercise 3.3
#   Write a prgram that determines the molecular weight of a hydrocarbon based on the number
#   of hydrogen, carbon, and oxygen atoms. You should use the folling weights:
#   Atom      Weight (grams/mole)
#   H             1.0079
#   C             12.011
#   O             15.9994

def main():
    h, c, o = 1.0079, 12.011, 15.9994 
    
    ha = eval(input("Enter the number of the hydrogen atoms: "))
    ca = eval(input("Enter the number of the carbon atoms: "))
    oa = eval(input("Enter the number of the oxyen atoms: "))
    
    tw = (ha * h) + (ca * c) + (oa * o)
    print()
    print("The total weight of the given hydrocarbon is:", round(tw,3),"grams/mole.")
    
main()