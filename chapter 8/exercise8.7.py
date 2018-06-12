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
    
    if n % 2 == 0:
        print("Number is even.")
    else:
        print("No two prime number sum to the total of", n)

main()