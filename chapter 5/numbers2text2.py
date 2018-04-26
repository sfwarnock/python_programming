# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 2018

@author: Scott Warnock
"""

# numbers2text2.py
#
#   A program to convert a sequence of Unicode numbers into a string of text.
#   Efficient version using a list accumulator.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that is represents.\n")
    
    # Get the message to encode.
    inString = input("Please enster the Unicode-encoded message: ")
    
    # Loop through each substring and build Unicode message.
    chars = []
    for numStr in inString.split():
        codeNum = eval(numStr)              # convert digits to a number.
        chars.append(chr(codeNum))    # accumulate new character
    
    message = " ".join(chars)
    print("\nThe decoded message is:", message)
    
main()