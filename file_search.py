#Ops Challenge 31
#David Armstrong
#11-16-2020
#Search for a file

###LIBRARIES###
import os
import platform
import os.path
from os import path

###VARIABLES###
#determine the operating system type. In this case, it is not necessary
system = platform.system()

#Take user intput for a file
user_input = input("Please enter a file to search for:\n>>>")

###FUNCTIONS###
#Request a directory path from the user
def take_path():
    global dir_path
    while True:
        dir_path = input("Please enter a folder path: ")
        #To speed up testing, just press enter to select the whole C: drive
        if (dir_path == "" and system == "Windows"):
            dir_path = "C:\\"
        #To speed up testing, just press enter to select this user
        if (dir_path == "" and system == "Linux"):
            dir_path = "/home/osboxes"
        #Check to see if the input is a valid path and a directory
        is_path = (path.exists(dir_path))
        is_dir = (path.isdir(dir_path))
        if (is_path == False or is_dir == False):
            print("Please enter a valid directory path\n")
        elif (is_path == True and is_dir == True):
            #End loop and return the value of dir_path
            return dir_path

def find_file():
    #Total files counter
    global files_searched
    files_searched = 0
    #Total files found counter
    global files_found
    files_found = 0
    for (root, dirs, files) in os.walk(dir_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            files_searched += 1
            if (name == user_input):
                print(f"{name} is present.\nIt is in the following location: {root}")
                files_found += 1
###MAIN###
take_path()
find_file()
print(f"Files searched = {files_searched}")
print(f"Files found = {files_found}")
###END###
