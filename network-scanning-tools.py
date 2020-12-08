# Ops Challenge 45
# David Armstrong
#12-08-2020
# Suite of scanning functions

# I hardcoded the network portion of the address for ease of testing

###lIBRARIES###
import socket
import nmap

###FUNCTIONS###
def banner_grab():
    host_inp = input('Please enter an IP address:\n>')
    hostip = f"192.168.1.{host_inp}"
    #hostip = input("Please enter an IP address")
    port_in = input("Please enter a port to scan:\n>")
    portno = int(port_in)
    timeout = 3
    #Initialize a socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        #Connect to the socket
        print("Attempting a banner grab...")
        sock.connect((hostip, portno))
        ret = (sock.recv(1024)).decode('utf-8')
        print("Got it!")
        print(ret)
        sock.close()
    except:
        print("This port is not open")
        pass

def portScanner():
    sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = 3
    sockmod.settimeout(timeout)
    #I have hardcoded all but the last octet for ease of testing
    host_inp = input('Please enter an IP address:\n>')
    hostip = f"192.168.1.{host_inp}"
    #hostip = input("Please enter an IP address")
    port_in = input("Please enter a port to scan:\n>")
    portno = int(port_in)
    result = sockmod.connect_ex((hostip, portno))
    if (result == 0):
        print("Port open")
    else:
        print("Port closed")

def nmap_scan():
    host_inp = input('Please enter an IP address:\n>')
    hostip = f"192.168.1.{host_inp}"
    ports = input("Please enter a port or port range")
    nm = nmap.PortScanner()
    nm.scan(hostip, ports)
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


def select_scan():
    while True:
        scan_type = input("Please select a scanning tool:\na) Banner grab\nb) Port Scanner\nc) NMAP Scanner\n>>>")
        try:
            if (scan_type == 'a'):
                banner_grab()
                break
            elif (scan_type == 'b'):
                portScanner()
                break
            elif (scan_type == 'c'):
                nmap_scan()
                break
            else:
                print("Please enter a valid option")
        except:
            pass
###MAIN###
#banner_grab(hostip, portno)
select_scan()
###END###
