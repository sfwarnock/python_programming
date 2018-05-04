# -*- coding: utf-8 -*-
"""
Created on Fri May  4 2018

@author: Scott Warnock
"""

# exercise 5.10.py
#
# Write a program that calcualtes the average word length in a sentence entered by the user.

def main():
    sen = input("Enter a full sentence: ")
    
    wordCoun = len(sen)
    
    for word in sen:
        word = sen.split(' ')
        senLen = len(word) 
    avg = wordCoun / senLen

    print("The average length of each word in the sentence you entered is", int(avg),"characters.")
main()