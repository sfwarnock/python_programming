# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 06:41:30 2018

@author: Scott Warnock
"""

# printfile.py
#
#   Prints a file to the screen.

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print (data)
    
main()