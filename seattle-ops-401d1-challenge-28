#Ops Challenge 28
#David Armstrong
#11-11-2020
#Logging to 3 different locations

import logging, subprocess
from logging.handlers import RotatingFileHandler
from logging.handlers import SMTPHandler
import getpass

###Variables###
#inp = input("Please enter a system command:\n>")
#Invalid command which should throw error
inp = "asdf"
#Get password for email address
password = getpass.getpass(prompt='Please enter your password: ', stream=None)

#Logger setup
logger = logging.getLogger(__name__)
message = logging.getLogger("Console")
smlog = logging.getLogger("Email")
message.setLevel(logging.INFO)

#Create the handlers
file_handler = RotatingFileHandler('ops27.log', maxBytes=25, backupCount=2)
console_handler = logging.StreamHandler()
#Email
sm_handler = SMTPHandler(mailhost=('smtp.gmail.com', 587),
                fromaddr="email@address,
                toaddrs="email@address",
                subject="Program Error",
                credentials=(username, password),
                secure=())

#Set log levels
file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.INFO)
sm_handler.setLevel(logging.ERROR)

#Formatting
#Add the log type to each entry
#File
f_formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
file_handler.setFormatter(f_formatter)
#Console
c_formatter = logging.Formatter('%(levelname)s:%(message)s')
console_handler.setFormatter(c_formatter)
#Email
sm_formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
sm_handler.setFormatter(sm_formatter)

#Apply the handlers to the loggers
logger.addHandler(file_handler)
message.addHandler(console_handler)
smlog.addHandler(sm_handler)


###Main###
#Try the function and write logs
try:
    subprocess.run([inp], check = True)
    message.info(f"{inp} worked")
except:
    print ('Command does not exist')
    logger.error(f"{inp} did not work")
    smlog.error("There was a problem with your Python script!")

###End###
