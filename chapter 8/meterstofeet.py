# -*- coding: utf-8 -*-
"""
Created on Thu May 31 2018

@author: Scott Warnock
"""

# meterestofeet.py
#

def main():
    meter = eval(input("Enter the elevation in meters: "))
    
    feet = meter * 3.28084
    
    print(meter, "meters is", round(feet,0),"feet.")

main()