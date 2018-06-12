# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 2018

@author: Scott Warnock
"""

# exercise8.7.py
#
#   The Goldbach conjecture asserts that every number is the sum of two prime numbers.
#   Write a program that gets a number from the user, checks to make sure it is even,
#   and then finds the two prime numbers that add up to the number.

def main():
    n = eval(input("Enter a number: "))
    
    y, x = 2, 3
    
    z = x + y
    
    if n % 2 == 0:
        x = n / 2
        print (x)
    else:
        while z != n:
            x += 1
            z = x + y
        print(x, y,n)

main()