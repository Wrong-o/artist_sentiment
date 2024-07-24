import sys

# Retrieve the variable passed from the main script
variable_from_main = sys.argv[1]

print(f"Received variable: {variable_from_main}")

#This file contains instructions specific for the text

#The letter "o" seem to be a substitute for the word "och", therefore:
#Changed " o " -> " och " 

user_input = input("Test för hov1_changes")
print(user_input)

processed_text = ['och' if token == 'o' else token for token in variable_from_main]

return[processed_text]