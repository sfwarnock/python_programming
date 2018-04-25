# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 2018

@author: Scott Warnock
"""

# text2numbers.py
#
#   A program to convert a tectual message into a sequence of numbers,
#       untilizing the underlying Unicode encoding.

def main():
    print("This program converts a textual message into a sequence of numbers representing")
    print("the Unicode encoding of the message.\n")
    
    #   Get the message to encode.
    message = input("Please enter the message to encode: ")
    
    print("\nHere are the Unicodes:")
    
    #   Loop through the message and print out the Unicode values.
    for ch in message:
        print(ord(ch), end=" ")
    
    print () # blank line before prompt.
    
main()