# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17

@author: 175272
"""

# Exercise 3.12
#
#   Write a program to find the sum of the cubes of the first natural numbers where
#   the value of n is provided by the user.

def main():
    n = eval(input("Enter a number: "))
    
    s = (n **2 * (n + 1) ** 2) / 4
    
    print("The first sum of cubes of the first natural number you entered is",s)
    
main()