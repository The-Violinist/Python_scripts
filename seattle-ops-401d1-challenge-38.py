#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: Add description
# Date:        11-25-2020
# Modified by: David Armstrong

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

##This function takes an url and retrieves the contents of the page.
##It then parses the data into a normal html layout.
##Finally, it searches the contents of the html code for tags titled 'form'

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    ##Searches for tags titled "form"
    return soup.find_all("form")

##This function retrieves useful information regarding the type of form, the action, and the method. It returns a dictionary of field type with name values.
def get_form_details(form):
    ##Initialize the outermost dictionary
    details = {}
    ##Returns the type of field (e.g. login.php or login.jsp)
    action = form.attrs.get("action").lower()
    ##Tells what type of request (e.g. get, post)
    method = form.attrs.get("method", "get").lower()
    ##Initializing a list for the inputs
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        ##Add sub dictionaries to the inputs list.
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    ##the returned details is an embeded array (dictionary (list (dictionaries))) which includes the action, method and then type of field and the corresponding name value.
    return details

##Sends the form 
def submit_form(form_details, url, value):
    #Puts an url together using the base url and joining components of that with the action result from form_details.
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    ##Initializes a dictionary to store the field name and value pair.
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        ##Determine the names and values of the fields.
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value
    ##Determines if the method is post and if so, returns the status code
    if form_details["method"] == "post":
        ##Use the data dictionary as the data requirement
        return requests.post(target_url, data=data)
    else:
        ##Use the data dictionary as the params requirement
        return requests.get(target_url, params=data)

def scan_xss(url):
    ##forms = a list of all tags titled "form"
    forms = get_all_forms(url)
    ##Determines how many items there are in the list and prints the number of forms on the page.
    print(f"[+] Detected {len(forms)} forms on {url}.")
    ##html/JavaScript to inject
    ##I tried about 20 different things here and was never able to get the desired result. I'm just not sure at this point where the problem lies.
    ##I keep getting a Status 404 and I know this URL works.
    js_script = "<script>alert('hello')<.script>"
    ##Set the default to vulnerability being false
    is_vulnerable = False
    ##Loop through each occurence of a form tag and 
    for form in forms:
        ##For each form in the list, use that form as the target of the get_form_details function.
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        print(content)
        ##Test if the js_script text is present in 
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    #Return whether or not the page is vulnerable
    return is_vulnerable

# Main

#Takes user input of an URL in order to run tests against it to determine if there are XSS vulnerabilities.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:")
    print(scan_xss(url))
