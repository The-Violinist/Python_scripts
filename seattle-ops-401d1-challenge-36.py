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
#host = "192.168.1.21"
#host = "http://scanme.nmap.org/"
host = input('Please enter an IP address:\n>')
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
    nm.scan(host, '20-443')
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            #print('----------')
            #print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            #lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))



###MAIN###
print("Trying telnet:\n")
try:
    telnet_grab(host, port)
except:
    print("Sorry, there was a network error.")
    pass
time.sleep(2)

print("Trying netcat:\n")
try:
    netcat_grab(host, port)
except:
    print("Sorry, there was a network error.")
    pass
time.sleep(2)

print("Trying nmap:\n")
try:
    nmap_grab(host)
except:
    print("Sorry, there was a network error.")
    pass
###END###
