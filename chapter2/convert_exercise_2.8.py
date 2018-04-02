# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 15:15:06 2018

@author: Scott Warnock
"""

# convert.py
#   A program to convert Fahrenheit temps to Celsius
#
#   Pseudocode: Input the temperature in degrees Fahrenheit (call it f)
# Calculate celsius as (5/9) f - 32
# Output celsius.
# Request user input 5 times before program quits.

def main():
    for temp in range(5):
        f = eval(input("What is the Fahernheit temperature? "))
        c = (f - 32) * 5/9
        print("The temperature is", c, "degrees celsius.")

main()