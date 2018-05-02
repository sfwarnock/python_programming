# -*- coding: utf-8 -*-
"""
Created on Wed May  2 2018

@author: Scott Warnock
"""

# exercise 5.9.py
#
#   Write a program that counts the number of words in a sentence entered by the user.

def main():
    sen = input("Enter a full sentence: ")
    
    for word in sen:
        word = sen.split()
    print ("The sentence you entered has", len(word), "words.")
main()