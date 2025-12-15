#to do list code(loos-e-nds)
def create():
  l=open("list.txt","w")
  print("-"*5,"An Empty List Has Been Created!!","-"*5)
  n=int(input("Enter The Number Of Tasks To Be Added: "))
  for i in range(0,n,1):
    task=input("Enter Task: ")
    print("☐",task,file=l)
  l.close()
  print("-"*5,"Tasks/Task Has Been Successfully Added!!","-"*5)
  print()

def add():
  l=open("list.txt","a")
  n=int(input("Enter The Number Of Tasks To Be Added: "))
  for i in range(0,n,1):
    task=input("Enter Task: ")
    print("☐",task,file=l)
  l.close()
  print("-"*5,"Task/Task Has Been Successfully Added!!","-"*5)
  print()

def view():
  print("-"*5,"Here Is Your List: ","-"*5)
  l=open("list.txt","r")
  print(l.read())
  l.close()
  print()

def completed():
  l=open("list.txt","r")
  n=int(input("Enter The Number Of The Task That Is To Be Marked As Completed: "))
  for i in range(n):
    line=l.readline()
  l.close()
  l=open("list.txt","r")
  lines=l.readlines()
  l.close()
  l=open("list.txt","w")
  print()
  del(lines[n-1])
  l.writelines(lines)
  print("☑",line.split(" ",1)[1],file=l,end="")
  l.close()
  print("-"*5,"Congratulations On Completing The Task!!","-"*5)
  print("-"*5,"Task Has Been Successfully Marked!!","-"*5)
  print()

def delete():
  l=open("list.txt","r")
  n=int(input("Enter The Number Of The Task That Is To Be Deleted: "))
  line=l.readlines()
  l.close()
  l=open("list.txt","w")
  del(line[n-1])
  l.writelines(line)
  l.close()
  print("-"*5,"Task Has Been Successfully Deleted!!","-"*5)
  print()

print("-"*5,"WELCOME TO LOOS-E-NDS TO-DO-LIST","-"*5)
print()
print("What Would You Like You Like To-Do")
print("1. Create A List")
print("2. Add Task")
print("3. Delete Task")
print("4. View List")
print("5. Mark Task As Completed")
print("6. Exit")

while True:
  c=int(input("Choose An Option: "))
  match c:
    case 1:
      create()
    case 2:
      add()
    case 3:
        delete()
    case 4:
      view()
    case 5:
      completed()
    case 6:
      break
    case _:
      print("-"*5,"Invalid Option","-"*5)
