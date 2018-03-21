# File: chaos_1.3.py
# A simple program illustrating chaotic behavior from chapter 1 exercises 1.3,1.5,1.7.

print("THis progam illustrates a chotic function")
x = eval(input("Enter a number between 0 and 1: "))
y = eval(input("Enter another number between 0 and 1: "))
n = eval(input("How many numbers should the program print? "))
for i in range(n):
    x = 3.9 * x * (1-x)
    y = 3.9 * (x - x * x)
    print (x, y)