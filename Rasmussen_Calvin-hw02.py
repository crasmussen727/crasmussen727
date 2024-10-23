# Calvin Rasmussen
# UWYO COSC 1010
# Submission Date: 11/01/24
# HW 02
# Lab Section: 12
# Sources, people worked with, help given to: 
# your
# comments
# here
# I started by defining the morse dictionary with its keys being the letters and the morse being the values 
morse_dict= {'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',   
        'F': '..-.', 'G': '--.',  'H': '....',  'I': '..',   'J': '.---', 
        'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',  
        'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',    
        'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--', 
        'Z': '--..'
    }

input_string= input("Enter your statement: ") #this allows for us to input our statement

morse_output=[] #this is our list for our output

for char in input_string: #for each character in the input, this will run
    if char.isalpha(): #if the character is in the alphabet it will go through here
        morse_char= morse_dict[char.upper()] #this will convert the letters to uppercase to make sure it works and transfers it to morse 
        morse_output.append(morse_char) #it will add the new character 
    elif char ==' ': #if it is a space then it will go through here
        morse_output.append(' ')#this adds the space in the morse_output

final_morse=' '.join(morse_output).replace(' ','  ') #this replaces the empty strings for double spaces
    
print(final_morse)#this prints the morse