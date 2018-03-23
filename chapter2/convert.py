# convert.py
#   A program to convert Celsius temps to Fahrenheit
#
#   Pseudocode: Input the temperature in degrees Celsius (call it c)
# Calculate fahrenheit as (9/5) c + 32
# Output fahrenheit.

def main():
    c = eval(input("What is the Celsius temperature? "))
    f = 9/5 * c + 32
    print("The temperature is", f, "degrees fahrenheit.")

main()