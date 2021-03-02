# Ops Challenge 13
# David Armstrong
# 10/21/2020
# ARP a network and check the existing hosts for open ports

###LIBRARIES###
from scapy.all import ARP, Ether, srp, sr1, IP, TCP
import random
from alive_progress import alive_bar
from time import sleep

###VARIABLES###
# IP Address for the destination
#target_ip = "192.168.1.0/24"
target_ip = input("Please enter a network address to scan:\n>")

# Empty list to be populated with clients
clients = []


###FUNCTIONS###
def port_stat():
    # Define target host
    #host = input("Please enter an IP or web address:\n>")
    host = client
    open_closed = 0
    # Ports to scan
    dport_range = [20, 21, 22, 53, 80, 443]
    print("Checking", host, "for open ports:")
    for dst_port in dport_range:
        # Randomized source port
        src_port = random.randint(5000, 65000)
        #print("Sending request to port", dst_port, "@", host, "from port", src_port)
        # Sends a SYN request and receives a flag from the target
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
        # Determine if there is a response
        try:
            #Check to see if there is a TCP response
            if (response.haslayer(TCP)):
                flag = (response.getlayer(TCP).flags)
                # If flags were SYN and ACK
                if (flag == "SA"):
                    sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="F"),timeout=1,verbose=0)
                    print("Port", dst_port, "is open.")
                    open_closed += 1
        except:
            continue
    if (open_closed == 0):
        print("No open ports.")
###MAIN###
# create ARP packet
print("Compiling list of hosts...")
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]

#Create list of up hosts with a progress bar
with alive_bar(len(result)) as bar:
    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        clients.append(received.psrc)
        #optional: create a dictionary# clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        sleep(0.05)
        bar()

for client in clients:
    port_stat()
###END###
