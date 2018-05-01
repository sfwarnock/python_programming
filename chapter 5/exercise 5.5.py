# -*- coding: utf-8 -*-
"""
Created on Tue May  1 2018

@author: Scott Warnock
"""

# exersice 5.5.py
#
#   Numerologists claim to be able to determine a person's character traits based of the 
#       "numeric value" of a name.  The value of a name is determined by summing up the values
#       of the letter of a name where "a" is 1, "b" is 2, "c" is 3 etc. up to "z" being 26. For
#       for example Zelle would have the value 26+5+12+12+5 = 60 (which happens to be a very auspicious number).
#       Wrtie a program that calculates the numeric value of a single name provided as input.

def main():
    name = input("Eneter your name: ").lower()
        
    letterVal = 0
    
    for ch in name:
        letterVal = ord(ch) + letterVal - 96
        
    print(letterVal)
 
main()