# -*- coding: utf-8 -*-
"""
Created on Mon May 21 2018

@author: Scott Warnock
"""

# exercise 7.6.py
#
# The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over
#   the limit plus a penalty of $200 for any speed over 90 mph.  Write a program that
#   accepts a speed limit and clocked speed and either prints a message indicating the
#   speed was leagl or prints the amount of the fine, if the speed is illgeal.

def main():
    speedLimit = eval(input("Enter the speed limit: "))
    
    clockedSpeed = eval(input("Enter the clocked speed: "))
    
    if clockedSpeed < speedLimit:
        print("Car was not traveling over the speed limit.  No ticket required.")
        
    if clockedSpeed >= 90:
        overLimit = clockedSpeed - speedLimit
        ticket = (overLimit * 5) + 250
        print("$",ticket)  
    elif clockedSpeed > speedLimit:
        overLimit = clockedSpeed - speedLimit
        ticket = (overLimit * 5) + 50
        print("$",ticket)
        
main()