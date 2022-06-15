'''

Welcome to the Course Checkpoint Challenge Activity!
In this activity you will be starting from scratch
and putting together a program that incorporates
a large number of the concepts we have learned to this
point in the course! Here are the requirements
for your challenge activity:

1. The program should run until the user indicates
   that they want to quit
2. The program should offer a menu of services to
   include the following:
     a. Add the names of all astronauts currently in
        space to a list and print that list out
        for the user whenever they ask.
     b. Create a second file named calc.py (from the
        menu to the left) and place four (4) functions
        in that file. Each function will perform
        a specific mathematical operation: add, 
        subtract, multiply, and divide two numbers. 
        Your main program file (this file)
        should import each of those functions
        individually for use. Your menu should offer
        the user a choice to perform any of those
        operations. When any of these functions is 
        called it should print out the docstring
        for the function to aid the user as well as
        the answer for the equation.
     c. Create a function in this file that will 
        print out the turn-by-turn directions between
        two locations, the total miles, and whether
        or not there are tolls on the trip. 
        MapQuest key has been provided
        below in the main body of the program or you
        can use your own.
     d. Create a menu option that provides the user
        with a quote on the cryptocurrency of their
        choice and stores the symbol/price as a key:value
        pair in a dictionary. This dictionary should
        be updated each time a quote is requested and
        after each quote request all key:value pairs
        in the dictionary should be printed out.
     e. Quit the program.

Good luck!!!

'''
# Feel free to use your key or the key that is below. There
# is no error in the key.
import requests
from calc import add, subtract, multiply, divide
from urllib.parse import urlencode


def astronauts(): 
  responseObject = requests.get("http://api.open-notify.org/astros.json")
  jsonData = responseObject.json()
  numAstronauts = (jsonData['number'])
  list_space = []
#  print(jsonData)
#  print(jsonData['people'][0]['name'])
  for i in range(numAstronauts):
    list_space.append(jsonData['people'][i]['name'])
  print("The current astronaust in space are: ", list_space)
  print()


def calculator():
  print("Please choose an option from the menu below!")
  print("1. Add a + b\n2. Subtract a-b\n3. Multiply a*b\n4. Divide a/b\n5. Exit")
  option = int(input("What would you like to do? "))
  print()
  if option == 1: 
    print(add(), end='\n\n')
  elif option == 2: 
    print(subtract(), end='\n\n')
  elif option == 3: 
    print(multiply(), end='\n\n')
  elif option == 4: 
    print(divide(), end='\n\n')
  elif option == 5:
    print("Exiting Calculator")
  else:
    print("Please try an option 1-5")

keyMapQuest = 'NGMJMoREO5aShAzbLtLChdPpxGVbuLQd'
def maps():
  tripStartingLocation = input('Enter the starting address of your trip: ')
  tripEndingLocation = input('Enter the address of your ending location: ')
  uriMapQuest = 'http://www.mapquestapi.com/directions/v2/route?'
  uriEncoded = uriMapQuest + urlencode({"key": keyMapQuest, "from":tripStartingLocation, "to":tripEndingLocation})
  jsonData = requests.get(uriEncoded).json()
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
#  print("**TODO Maps**", end='\n\n')

def crypto():
  token = input('Please enter token symbol: ')
  cryptoURI = "https://api.lunarcrush.com/v2?data=assets&key={API_KEY_HERE}&symbol="+token.upper()
  json_data = requests.get(cryptoURI).json()
  tokenSymbol = str(json_data["config"]["symbol"])
  currentPrice = str(json_data["data"][0]["price"])
#  print(json_data)
  cryptoDict[tokenSymbol] = currentPrice
#  cryptoDict["price"].append("price")
  print(cryptoDict, end='\n\n')
  

cryptoDict = {}

def main():
  print("Welcome to my program!", end='\n\n')
  while True:
    print("Please choose an option from the menu below!")
    print("1. Astronauts\n2. Calculator\n3. Maps\n4. Crypto\n5. Exit")
    option = int(input("What would you like to do? "))
    print()
    
    if option == 1: 
      astronauts()
    elif option == 2: 
      calculator()
    elif option == 3: 
      maps()
    elif option == 4: 
      crypto()
    elif option == 5:
      break
    else:
      print("Please try an option 1-5")
  
  print("Thank you for using my program!")
main()
##
## End of file...