# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 06:35:04 2018

@author: Scott Warnock
"""

# userfile.py
#
#
#   Progam to create a file of usernames in batch mode.

def main():
    print("This program creates a file of usernames from a file of names.")
    
    # get the file names.
    infileName = input("What files are the names in? ")
    outfileName = input("What file should the usernames go in? ")
    
    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    
    # process each line of the input file.
    for line in infile:
        # get the first and last names from line.
        first, last = line.split()
        # create the username
        uname = (first[0] + last[:7]).lower()
        # write it to the ouputfile
        print (uname, file=outfile)
        
    # close both files
    infile.close()
    outfile.close()
    
    print("Usernames have been written to", outfileName)
    
main()