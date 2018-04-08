# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 19:12:49 2018

@author: Scott Warnock
"""

# factorial.py
#   Program to compute the factorial of number
#   Illustrates for loop with an accumulator

def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()