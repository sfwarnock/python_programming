# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7  2018

@author: Scott Warnock
"""

# exercise8.5.py
#
#   A postive whole number n>2 is prime if no number between 2 and Sprt(n) (inclusive)
#   evenly divides n.  Write a program that accpets a value of n as input and determines
#   if the value is prime.  If n in not prime, your program should quit as soon as as it 
#   finds a value that evenly divides n.

import math

def main():
    n = eval(input("Enter a whole number: "))
    
    x = math.sqrt(n)
    
    if n % 2 == 0:
        print(n,"is not prime.")
    elif x == int(x):
        print(n,"is not prime.")
    else:
        print(n,"is prime.")
        
main()