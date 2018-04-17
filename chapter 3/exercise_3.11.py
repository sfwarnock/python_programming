# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17

@author: 175272
"""

# Exercise 3.11
#   Write a program to find the sum of the first n natural numbers, where the value of n
#   is provided by the user.

def main():
    n = eval(input("Enter a number: "))
    
    s = (n * (n +1)) / 2
    
    print("The first sum of the first natural number you entered is",s)
    
main()