#!/usr/loca/bin/python3
# Import sleep method from time module (for delay)
from time import sleep

FILE = "/home/file.txt"  # Set the file path (that will be on the conatiner)

num = 1  # Set number variable to 1
while True:  # Keep running until killed
    with open(FILE, 'a') as myfile:  # Open file in "append" mode
        line = "Line number " + str(num) + "\n"  # Create a line (not crutial)
        myfile.write(line)  # Write the line to the file
    num += 1  # Increment num by 1
    sleep(2)  # Sleep for 2 seconds
