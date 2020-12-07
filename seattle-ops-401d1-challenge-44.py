# Ops Challenge 44
# David Armstrong
#12-07-2020
# Checks to see if a port is open

###LIBRARIES###
import socket
###VARIABLES###
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10
sockmod.settimeout(timeout)
#I have hardcoded all but the last octet for ease of testing
host_inp = input('Please enter an IP address:\n>')
hostip = f"192.168.1.{host_inp}"
#hostip = input("Please enter an IP address")
port_in = input("Please enter a port to scan:\n>")
portno = int(port_in)

###FUNCTIONS###
def portScanner(hostip, portno):
    result = sockmod.connect_ex((hostip, portno)) # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
    if (result == 0):
        print("Port open")
    else:
        print("Port closed")
###MAIN###
portScanner(hostip, portno)
###END###
