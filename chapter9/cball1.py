# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 2018

@author: Scott Warnock
"""

# cball1.py

from math import sin, cos, radians

def main():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between postions calculations: "))
    
    # convert angle to radians
    theta = radians(angle)
    
    # set the initial postion and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    
    # loop until the ball hits the ground
    while ypos >= 0.0:
        # calculate positon and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1
    
    print("\nDistance traveled: {0:0.1f} meters. ".format(xpos))

main()