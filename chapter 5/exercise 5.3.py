# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 2018

@author: Scott Warnock
"""

# exercise 5.3
#
#   #   A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C,
#   60-69:D, <60:F.  Write a program that accepts an exam score as an input and prints out the 
#   correspondnig grade.

def main():
    # request score from user.
    score = eval(input("Enter your score on the exam: "))
    
    for index in range(score):
        if score >= 90:
            index = 4
        elif score >= 80:
            index = 3
        elif score >= 70:
            index = 2
        elif score >= 60:
            index = 1
        elif score <= 59:
            index = 0
            break
    
    grade = ['F', 'D', 'C', 'B', 'A']
    
    print("Your letter grade on the exam is:", grade[index])
    
main()