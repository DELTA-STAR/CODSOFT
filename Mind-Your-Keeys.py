#password generator(Mind-Your-Keeys)
import string
import random

def inp():
  n=int(input("Enter The Length Of The Password: "))
  if(n<8):
      print("-"*5,"Lower Than The Accepted Length Of Passwords","-"*5)
      print("-"*5,"The Minimum Limit Is Usually 8","-"*5)
      inp()
  elif(n>64):
      print("-"*5,"More Than The Accepted Length Of Passwords","-"*5)
      print("-"*5,"The Max Limit Is Usually 64","-"*5)
      inp()
  else:
      password(n)
        
def password(n):
  included=string.ascii_lowercase
  included+=string.ascii_uppercase
  included+=string.digits
  sc="!@#$%"
  included+=sc
  password=""
  for i in range(n):
    password+=random.choice(included)
  print(password)
  
print("-"*5,"WELCOME TO MIND-YOUR-KEEEYS PASSWORD GENERATOR","-"*5)
inp()
