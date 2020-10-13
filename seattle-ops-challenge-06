# Ops Challenge 06
# David Armstrong
# 10-13-2020
# Taking user input and encrypting files or input messages

# Import Libraries
from cryptography.fernet import Fernet
import os

### DECLARE FUNCTIONS ###
#Create the key
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

#Encrypt a message
def enc_message():
    mess = input("Please enter a message to encrypt \n>>>")
    message = mess.encode()
    encrypted = f.encrypt(message)
    print("Here is the encrypted message: ")
    print(encrypted)

#Decrypt a message
def decr_message():
    f = Fernet(key)
    decrypting = input("Please enter a hash to decrypt \n>>>")
    #Change the data into bytes
    decrypts = bytes(decrypting, 'utf-8')
    unhash = f.decrypt(decrypts)
    unhashed = unhash.decode("utf-8")
    print("Here is the decrypted message: ")
    print(unhashed)

#Bring all functions together and request user input
def user_input():
    num = int(input("Please select from the following options: \n 1. Encrypt a file \n 2. Decrypt a file \n 3. Encrypt a message \n 4. Decrypt a message \n >>>"))
    if (num == 1):
        filename = input("Please enter a file to encrypt \n>>>")
        encrypt_file(filename, key)
    elif (num == 2):
        filename = input("Please enter a file to decrypt \n>>>")
        decrypt_file(filename, key)
    elif (num == 3):
        enc_message()
    elif (num == 4):
        decr_message()

### MAIN ###
# generate and write a new key if it doesn't exist
if os.path.exists("key.key"):
    print ("There is already an existing key.")
else:
    print("Creating the key.")
    write_key()

# load the previously generated key
key = load_key()

# initialize the Fernet class
f = Fernet(key)

#Run the program
user_input()
###END###
