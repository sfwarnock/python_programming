# -*- coding: utf-8 -*-
"""
Created on Tue May  8 2018

@author: Scott Warnock
"""

# convert2.py
#   A program to convert Celsius temps to Fahrenheit.
#   This version issues heat and cold warnings.

def main():
    c = eval(input("What is the Celsius temperature? "))
    f = (9/5 * c) + 32
    print ("The temperature is", f, "degrees Fahrenheit.")
    
    #print warnings for extreme temps.
    if f > 90:
        print ("It's really hot out there. Be careful!")
    if f < 30:
        print ("Brrrrr, Be sure to dress warmly!")

main()