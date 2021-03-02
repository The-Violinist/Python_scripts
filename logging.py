#Ops Challenge 26
#David Armstrong
#11-09-2020
#First use of logging
# https://dotnettutorials.net/lesson/logging-module-in-python/

import logging
import subprocess

logging.basicConfig(filename='challenge06.txt',level=logging.INFO)
###Variables###

#Variable to use for the subprocess
inp = "ls"

###Main###
#Call the function

try:
	subprocess.run([inp], check = True)
	print("That worked")
	logging.info(f"{inp} worked")
except:
	print ('Command does not exist')
	logging.error(f"{inp} did not work")
###End###
