# Yongdong XI (2022/4/28)
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

key = cipher_key(shift_value)

def shift_line(line, dict_key):
    new_line = ""
    for x in line:
        if x.isupper() == True:
            new_line += dict_key[x.upper()]
        else:
            new_line += dict_key[x.upper()].lower()

    return new_line


def encrypt_message(filename, dict_key):
    with open(filename,"r") as file1:
        old_file = file1
    new_file = open("new_file.txt","a")

    while True:
        old_line = old_file.readline()
        new_line = shift_line(old_line, dict_key)
        new_file.write(new_line + "\n")
        if len(old_line) == 0:
            break
    
    old_file.close()
    new_file.close()


encrypt_message(user_file, key)