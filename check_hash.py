#Ops Challenge 33
#David Armstrong
#11-18-2020
#Analyze files in a directory (and all subdirectories) for hash and size, then check hashes against virustotal

###LIBRARIES###
import os, platform, hashlib, datetime
import os.path
from os import path
###VARIABLES###
#determine the operating system type. In this case, it is not necessary but helps with testing
system = platform.system()
#List of tuples which holds the file data
file_info = [("File Name","Time Recorded","Hash Value","File Size")]
hashes = []
###FUNCTIONS###
#Request a directory path from the user
def take_path():
    global dir_path
    while True:
        dir_path = input("Please enter a folder path: ")
        #To speed up testing, just press enter to select the whole C: drive
        if (dir_path == "" and system == "Windows"):
            dir_path = r"C:\Users\Violinist\Desktop\encrypt"
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
            contents_size = get_size(path)
            contents_hash = get_hash(path)
            hashes.append(contents_hash)
            time_now = datetime.datetime.now()
            file_info.append(tuple((name, str(time_now), contents_hash, f"{contents_size/1000000} MB")))

#Take the hash and test against the virustotal database
def test_hash(contents_hash):
    apikey = os.getenv('API_KEY_VIRUSTOTAL')
    #This is inside of the analize_file, so the hash value is created there
    hash = contents_hash
    # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
    query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash
    os.system(query)

#Take the file information and make it readable
def print_table():
    for file_name,search_time,hash_contents,file_size in file_info:
        print("{:<35.33}{:<30.30}{:<37.37}{}".format(file_name,search_time,hash_contents,file_size))

def count_detections():
    virus_count = 0
    file_count = 0
    for hash in hashes:
        tested_for_virus = test_hash(hash)
        if (tested_for_virus == f"{hash}: MALICIOUS"):
            print(f"{hash} contains a virus.")
            virus_count += 1
        file_count += 1
        print(f"{file_count} total files counted. There were {virus_count} files containing malware.")

###MAIN###
take_path()
analyze_file()
print_table()
count_detections()
###END###
