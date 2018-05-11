# -*- coding: utf-8 -*-
"""
Created on Fri May 11 06:31:40 2018

@author: Scott Warnock
"""

# quadratic6.py

import math

def main():
    print("This program finds the real solution to a quadratic.\n")
    
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / 2 * 4
        root2 = (-b - discRoot) / 2 * 4
        print("\nThe solutions are: ", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nNo real roots.")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("\nYou didn't enter there numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input was not the correct form.  Missing comma?")
    except:
        print("Something went wrong, please debug your code.")
main()