# Calvin Rasmussen
# UWYO COSC 1010
# Submission Date: 11/15/2024
# HW 04
# Lab Section:12
# Sources, people worked with, help given to: notes from class, lots of practice and patence
# Open the input and output files
with open('prompt.txt', 'r') as input_file, open('out.txt', 'w') as output_file:
    for line in input_file:
        pairs = line.split("\t") # I need to split the line by tab
        pairs = line.split(" ")  #also need to split the pairs by space
        result_line = "" # start an empty string to store the result for this line
        for pair in pairs: # this will process each key-value pair in the line
            key, value = pair.split(":")  # this will split the pair into key and value
            value = int(value)  # this will convert the value to an integer
            
            if key == 'w':
                result_line += " " * value  # Add 'value' number of white spaces
            elif key == '*':
                result_line += "*" * value  # Add 'value' number of asterisks
        
        output_file.write(result_line + '\n') # put all of this into the output file
