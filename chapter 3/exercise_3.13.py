# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19

@author: Scott Warnock
"""

# Exercise 3.13
#
#   Write a program to sum a series of numbers entered by the user.  The program should
#   first prompt the user for how many numbers are to be summed.  It should then input each
#   of the numbers and print a total sum.

print("This program sums numbers entered by a user")
print()

def main():
    tn = eval(input("How many numbers do you want to sum? "))
    sum = 0
    for n in range(tn):
        n = eval(input("Enter a number: "))
        sum = sum + n
    print()    
    print ("The total sum of the numbers you entered is", sum)
main()