# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 2018

@author: Scott Warnock
"""

# month.py
#
#   A program that outputs the month for the given month number.

def main():
    #   months is used as a lookup table.
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    
    n = eval(input("Enter a month number (1-12): "))
    
    #   compute starting postion of month n in months.
    pos = (n-1) * 3
    
    #   Grab the appropriate slice from months.
    monthAbbrev = months[pos:pos+3]
    
    #   print the results
    print("The month abbreviation is", monthAbbrev + ".")
    
main()