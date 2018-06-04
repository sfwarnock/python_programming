# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 2018

@author: Scott Warnock
"""

# exercise8.3.py
#
#   Write a program the uses a while loop to determine how long it takes for an
#   investment to double at a given interest rate.  The input will be an annualized
#   interest rate, and the output is the number of years if takes an investment to 
#   double.  Note: the amount of the intial investment does not mater; you can use
#   $1.

def main():
    apr = eval(input("Enter the APR (input as .##): "))
    
    total = 0
    
    year = 0
    
    while total <= 13000:
        year += 1
        total = 6500 * (( 1 + (apr / 12)) ** (12 * year))
    print ("At a", apr, "percent APR, it will take", year, "years to double your investment.")
        
main()