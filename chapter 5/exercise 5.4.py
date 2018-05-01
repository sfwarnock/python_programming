# -*- coding: utf-8 -*-
"""
Created on Tue May  1 2018

@author: Scott Warnock
"""

# exersice 5.4
#
#   An acronym is a word formed by taking the first letters of the words in a phrase and making
#       a word from them.  For example, RAM is an acronym for "random access memory".  Write a progam
#       that allows the user to type in a phrase and then outputs the acronym for that phrase.  Note:
#       the acronym should be all uppercase, even if the words in the phrase are not capitalized.

def main():
    # enter phrase
    inPhrase = input("Enter the phrase you would like to turn into an acronym: ")
    
    letter = []
    for word in inPhrase.split(' '):
        first = word[0].upper()
        letter.append(first)
        
    acronym = "".join(letter)
    print("\nThe acronym is:", acronym)
        
main()