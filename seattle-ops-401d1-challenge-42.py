#Original script from pythonpool.com
#Edited by David Armstrong
#12-3-2020
#Using the nmap library to scan targets

import nmap
import re


###VARIABLES###
scanner = nmap.PortScanner()
ip_addr = input("Please enter an IP address: ")
range = input("Please enter a range of ports to scan: ")

###FUNCTIONS###
def scan_type():
    resp = input("""\nPlease enter the type of scan you want to run
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Comprehensive Scan
                    4) Regular Scan
                    5) OS Detection
                    6) Ping Scan entire network\n""")
    return resp

def syn_ack(ip_addr):
    print("Performing scan")
    scanner.scan(ip_addr,range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("Protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def udp(ip_addr):
    print("Performing scan")
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

def comprehensive(ip_addr):
    print("Performing scan")
    scanner.scan(ip_addr, range, '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def reg_scan(ip_addr):
    print("Performing scan")
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def os_system(ip_addr):
    print(scanner.scan(ip_addr, arguments="-O")['scan'][ip_addr]['osmatch'][0])

def ping_scan(ip_addr):
    #strip off the last part of the ip address
    compiler = re.compile(r'\d+.\d+.\d+.')
    found = compiler.match(ip_addr)
    #add on the network ending
    network = f"{found[0]}0/24"
    print(network)
    scanner.scan(hosts=network, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))

#Run the selected scan
def run_scan(response):
    if (response == '1'):
        syn_ack(ip_addr)
    elif (response == '2'):
        udp(ip_addr)
    elif (response == '3'):
        comprehensive(ip_addr)
    elif (response == '4'):
        reg_scan(ip_addr)
    elif (response == '5'):
        os_system(ip_addr)
    elif (response == '6'):
        ping_scan(ip_addr)
    else:
        print("Please choose a number from the list")

###MAIN###
#Loop until the user does not want to scan any more
while True:
    scan = input("Would you like to run a scan? ")
    if (scan == 'y' or scan == 'yes'):
        response = scan_type()
        run_scan(response)
    else:
        break
###END###
