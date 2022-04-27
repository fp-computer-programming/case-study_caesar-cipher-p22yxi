# Imports
from string import ascii_uppercase

# Main
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

# Functions
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))

with open(user_file, 'r') as file1:
    lines = file1.readlines()
    for x in lines:
        line = x


def shift_line(line, dict_key):
    new_line = " "
    for w in line:
        for (k, v) in dict_key.items():
            if k == w:
                new_line += w
        
    # Add code here
    return new_line


def encrypt_message(filename, dict_key):
    ofile = open(filename, "w")
    ofile.write(new_line + "\n")
    ofile.close()


    # Add code here




key = cipher_key(shift_value)

encrypt_message(user_file, key)