'''

Welcome to 'Challenge Activity' 6.4.14.c01! This challenge
activity is going to test your comprehension on parsing
JSON data and interacting with the user. Here are the requirements 
for your JSON program for this Challenge Activity:

1. The program must run until the user decides to quit
2. Your list program needs to support the following user options:
    a. Provide a cryptocurrency price quote leveraging the LunarCrush API
    b. Provide directions leveraging the MapQuest API
    c. Provide an alphabetically sorted list (by first name) of all
       the astronauts currently in space using the ISS API
    d. Allow the user to quit

Once you have completed this activity you can 'Submit' your file and
view one possible solution set for the activity or you can 'Fork'
the solution set to have a copy with which you can work. If you look
at the image to the left, 6.4.14.c01-image you will see an 
example of what your menu could look like and how some of the 
functionality should work.

Good luck and here are some import statements to get you started!

'''
from requests import get
from urllib.parse import urlencode

print("")
message = 'Would you like to:\n1. Get a crypto quote\n2. Get directions using MapQuest\n3. Get a list of astronauts in space sorted alphabetically\n4. Quit\n\n'

def crypto():
  token = input('Please enter token symbol: ')
  cryptoURI = "https://api.lunarcrush.com/v2?data=assets&key={API_KEY_HERE}&symbol="+token.upper()
  json_data = get(cryptoURI).json()
  tokenSymbol = str(json_data["config"]["symbol"])
  currentPrice = str(json_data["data"][0]["price"])
  print("Price of ", tokenSymbol, "is ", currentPrice, end='\n\n')
  



keyMapQuest = 'NGMJMoREO5aShAzbLtLChdPpxGVbuLQd'
def maps():
  tripStartingLocation = input('Enter the starting address of your trip: ')
  tripEndingLocation = input('Enter the address of your ending location: ')
  uriMapQuest = 'http://www.mapquestapi.com/directions/v2/route?'
  uriEncoded = uriMapQuest + urlencode({"key": keyMapQuest, "from":tripStartingLocation, "to":tripEndingLocation})
  jsonData = get(uriEncoded).json()
#  print(jsonData)
  tripDistance = jsonData["route"]['distance']
  print("trip distance is ", tripDistance, end='\n\n')
  tripToll = jsonData["route"]['hasTollRoad']
  print("trip Toll is ", tripToll, end='\n\n')

  print("Step by step directions:", end='\n\n')
  for i in range(len(jsonData["route"]['legs'][0]['maneuvers'])):
    tripManeuvers = jsonData["route"]['legs'][0]['maneuvers'][i]['narrative']
    print(tripManeuvers)

  print()
  

while True:
  print(message)
  userChoice = int(input("What is your choice?"))
  if userChoice == 1:
#    print("TODO Crypto")
    crypto()
  elif userChoice == 2:
#    print("TODO Maps")
    maps()
  elif userChoice == 3:
#    print("TODO astronauts")
    responseObject = get("http://api.open-notify.org/astros.json")
    jsonData = responseObject.json()
#    print(jsonData)
    astronauts = []
    for astronaut in jsonData['people']:
      astronauts.append(astronaut['name'])
      astronauts.sort()
    print(astronauts)
  elif userChoice == 4:
    print("Quitting...")
    break
  else:
    print("Choose a valid number 1-4")
    break

print("Thank you for using my program!")
