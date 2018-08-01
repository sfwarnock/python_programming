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
    #numDays = eval(input("How days of averges do you have to enter?"))
    
    avgTemp = eval(input("Enter days average temperature: "))
        
    coolDays, heatDays = 0, 0
    
    coolDaysAvg, heatDaysAvg = 0, 0
    
    if avgTemp >= 80:
        aboveHeating = avgTemp - 80
        coolDays = coolDays + 1
        coolDaysAvg = aboveHeating / coolDays
            
    elif avgTemp <= 60:
        belowCooling = 60 - avgTemp
        heatDays = heatDays + 1
        heatDaysAvg = belowCooling / heatDays
                        
    print('Total heating days are: ', heatDaysAvg)
    print('Total cooling days are: ', coolDaysAvg)
#   print the number of heating and cooling days

main()    