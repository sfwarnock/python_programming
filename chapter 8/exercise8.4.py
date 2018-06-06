# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 2018

@author: Scott Warnock
"""

# exercise8.4.py
#
#   The Syracuse sequence is generated by starting with a natural number and repeatedly
#   applying the following function until reaching 1.
#
#       syr(x) = x/2    if x is even
#               3x + 1  if x is odd
#
#
#   For example, the Syracuse sequence starting with 5 is: 5, 16, 8, 4, 2, 1.  It is an
#   open question in mathematics whether this sequence will always go to 1 for every
#   possiable starting value.
#
#   Write a program that gets a starting value from the duser and the prints the Syracuse
#   for that starting value.

def main():
    