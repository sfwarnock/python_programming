# -*- coding: utf-8 -*-
"""
Created on Tue May 29 2018

@author: Scott Warnock
"""

# average5.py

def main():
    fileName = input("What file are the numbers in?")
    inFile = open(fileName,'r')
    sum = 0.0
    count = 0
    for line in inFile:
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the numbers is", sum / count)

main()