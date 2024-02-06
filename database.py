
users =[]
user={}
def add_user():
  name= input("enter your name ")
  age =input ("enter your age ")
  city =input ("enter your city ")
  user ["name"]=name
  user ["age"]=age
  user ["city"]=city
  with open("users.txt", "a") as f:
     f.write(str(user)) 
  return user

def display_user():
     with open("users.txt", "r") as f:
        for line in f:
           print(line)
#   users .append(user)
#   print (users , "\n")



while True :
  print("1. open registration\n2. acess data\n3. exit \n")
  choice  = input ("enter your choose  ")

  if choice  =='1':
     add_user()

  elif  choice =='2':
     display_user()

  elif choice  =='3':
     break  

