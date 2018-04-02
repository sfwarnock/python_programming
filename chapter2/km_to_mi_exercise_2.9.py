# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 15:24:48 2018

@author: Scott Warnock
"""

# kilometers to miles, exercise 2.9.

# This program converts user inputed kilometers to miles.

def main():
    km = eval(input("Type number of kilometers: "))
    mi = km / 1.609344

    print(km, "kilometers is equal to" ,mi, "miles.")

main()