# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:07:51 2018

@author: Scott Warnock
"""

# average2.py

def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    
    while moredata[0] == "y":
        x = eval(input("Enter a number: "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", sum / count)
    
main()