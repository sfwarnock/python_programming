# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:51:04 2018

@author: Scott Warnock
"""

# program: maxn.py
#   Finds the maximum of a series of numbers.

def main():
    n = eval(input("How many numbers are there? "))
    
    #   set max to be the frist value
    maxn = eval(input("Enter a number >> "))
    
    #   now compare the n-1 successive values
    for i in range(n-1):
        x = eval(input("Enter a number>> "))
        if x > maxn:
            maxn = x
    
    print("\nThe largest value is", maxn)
    
main()