#!/usr/bin/env python3

#Challenge: Uptime Sensor
#David Armstrong
#10-06-2020
#Detecting active IP using ping and creating a log

#Libraries
import os
import subprocess
import time
import datetime

#Variables
#Target address
addr = "8.8.8.8"

def ping():
    timenow = datetime.datetime.now()
    with open(os.devnull, 'w') as dnull:
        try:
            subprocess.check_call(
                ['ping', '-n', '1', '-w', '100', addr],
                stdout=dnull,  # suppress output
                stderr=dnull,
                )
            upordown = "Success!"
        except subprocess.CalledProcessError:
            upordown = "Failure!"
        #print(upordown)
        if upordown == "Success!":
            status = ("Network Active to " + addr)
        else:
            status = ("Network Inactive to " + addr)
    print(upordown, timenow, status)

while True:
    ping()
    time.sleep(2)
