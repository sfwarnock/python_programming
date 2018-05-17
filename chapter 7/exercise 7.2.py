# -*- coding: utf-8 -*-
"""
Created on Thu May 17 2018

@author: Scott Warnock
"""

# exercise 7.2.py
#
#   A certain CS professor gives five-point quizzes that are graded on the scale
#       5-A, 4-B, 3-C, 2-D, 1-F, 0-F.  Write a program that accepts a quiz score
#       as an input and uses a decsion structre to calculate the corresponding grade.

def main():
    grade = eval(input("Please enter your grade: "))
    
    if grade == 5:
        print("You got an A on this assignment")
    elif grade == 4:
        print("You got a B on this assignment")
    elif grade == 3:
        print("You got a C on this assignment")
    elif grade == 2:
        print("You got n D on this assignment")
    elif grade == 1:
        print("You got a F on this assignment")
    else:
        print("You got a f on this assignment")

main()