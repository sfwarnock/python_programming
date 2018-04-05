# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 06:07:28 2018

@author: Scott Warnock
"""

# This program converts pounds to kilograms.

print("This progam converts pounds to kilograms.")

def main():
    lbs = eval(input("Enter the number of pounds: "))
    kg = lbs * .4535
    
    print(lbs,"lbs. is equal to", kg,"kg." )

main()