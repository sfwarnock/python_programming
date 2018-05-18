# -*- coding: utf-8 -*-
"""
Created on Fri May 18 2018

@author: Scott Warnock
"""

# exercise 7.4.py
#
#   A certain college classifies students according to credits earned. A student
#       with less than 7 credits is a Freshman.  At least 7 credits are required 
#       to be a Sophmore, 16 to be a Junior and 26 to be classified as a Senior.
#       Write a program that calculates class standing from the number of credits
#       earned.

def main():
    
    numOfCredits = eval(input("Enter the number of credits you have earned to-date: "))
    
    if numOfCredits < 7:
        print ("You are a Freshman.")
    elif numOfCredits < 16:
        print ("You are a Sophmore.")
    elif numOfCredits < 26:
        print ("You are a Junior.")
    else:
        print ("You are a Senior.")
        
main()