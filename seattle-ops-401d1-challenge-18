# Ops Challenge 18
# David Armstrong
# 10/28/2020
# Unzip a password protected file using brute force

###LIBRARIES###
from zipfile import ZipFile

###VARIABLES###
#pwfile = input("Please enter the password list file:\n>")
pwfile = r"C:\Users\Violinist\Desktop\rockyou.txt"
open_file = open(pwfile, "r", errors='ignore')

###FUNCTIONS###
#Try each word in a file as the password for an SSH login
def pwd_list():
    #file = input("Please enter a file to unzip:\n>")
    file = "test.zip"
    #Read through each line of the file
    print("Testing passwords...")
    for i in open_file:
        #Divide the line into a list of words
        pword = i.split()
        length = (len(pword))
        x = 0
        #Set the break-in status to "no"
        break_in = "no"
        #Try each word as the password
        while (x < length):
            pwd = pword[x]
            #time.sleep(1)
            #print("Trying password", pwd)
            try:
                with ZipFile(file) as zf:
                    zf.extractall(pwd=bytes(pwd,'utf-8'))
                print(pwd, "was the correct password. Your file is now extracted.")
                break_in = "yes"
                break
            except:
                pass
            x += 1
        if (break_in == "yes"):
            break
    open_file.close()

###MAIN###
pwd_list()
###END###
