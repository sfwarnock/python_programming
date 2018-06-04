# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 2018

@author: Scott Warnock
"""

# exercise 8.2.py
#
#   The National Weather Service computes the windchill index using the following formula:
#       
#       35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(v^0.16)
#
#   Where T is the temperature in degrees Fahrenheit , and V is the wind speed in mph.
#
#   Write a program the prints a nicely formatted table of windchill values.  Row should
#   represent wind speed for 0 to 50 in 5 mph increments, and the columns represent temp.
#   from -20 to +60 in 10 degree increments.  Note: the formula only applies for wind
#   speeds in excess of 3 mile per hour.

def main():
    temp = -20
    windSpeed = 0 
    windChill = 35.74 + (.6251 * temp) - 35.75 * (windSpeed ** .16) + .4275 * (windSpeed ** .16)

    for temp in range(temp + 5):
        if windSpeed <= 3:
            windChill = 35.74 + (.6251 * temp) - 35.75 * (0 ** .16) + .4275 * (0 ** .16)
        print(temp, windSpeed,windChill)
        else:
            windChill = 35.74 + (.6251 * temp) - 35.75 * (windSpeed ** .16) + .4275 * (windSpeed ** .16)
            windSpeed += 5
    print(temp, windSpeed,windChill)
main()