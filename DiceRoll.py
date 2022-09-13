#Name: DiceRoll
#Author: Owen Maguire
#Date: 10/15/21
#Desc: This program will "Roll" two dice and output the results to the user. It will also repeat until the user wishes to quit. 
#Location: Beaverton High School, Oregon

#   ─ │ ┌ ┐ └ ┘ ●    *Special Characters*

import random # random number library

#turns rolling the dice into a function
def dice():

  total = 0
  for i in range(2): # "rolls" 2 dice
    roll = random.randint(1, 6) # generates a random number 1-6

    i += 1

    #top of die
    print   ("┌───────────────┐")
    if(roll == 2 or roll == 3):
      print ("│ ●             │")
    elif(roll == 4 or roll == 5 or roll == 6):
      print ("│ ●           ● │")
    elif(roll == 1):
      print ("│               │")

    print   ("│               │")

    #middle of die
    if(roll == 1 or roll == 5 or roll == 3):
      print ("│       ●       │")
    elif(roll == 4 or roll == 2):
      print ("│               │")
    elif(roll == 6):
      print ("│ ●           ● │")

    print   ("│               │")
    #bottom of die
    if(roll == 4 or roll == 5 or roll == 6):
      print ("│ ●           ● │")
    elif(roll == 2 or roll == 3):
      print ("│             ● │")
    elif(roll == 1):
      print ("│               │")

    print   ("└───────────────┘")

    total += roll # adds both dice together

    if(i == 2):
      # prints the sum of 2 dice
      print("You rolled a(n)", total, "\n") 

  return ""

while(True): #infinite loop

  print()
  print("This program will randomly roll two dice and show you the output.\n")

  #breaking loop
  start = input("Would you like to roll? (Y/N)  ")
  if(start[0].upper() == "N"):
    break

  #prints the dice() function onto the screen
  print(dice())

  #breaking loop
  again = input("Roll again? (Y/N)")
  if again[0].upper() == "N":
    break 