# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 06:05:12 2018

@author: Scott Warnock
"""

# Exercise 3.5
#   A coffee shop sells coffee at $10.50 a pound plus the cost of shipping.  Each order ships
#   for $0.86 per pound + $1.50 fixed cost for overhead.  Write a program that calculates the
#   cost of an order.

def main():
    fc, sc, cpp = 1.50, .86, 10.50  # fc = fixed cost, sc = shipping cost, cpp = cost per pound (of coffee)
    oq = eval(input("Enter the number of pounds of coffee you would like: "))   # oq = order quantity
    tc = fc + (sc * oq) + (cpp * oq)
    print()
    print("The total cost of your order is: $",tc)
     
main()