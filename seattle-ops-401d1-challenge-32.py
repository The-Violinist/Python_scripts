#Ops Challenge 32
#David Armstrong
#11-17-2020
#Analyze files in a directory (and all subdirectories) for hash and size

###LIBRARIES###
import os
import platform
import os.path
from os import path
import hashlib
import datetime

###VARIABLES###
#determine the operating system type. In this case it is not necessary but is used to create a hardcoded filepath
system = platform.system()

#A list of tuples which will hold all of the file data that is gathered
file_info = [("File Name","Time Recorded","Hash Value","File Size")]

###FUNCTIONS###
#Request a directory path from the user
def take_path():
    global dir_path
    while True:
        dir_path = input("Please enter a folder path: ")
        #To speed up testing, just press enter to select the whole C: drive
        if (dir_path == "" and system == "Windows"):
            dir_path = r"C:\Users\Violinist\Desktop\CSET"
        #To speed up testing, just press enter to select this user
        if (dir_path == "" and system == "Linux"):
            dir_path = "/home/osboxes/Desktop/Challenges"
        #Check to see if the input is a valid path and a directory
        is_path = (path.exists(dir_path))
        is_dir = (path.isdir(dir_path))
        if (is_path == False or is_dir == False):
            print("Please enter a valid directory path\n")
        elif (is_path == True and is_dir == True):
            #End loop and return the value of dir_path
            return dir_path

#Get the md5 hash of a file
def get_hash(target_file):
    with open(target_file, "rb") as file_to_check:
        try:
            # read contents of the file then pipe to hash creator
            contents = file_to_check.read()
            md5_returned = hashlib.md5(contents).hexdigest()
            return md5_returned
        except:
            pass

#Get the size of a file
def get_size(target_file):
    file_size = os.path.getsize(target_file)
    return file_size

#Analyze each file
def analyze_file():
    for (root, dirs, files) in os.walk(dir_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            contents_hash = get_hash(path)
            contents_size = get_size(path)
            time_now = datetime.datetime.now()
            file_info.append(tuple((name, str(time_now), contents_hash, f"{contents_size/1000000} MB")))

#Take the file information and make it readable
def print_table():
    for file_name,search_time,hash_contents,file_size in file_info:
        print("{:<35}{:<30}{:<37}{}".format(file_name,search_time,hash_contents,file_size))

###MAIN###
take_path()
analyze_file()
print_table()
###END###
