#Ops Challenge 07
#David Armstrong
#09-08-2020
#To list the full contents of a folder as a tree
import os
#Declaration of variables

path = input("Please enter a folder path: ")

#Declaration of functions
def walk (user_input):
    for (files) in os.walk(user_input):
        print(files)
#Main
walk(path)
#End