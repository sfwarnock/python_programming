# convert.py
#   A program to convert Celsius temps to Fahrenheit
#
#   Pseudocode: Input the temperature in degrees Celsius (call it c)
# Calculate fahrenheit as (9/5) c + 32
# Print a table of Celsius temps and Fehrenhrit equivalents every 10 degrees from 0C to 100C.

def main():
   c = -10
   for temp in range(11):
       c = c + 10
       f = 9/5 * c + 32
       print ("When it is",c,"degrees celsius, it is",f,"degrees fharenheit.")
       
main()