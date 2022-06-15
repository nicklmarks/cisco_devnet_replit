'''

Welcome to 'Challenge Activity' 3.6.1.10.c01! This challenge
activity is going to test your comprehension on lists and
list methods! For this challenge you will be creating an interactive
list tool that interacts with the user. Here are the requirements 
for your list program for this Challenge Activity:

1. The program must run until the user decides to quit
2. Your list program needs to support the following user options:
    a. Append an element to the list
    b. Insert an element in the list (int/str/float)
    c. Remove an element from the list
    d. Clear the entire list
    e. Reverse the order of the elements in the list
    f. Print the last element in the list
3. Each time the list is changed, the new list should be printed out
   for the user

Once you have completed this activity you can 'Submit' your file and
view one possible solution set for the activity or you can 'Fork'
the solution set to have a copy with which you can work. If you look
at the image to the left, 3.6.1.10.c01-image you will see an 
example of what your menu could look like and how some of the 
functionality should work.

Good luck!!!

'''

print("Welcome to my list program!")
print()

list = []

message = '''What would you like to do:
1. Append an element to the list
2. Insert an element in the list
3. Remove an element from the list
4. Clear the list
5. Reverse the list elements
6. Print the last element in the list
7. Quit

'''

while True:
  try:
    print(message)
    userResponse = input('Enter your choice: ')
    #print(input)
    if int(userResponse) == 1:
      print("""Which data type would you like to enter:
            1. String
            2. Integer
            3. Float
            """)
      userResponse2 = input('Please Enter your choice: ')
      if int(userResponse2) == 1:
        #string
        userResponse2 = input('Please Enter a string: ')
        list.append(str(userResponse2))
      elif int(userResponse2) == 2:
        #Integer
        userResponse2 = input('Please Enter an integer: ')
        list.append(int(userResponse2))
      elif int(userResponse2) == 3:
        #Float
        userResponse2 = input('Please Enter an decimal number: ')
        list.append(float(userResponse2))
      print("Your current list is ", list)
  
      #break
    elif int(userResponse) == 2:
      print("""Which data type would you like to enter:
          1. String
          2. Integer
          3. Float
          """)
      userResponse3 = input('Please Enter your choice: ')
      userResponse3_index = int(input('Please Enter the index position (between 0 and ' +  str(len(list)) + '): '))
  
      if int(userResponse3) == 1:
        #string
        userResponse3_input = input('Please Enter a string: ')
        list.insert(userResponse3_index, str(userResponse3_input))
      elif int(userResponse3) == 2:
        #Integer
        userResponse3_input = int(input('Please Enter an integer: '))
        list.insert(userResponse3_index, int(userResponse3_input))
      elif int(userResponse3) == 3:
        #Float
        userResponse3_input = input('Please Enter an decimal number: ')
        list.insert(userResponse3_index, float(userResponse3_input))
      print("Your current list is ", list)
  
      #break
    elif int(userResponse) == 3:
      userResponse4 = int(input('Enter the index of the value you would like to remove(between 0 and ' +  str(len(list)) + ': '))
      if userResponse4 < 0 or userResponse4 > len(list) or type(userResponse4) != int:
        print("Please enter an index between 0 and ", len(list))
        break
      else:
        list.pop(userResponse4)
      print("Your current list is ", list)
      
    elif int(userResponse) == 4:
      print("The list has been cleared")
      list = []
      print("Your current list is ", list)
      #break
    elif int(userResponse) == 5:
      list.reverse()
      print("Your current list is ", list)
      #list = list2
      #break
    elif int(userResponse) == 6:
      print("The last element in the list is: ", list[-1])
      print("Your current list is ", list)
      #break
    elif int(userResponse) == 7:
      break
    else: 
      print("Invalid Entry. Please try again")

  except:
    print("An exception occured try again")

print("Your current list is ", list)
print("Thank you for using the program. Have a nice day!")
  