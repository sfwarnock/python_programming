# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19

@author: Scott Warnock
"""

# Exercise 3.14
#
#   Write a program that finds the average of a series of numbers entered by the user.
#   First prompt the user for how many numbers are to be entered..

print("This program averages numbers entered by the user.")
print()

def main():
    tn = eval(input("How many numbers do you want to average? "))
    sum = 0
    for n in range(tn):
        n = eval(input("Enter a number: "))
        sum = sum + n
        mean = sum / tn
    print()    
    print ("The mean of the numbers you entered is", mean)
main()