# Ops Challenge 07
# David Armstrong
# 10-14-2020
# Taking user input and encrypting folders recursively

# Import Libraries
from cryptography.fernet import Fernet
import os

### FUNCTIONS ###
#Create Key
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#Initialize the key
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

#Traverse directory tree and encrypt all files
def file_walk_en():
    for (root, dirs, files) in os.walk(start_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            print("Accessing", name)
            encrypt_file(path, key)

#Traverse directory tree and decrypt all files
def file_walk_de():
    for (root, dirs, files) in os.walk(start_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            print("Accessing", name)
            decrypt_file(path, key)

#Ask whether to encrypt or decrypt
def encr_decr():
    en_de = input("Would you like to encrypt or decrypt the folder?\nPlease enter:\n1. To encrypt\n2. To decrypt\n>")
    if (en_de == "1"):
        file_walk_en()
    else:
        file_walk_de()

#Decrypt a file
def decrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write over the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("The file has now been decrypted.")

#Encrypt a file
def encrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypting_data = f.encrypt(file_data)
    #Write over the existing file
    with open(filename, "wb") as file:
        file.write(encrypting_data)
    print("The file has now been encrypted.")

### MAIN ###
#Check to see if the key already exists; create if not
if os.path.exists("key.key"):
    print ("There is already an existing key.")
else:
    print("Creating the key.")
    write_key()

# load the previously generated key
key = load_key()

# initialize the Fernet class
f = Fernet(key)

#Set listing start location
start_path = input("Please enter a folder to encrypt (full path): \n >>>")
#Run the main function to encrypt or decrypt a directory recursively
encr_decr()
### END ###
