# Ops Challenge 36
# David Armstrong
# 11-23-2020
# Performs banner grabbing

###LIBRARIES###
import time
import socket
from telnetlib import Telnet
import nmap
###VARIABLES###
host = "192.168.1.21"
#host = input('Please enter an IP address:\n>')
port = 22
#port = input('Please enter a port number:\n>')

###FUNCTIONS###
def telnet_grab(host, port):
    with Telnet(host, port) as tn:
        #Grab the banner and convert from bytes
        socket = (tn.read_some()).decode('utf-8')
        print("Banner grab with Telnet:")
        print(socket)
        tn.close()

def netcat_grab(host, port):
    #Define a socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
    #Connect to the socket
    sock.connect((host, port))
    ret = (sock.recv(1024)).decode('utf-8')
    print("Banner grab with Netcat:")
    print(ret)
    sock.close()

def nmap_grab(host):
    nm = nmap.PortScanner()
    nm.scan(host, '20-8080')
    print(f"Port information for {host}")
    for protocol in nm[host].all_protocols():
        found_port = nm[host][protocol].keys()
        for port in found_port:
            print ('port : %s\tstate : %s' % (port, nm[host][protocol][port]['state']))

###MAIN###
telnet_grab(host, port)
time.sleep(2)
netcat_grab(host, port)
time.sleep(2)
nmap_grab(host)
###END###
