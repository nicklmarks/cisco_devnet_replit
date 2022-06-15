#add, subtract, multiply, and divide two numbers

def add():
  """add(a,b) = a+b"""
  print(add.__doc__)
  a = int(input("Choose a value for a: "))
  b = int(input("Choose a value for b: "))  
  return a + b

def subtract(): 
  """subtract(a,b) = a-b"""
  print(subtract.__doc__)
  a = int(input("Choose a value for a: "))
  b = int(input("Choose a value for b: "))  
  return a - b

def multiply(): 
  """multiply(a,b) = a*b"""
  print(multiply.__doc__)
  a = int(input("Choose a value for a: "))
  b = int(input("Choose a value for b: "))  
  return a * b

def divide(): 
  """divide(a,b) = a/b"""
  print(divide.__doc__)
  a = int(input("Choose a value for a: "))
  b = int(input("Choose a value for b: "))  
  return a // b

