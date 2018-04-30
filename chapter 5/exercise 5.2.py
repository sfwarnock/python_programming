# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 2018

@author: Scott Warnock
"""

# exercise 5.2
#
#   A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C,
#   2-D, 1-F, 0-F.  Write a program that accepts a quiz score as an input and prints out the 
#   correspondnig grade.

def main():
    # request user score.
    score = eval(input("Enter your score on the quiz: "))
    
    grade = ['F', 'F', 'D', 'C', 'B', 'A']
    
    print("Your grade is a:", grade[score])
    
main()