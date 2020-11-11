#Ops Challenge 27
#David Armstrong
#11-10-2020
#Logging with rotation

import logging, subprocess
from logging.handlers import RotatingFileHandler

#Logger setup
logger = logging.getLogger('Rotating_Logger')
#Set the starting level to log
logger.setLevel(logging.INFO)
#Create the handler with values: logfile, maxbytes, and number of files to rotate (+ first file)
handler = RotatingFileHandler('ops27.log', maxBytes=50, backupCount=5)
#Apply the handler to the logger
logger.addHandler(handler)

###Variables###
inp = input("Please enter a system command:\n>")

###Main###
#Try the function and write logs
try:
	subprocess.run([inp], check = True)
	print("That worked")
	logger.info(f"{inp} worked")
except:
	print ('Command does not exist')
	logger.error(f"{inp} did not work")
###End###
