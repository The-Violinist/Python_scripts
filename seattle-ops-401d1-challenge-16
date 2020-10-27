# Ops Challenge 16
# David Armstrong
# 10/26/2020
# Checking a password against a dictionary

###LIBRARIES###
import time
import re

###VARIABLES###
#pwfile = input("Please enter the password list file:\n>")
pwfile = "test.txt"
open_file = open(pwfile, "r")

###FUNCTIONS###
#Read through a file containing passwords, assign them to a variable and print to the screen
def pwd_list():
    for i in open_file:
        #Read each line and divide the line into a list of words
        pword = i.split()
        length = (len(pword))
        x = 0
        #Iterate through the length of the list and print each word to the screen
        while (x < length):
            #variable for assigning each password before printing
            word = pword[x]
            print(word)
            x += 1
            time.sleep(.2)
    open_file.close()

#Same as above, but this will take user input to see if their password is in the list
def chk_pwd():
    for i in open_file:
        pword = i.split()
        length = (len(pword))
        x = 0
        while (x < length):
            #variable for assigning each password before printing
            word = pword[x]
            #Check to see if there is a match with the user input
            if (pwd_to_check == word):
                print("Your password,", pwd_to_check, ", is on the list")
                break
            x += 1
        #Stop iterating if the password has a match in the file
        if (pwd_to_check == word):
            break
    open_file.close()

#Check to see if a user password fulfills criteria
def check_strength():
    while True:
        global pwd_to_check
        pwd_to_check = input("Please enter a password to check:\n>")
        #Has a lowercase letter
        lower = re.search("[a-z]", pwd_to_check)
        #Has an uppercase letter
        upper = re.search("[A-Z]", pwd_to_check)
        #Has a digit
        digit = re.search("[\d]", pwd_to_check)
        #Has a symbol
        symbol = re.search("[^a-zA-Z\d\s:]", pwd_to_check)
        if (lower == None):
            print("Password must include a lowercase letter.")
            continue
        if (upper == None):
            print("Password must include an uppercase letter.")
            continue
        if (digit == None):
            print("Password must include a digit.")
            continue
        if (symbol == None):
            print("Password must include a symbol.")
            continue
        print("Your password includes all required components!")
        break

#Ask user which mode
mode = int(input("Please enter which mode you would like to use:\n 1) List passwords in file\n 2) Check a password against the file:\n 3) Check password strength:\n>"))
#Read list
if (mode == 1):
    pwd_list()
#Check list for password
elif (mode == 2):
    pwd_to_check = input("Please enter a password to check:\n>")
    chk_pwd()
#Check for strong password
elif (mode == 3):
    check_strength()
