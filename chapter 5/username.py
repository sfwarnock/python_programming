# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 2018

@author: Scott Warnock
"""

# username.py
#
#   Simple string processing program to generate usernames.

def main():
    print("This program generates computer username.\n")
    
    #   get user's first and last names.
    f = input("Please enter your first name: ")
    l = input("Please enter your last name: ")
    
    #   concatenate first intial with 7 chars of the last name.
    uname = f[0].lower() + l[:7].lower()
    
    #   output the username.
    print("Your username is: ", uname)
    
main()