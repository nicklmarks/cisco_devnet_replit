##
## Welcome to 'Challenge Activity' 2.6.1.12.c01!
## To complete the Challenge Activity, take a look 
## at the image to the left (under main.py) and see if
## you can reproduce the output exactly. 
## However, for this activity, there are some constraints:
##
## 1. You must use the URIs provided in the comments below
##    and there are no errors in the URI itself.
##
## Once you have completed this activity,
## you can 'Submit' your file and view a possible
## olution set for the activity or you can 'Fork'
## the solution set to have a copy with which to work.
## Good luck!
##
## The URI below has NO errors and is correct and is the 
## only URI you will need for this activity:
##
issURI = "http://api.open-notify.org/iss-now.json"

## Place your code below this line...
import requests

httpResponse = requests.get(issURI)
jsonData = httpResponse.json()
print("Welcome to my International Space Station (ISS) Locator!")
print()
print("Here is the JSON data for where the ISS is currently located:")
print(jsonData)