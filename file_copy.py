import os, shutil
start_path = "O:\\MSP Docs\\"
# start_path = "C:\\Users\\darmstrong\\Downloads\\"
destination = "C:\\test\\"
if not os.path.exists("C:\\test\\"):
    os.makedirs("C:\\test\\")
def file_walk():
    for (root, dirs, files) in os.walk(start_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            if name[-5:] == ".docx":
                try:
                    shutil.copyfile(path, destination+name)
                except PermissionError:
                    print("Permission denied.")
                except shutil.SameFileError:
                    print("Source and destination represents the same file.")

file_walk()