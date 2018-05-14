# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:50:58 2018

@author: Scott Warnock
"""

# program: mann_simple.py
#   The simple version of manx.py

def main():
    x1, x2, x3 = eval(input("Please enter three values: "))
    print("\nThe largest value is", max(x1, x2, x3))
    
main()