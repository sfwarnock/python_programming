# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 06:05:07 2018

@author: Scott Warnock
"""

# Exercise 3.4
#
#   Write a progrm that determines the distance to a lightning strike based on the time
#   elapsed between the flash and the sound of the thunder.  The speed of sound is 
#   approximately 1100ft/sec and 1 mile is 5280 ft.

def main():
    s = 1100
    m = 5280
    
    t = eval(input("Enter the number seconds between flash and the sounds of thunder: "));print()
    
    d = (t * s) / m
    
    print("The lightning is approximately", round(d,2),"miles away.")
    
main()