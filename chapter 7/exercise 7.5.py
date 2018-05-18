# -*- coding: utf-8 -*-
"""
Created on Fri May 18 2018

@author: Scott Warnock
"""

# exercise 7.5.py
#
#   The body mass index (BMI) is calculated as a persons weight (lbs) times 720,
#       divided by the square of the person's height (in inches).  A BMI in the range
#       19-25, inclusive, is considered healthy.  Write a program that calculates a
#       persons's BMI and prints a message telling whether they are above, within,
#       or below the healthy range.


def main():
    
    height = eval(input("Enter your height, in inches: "))
    
    weight = eval(input("Enter your weight, in pounds: "))
    
    bmi = (weight * 720) / height ** 2 ; print("Your BMI is: ", round(bmi,2))
    
    if bmi < 19:
        print ("Your BMI is under the healthy range.")
    elif bmi <= 25:
        print ("Your BMI is within the healthy range.")
    else:
        print ("Your BMI is above the healthy range.")
        
main()