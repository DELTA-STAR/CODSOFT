#calculator code(do-your-math)
def inp():
  c=open("num.txt","a")
  n=int(input("Enter Number Of Elements To Be Entered: "))
  if(n>0):
    for i in range(n):
      e=int(input("Enter Number: "))
      print(e,file=c)
  else:
      print("Invalid Input")
      print()
      inp()

def option():
  print("-"*5,"Do You Want To Continue?","-"*5)
  print()
  o=int(input("Enter 1 to Continue otherwise 0: "))
  if(o==0):
    c=open("num.txt","w")
    c.close()
    return 0
  print()

def add():
  inp()
  c=open("num.txt","r")
  s=0
  num=c.readline()
  while(num!=""):
    n=num.strip()
    s=s+float(n)
    num=c.readline()
  c.close()
  print("-"*5,"The Sum Of The Entered Elements Is: ",s,"-"*5)
  c=open("num.txt","w")
  print(s,file=c)
  c.close()
  print()

def sub():
  inp()
  c=open("num.txt","r")
  num=c.readline()
  n=num.strip()
  s=float(n)
  num=c.readline()
  while(num!=""):
    n=num.strip()
    s=s-float(n)
    num=c.readline()
  print("-"*5,"The Difference Of The Entered Elements Is: ",s,"-"*5)
  c.close()
  c=open("num.txt","w")
  print(s,file=c)
  c.close()
  print()
  
def mul():
  inp()
  c=open("num.txt","r")
  num=c.readline()
  m=1
  while(num!=""):
    n=num.strip()
    m=m*float(n)
    num=c.readline()
  print("-"*5,"The Multiplication Of The Entered Elements Is: ",m,"-"*5)
  c.close()
  c=open("num.txt","w")
  print(m,file=c)
  c.close()
  print()

def div():
  inp()
  c=open("num.txt","r")
  num=c.readline()
  n=num.strip()
  d=float(n)
  num=c.readline()
  while(num!=""):
    n=num.strip()
    if(n=="0"):
      d=0
    else:
      d=d/float(n)
      num=c.readline()
  print("-"*5,"The Division Of The Entered Elements Is: ",d,"-"*5)
  c.close()
  c=open("num.txt","w")
  print(d,file=c)
  c.close()
  print()

print("-"*5,"WELCOME TO DO-YOUR-MATH CALCULATOR","-"*5)
print()
print("What Would You Like To Do\n")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Exit")
while True:
    o=int(input("Choose An Option: "))
    match o:
        case 1:
            add()
            o=option()
            if (o==0):
                break
        case 2:
            sub()
            o=option()
            if (o==0):
                break
        case 3:
            div()
            o=option()
            if (o==0):
                break
        
        case 4:
            mul()
            o=option()
            if (o==0):
                break
        case 5:
            break
        case _:
            print("-"*5,"Invalid Option","-"*5)
