# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 2018

@author: Scott Warnock
"""

# exercise8.11.py

# Heating and cooling degree-days are measures used by utility companies to estimate
#   energy requirements. If the avergae temperature for a day is below 60, then the 
#   number of degrees below 60 is added to the heating degree-days. If the temperature
#   is above 80, the amount over 80 is added to the cooling days. Write a program that 
#   accepts a sequence of the average daily temps and computes the running total of cooling
#   heating degree-days. The program should print these two totals after all the data has been processed.

def main():
    
#   ask how many days of averges to enter
    numDays = eval(input("How days of averges do you have to enter?"))
    
    avgTemp = eval(input("Enter days average temperature: "))
    
    coolDays = y
    
    heatDays = x
    
    for avgTemp in range(numDays):
    #   compute cooling and heating day totals
        if avgTemp >= 80:
            coolDays = 80 - avgTemp
            
        elif avgTemp <= 60:
            heatDays = 60 - avgTemp
            
        else:
            

#   print the number of heating and cooling days

main()    