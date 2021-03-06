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
    
    numberOfDays = eval(input("How many days of tempratures do you want to enter: "))
   
    coolDegreeDays, heatDegreeDays = 0, 0
    
    allTemps = []
    
    for avgTemp in range(numberOfDays):
        avgTemp = eval(input("Enter days average temperature: "))
        allTemps.append(avgTemp)
        
    print(allTemps)
    
    for temps in allTemps:
        if avgTemp >= 80:
            coolDegreeDays = avgTemp - 80         
        elif avgTemp <= 60:
            heatDegreeDays = 60 - avgTemp
                        
    print('Total heating days are: ', heatDegreeDays)
    print('Total cooling days are: ', coolDegreeDays)

main()