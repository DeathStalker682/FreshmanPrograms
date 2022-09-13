#Name: Roman Numerals
#Author: Owen Maguire
#Date: 10/24/21
#Desc: User enters a whole number between 1 and 3999 and the program converts it into Roman Numerals. Repeats until user wants to quit. 
#Location: Beaverton High School, Oregon


#dictionary of value-symbol relationships
Rnum = {1000:"M", 900:"CM", 500:"D", 400:"CD",100:"C",90:"XC", 50:"L", 40:"XL",10:"X", 9:"IX",5:"V",4:"IV",1:"I",0:""}

while(True):#infinite loop

  #spacing
  print()

  #intro
  print("This program will take a number, provided by you, from 1 to 3999 and turn it into Roman Numerals. \n")

  #User input
  num = int(input("Please enter a number. (1-3999)   "))

  #Determines if number is between 1 and 3999
  while(num > 3999):
    print("Not a valid number")
    num = int(input("Please enter a number. (1-3999)   "))

  #Turning number in Roman Numerals
  while(num >= 1000):
    print(Rnum[1000], end = "")
    num -= 1000
  while(num >= 900):
    print(Rnum[900], end = "")
    num -= 900
  while(num >= 500):
    print(Rnum[500], end = "")
    num -= 500
  while(num >= 400):
    print(Rnum[400], end = "")
    num -= 400
  while(num >= 100):
    print(Rnum[100], end = "")
    num -= 100
  while(num >= 90):
    print(Rnum[90], end = "")
    num -= 90
  while(num >= 50):
    print(Rnum[50], end = "")
    num -= 50
  while(num >= 40):
    print(Rnum[40], end = "")
    num -= 40
  while(num >= 10):
    print(Rnum[10], end = "")
    num -= 10
  while(num >= 9):
    print(Rnum[9], end = "")
    num -= 9
  while(num >= 5):
    print(Rnum[5], end = "")
    num -= 5
  while(num >= 4):
    print(Rnum[4], end = "")
    num -= 4
  while(num >= 1):
    print(Rnum[1])
    num -= 1
  
  #spacing
  print()
  print()

   #breaking infinite loop
  again = input("Again? (Y/N)")
  if again[0].upper() != "Y":
    break 