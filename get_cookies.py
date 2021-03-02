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
target = input("Please enter a website from which to retrieve cookies:\n>")
targetsite = f"http://www.{target}"
###FUNCTIONS###
def cookie_get():
    try:
        response = requests.get(targetsite)
        for item in response.cookies.items():
            cookie_list.append(item)
    except:
        pass

def send_cookie():
    resp = requests.get(targetsite, cookies=cookie_to_send)
    content = resp.text
    with open('request.html', 'w') as f:
        f.write(content)

def open_file():
    if (platform == "win32" or platform == "Windows"):
        os.system("start request.html")
    elif (platform == "linux" or platform == "Linux"):
        os.system("firefox request.html")

###MAIN###
cookie_get()
print(cookie_list)
try:
    main_page = cookie_list[0]
    #turn the list into a dictionary
    cookie_to_send = {'name' : main_page[0], 'cookies' : main_page[1]}
    send_cookie()
    open_file()
except:
    pass
###END###
