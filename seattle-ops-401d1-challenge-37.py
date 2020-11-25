#!/usr/bin/env python3

#Ops Challenge 37
#David Armstrong
#11-24-2020
#Get cookies from a website and send them back

###LIBRARIES###
import requests, os, sys

###VARIABLES###
cookie_list = []
platform = sys.platform

###FUNCTIONS###
def cookie_get():
    targetsite = "http://www.kleinmannstrings.com/"
    #targetsite = input("Please enter a website from which to retrieve cookies:\n>")
    response = requests.get(targetsite)
    for item in response.cookies.items():
        cookie_list.append(item)

def send_cookie():
    url = "http://www.kleinmannstrings.com/"
    resp = requests.get(url, cookies=cookie_to_send)
    content = resp.text
    with open('request.html', 'w') as f:
        f.write(content)

###MAIN###
cookie_get()
#turn the list into a dictionary
main_page = cookie_list[0]
cookie_to_send = dict(name=main_page[0], cookies=main_page[1])
#use the dictionary to fill the required cookies field in the get request
send_cookie()

if (platform == "win32" or platform == "Windows"):
    os.system("start request.html")
elif (platform == "linux" or platform == "Linux"):
    os.system("firefox request.html")
###END###
