# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2018

@author: Scott Warnock
"""

# exercise 7.8.py
#
# A person eligible to be a US senator if they are at least 30 years old and have been
#   a US citizen for at least 9 years.  To be a US represntative these numbers are 25
#   and 7, respectively.  Write a program that accepts a person's age and years of 
#   citizenship as input and outputs their elgibility for the Senate and House.

def main():
    age = eval(input("Enter your age: "))
    
    usCitizen = eval(input("How many years have you been a U.S. Citizen: "))
    
    if age >= 30 and usCitizen >= 9:
        print("You are elgiable to be either a US Senator or House Representative!")
    elif age >= 25 and usCitizen >=7:
        print("You are elgiable to be a House Representative!")
    else:
        print("You are not elgiable to be either a US Senator or House Representative!")
        
main()