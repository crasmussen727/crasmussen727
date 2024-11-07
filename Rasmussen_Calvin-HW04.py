# Open the input and output files
with open('prompt.txt', 'r') as input_file, open('out.txt', 'w') as output_file:
    # Loop through each line in the input file
    for line in input_file:
        # Split the line by tab to get the key-value pairs
        pairs = line.split(" ")
        
        # Initialize an empty string to store the result for this line
        result_line = ""
        
        # Process each key-value pair
        for pair in pairs:
            # Split the pair into key and value
            key, value = pair.split(":")
            value = int(value)  # Convert the value to an integer
            
            # Depending on the key, append the corresponding character repeated value times
            if key == 'w':
                result_line += " " * value  # Add 'value' number of white spaces
            elif key == '*':
                result_line += "*" * value  # Add 'value' number of asterisks
        
        # Write the constructed result to the output file
        output_file.write(result_line)