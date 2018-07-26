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
    
    totalDays = eval(input('How many days of temperatures do you have?'))
    
    coolDays = 0
    
    heatDays = 0
    

    if avgTemp >= 80:
        aboveHeating = 80 - avgTemp
        coolDays = aboveHeating + coolDays
            
    elif avgTemp <= 60:
        belowCooling = 60 - avgTemp
        heatDays = belowCooling + heatDays
                        
    print('Total heating days are: ', heatDays, coolDays)
#   print the number of heating and cooling days

main()    