#Name: Forgotten Highlands
#Author: Owen Maguire
#Date: 12/16/21
#Desc: A playable adventure game.
#Location: Beaverton High School, Oregon

#art from https://www.asciiart.eu/

#Sword in boulder to kill dragon?


def tree():
  print("        ^         ")
  print("       / \        ")
  print("      /   \       ")
  print("      /   \       ")  
  print("     /     \      ") 
  print("     /     \      ")
  print("    /       \     ")
  print("    ^^^[_]^^^     ")
  return ""

def mountains():
  print("          /\                                     ")
  print("         /**\                                    ")
  print("        /****\   /\                              ")
  print("       /      \ /**\                             ")
  print("      /  /\    /    \        /\    /\  /\        ")
  print("     /  /  \  /      \      /  \/\/  \/  \  /\   ")
  print("    /  /    \/ /\     \    /    \ \  /    \/  \  ")
  print("   /  /      \/  \/\   \  /      \    /   /    \ ")
  print("__/__/_______/___/__\___\________________________")
  return ""

def ocean():
  print("          |                          ")
  print("        \ _ /                        ")
  print("      -= (_) =-                      ")  
  print("        /   \         _\/_           ")
  print("          |           //|\  _\/_     ")
  print("   _____ _ __ __ ____ _ | __/|\/ _   ")
  print(" =-=-_-__=_-= _=_=-=_,- |_--|-,_     ")  
  print("  =- _=-=- -_=-=_,-           |      ")
  print(" =- =- -=.--                         ")
  return ""

def cliff():      
  print("       _.-'````````-._                            ")
  print("    /-`                '.                         ")
  print("    `':.,_               '._                      ")
  print("         \`'-._             `'-._                 ")
  print("          \    `:._              `'-._            ")
  print("          |      \ `:_                `-----      ")
  print("          |       \   `:_                         ")
  print("          |      :|    \ '.                       ")
  print("          |       |     |  `:_                    ")
  print("          |       |:    |     `:_                 ")
  print("          |:      |     |                         ")
  print("          |       |                               ")
  print("          |                                       ")
  return ""

def stream():
  print("     )\      ")
  print("    ( (      ")
  print("    ) \      ")
  print("   /  (      ")
  print("   \   \     ")
  print("    )   )    ")
  print("    /   (    ")
  print("   (     \   ")
  print("   )     \   ")
  print("  /       \  ")
  return ""
  
def grass():
  print(" - \|/         -         -    \/    ")
  print("      ------     --- \|/     --     ")
  print("---           \|/ ---       ---     ")
  print("  \/   ---- \/              ----    ")
  print("-----         -----   \|/     ---   ")
  print("---     --      ------      \|/     ")
  print("  \|/ ----     -\|/----        ---  ")
  print("----   \/  -       --------    \|/  ")
  return ""

#variables
x = 0
y = 0
machete = False
rope = False
north = True
east = True
south = True
west = True

#reference other file       
#word art from: https://patorjk.com/software/taag/#p=display&f=Big&t=
title = open("title.txt")
for line in title:   #https://www.w3schools.com/python/ref_string_rstrip.asp
  line = line.rstrip()
  print(line)
print("This is an adventure game. Your goal is to escape. Use cardinal directions to move around. (North, South, East, West) Type exit to quit.")

while(True):
  print(x,y,"\n")

  if machete == True:
    print("┌───────┐")
    print("│Machete│")
    print("└───────┘")
  if rope == True:
    print("┌────┐")
    print("│Rope│")
    print("└────┘")
    
  #user commands
  move = input("").lower()
  #commands
  if move[0] == "n" and north == True:
    y += 1
  elif move[0] == "s" and south == True:
    y -= 1
  elif move[0] == "e" and east == True:
    x += 1
  elif move[0] == "w" and west == True:
    x -= 1
  elif move == "exit":
    break
  else: 
    print("I'm sorry, I don't know what to do with that command. \n")

  #Locations
  if x == 0 and y == 0:
    print(grass())
    print("You are in a grass plain with mountains and forests far in the distance.")
    north = True
    east = True
    south = True
    west = True
  elif x == 1 and y == 0:
    print(stream())
    print("You walk for a bit and find a small, moss covered, stream in front of you.")
    north = True
    east = True
    south = True
    west = True
  elif x == 2 and y == 0:
    print(cliff())
    print("You are at the edge of a cliff. You look down and see a pile of bones! This must have been where people tried to get down before.")
    north = True
    east = False
    south = True
    west = True
  elif x == -1 and y == 0:
    print(tree())
    print("You are in a forest, and you see something strange on a tree to the north.")
    north = True
    east = True
    south = True
    west = True
  elif x == -2 and y == 0:
    print(tree())
    print("The forest is too thick for you to go any further to the West.")
    north = True
    east = True
    south = True
    west = False
  elif x == 0 and y == 1:
    print(mountains())
    print("The mountains to the north look very large from here.")
    north = True
    east = True
    south = True
    west = True
  elif x == 1 and y == 1:
    print(stream())
    print("You see a small, moss covered stream.")
    north = True
    east = True
    south = True
    west = True
  elif x == 2 and y == 1:
    print(cliff())
    print("You are at the edge of a cliff. There is no way down from here.")
    north = True
    east = False
    south = True
    west = True
  elif x == -1 and y == 1:
    print(tree())
    print("You are in a forest. There is a tree with <-- engraved on it.")
    north = True
    east = True
    south = True
    west = True
  elif x == -2 and y == 1:
    print(tree())
    print("The forest is thick. Maybe if you had a tool you could go further to the west.")
    north = True
    east = True
    south = True
    west = False
    if machete == True:
      west = True
  elif x == 0 and y == 2:
    print(mountains())
    print("You are at the foot of massive, impassible mountains.")
    north = False
    east = True
    south = True
    west = True
  elif x == 1 and y == 2:
    #reference other file
    waterfall = open("waterfall.txt")
    for line in waterfall:
      line = line.rstrip()
      print(line)
    print("You see a small waterfall running off the edge of the mountains.")
    north = False
    east = True
    south = True
    west = True
  elif x == 2 and y == 2:
    print(mountains())
    print("There is a cliff to the East. It looks like you might be able to get down from there if you had a tool.")
    north = False
    east = False
    south = True
    west = True
    if rope == True:
      east = True
  elif x == -1 and y == 2:
    print(mountains())
    print("You are at the foot of impassible mountains, but it looks like there is a large structure to the West.")
    north = False
    east = True
    south = True
    west = True
  elif x == -2 and y == 2:
    #reference other file
    castle = open("castle.txt")
    for line in castle:
      line = line.rstrip()
      print(line)
    print("You are in front of a large blackstone castle. It looks deserted.")
    north = True
    east = True
    south = True
    west = False
  elif x == 0 and y == -1:
    print(grass())
    print("You come across a herd of grazing buffalo, and you see what looks like an ocean to the South.")
    north = True
    east = True
    south = True
    west = True
  elif x == 1 and y == -1:
    print(tree())
    print("You find a giant boulder in the middle of a circle of trees. It looks manmade.")
    north = True
    east = True
    south = True
    west = True
  elif x == 2 and y == -1:
    print(cliff())
    print("You are at the edge of a cliff. There is no way down from here. ")
    north = True
    east = False
    south = True
    west = True
  elif x == -1 and y == -1:
    print(tree())
    print("You are in a thin forest with an ocean to the South.")
    north = True
    east = True
    south = True
    west = True
  elif x == -2 and y == -1:
    print(tree())
    print("The forest is thick. You cannot go any further to the West.")
    north = True
    east = True
    south = True
    west = False
  elif x == 0 and y == -2:
    print(ocean())
    print("You are on a beach. There is shrapnel and burnt wood all around you. Something must have happened here.")
    north = True
    east = True
    south = False
    west = True
  elif x == 1 and y == -2:
    print(ocean())
    print("You are on a beach. There is shrapnel and burnt wood all around you. Something must have happened here.")
    north = True
    east = True
    south = False
    west = True
  elif x == 2 and y == -2:
    print(ocean())
    print("You are on a beach. There is shrapnel and burnt wood all around you. Something must have happened here.")
    north = True
    east = False
    south = False
    west = True
  elif x == -1 and y == -2:
    print(ocean())
    print("You are on a beach. There is shrapnel and burnt wood all around you. You look down and find a machete. I wonder what this could be used for?")
    north = True
    east = True
    south = False
    west = True
    machete = True
  elif x == -2 and y == -2:
    print(ocean())
    print("You are on a beach. You look out towards the ocean and see a glimmer of something! I wonder what it could be?")
    north = True
    east = True
    south = False
    west = False
  elif x == -3 and y == 1:
    village = open("village.txt")
    for line in village:
      line = line.rstrip()
      print(line)
    print("As you cut through the foliage you find yourself in a small clearing with a few clay huts. It looks empty, but you see a smoldering fire in front of you. You walk into one of the huts and find rope! This could be useful. There is nowhere else to go in the village.")
    north = False
    east = True
    south = False
    west = False
    rope = True
  elif x == -2 and y == 3:
  #reference other file
    entrance = open("entrance.txt")
    for line in entrance:
      line = line.rstrip()
      print(line)
    print("You walk into the front gate of the castle and are met with two guards blocking your way, or so you thought. It looks like the guards have been turned to stone!")
    north = True
    south = True
    east = True
    west = True
  elif x == -2 and y == 4:
    garden = open("garden.txt")
    for line in garden:
      line = line.rstrip()
      print(line)
    print("You seem to be in the castle garden. As you walk around you see bloodstains on the ground?! Could a battle have happened here?")
    north = True
    south = True
    east = False
    west = False
  elif x == -2 and y == 5:
    wall = open("wall.txt")
    for line in wall:
      line = line.rstrip()
      print(line)
    print("You walk even further into the castle and see a wall. Something about that wall looks suspicious.")
    north = True
    south = True
    east = False
    west = False
  elif x == -2 and y == 6:
    dragon = open("dragon.txt")
    for line in dragon:
      line = line.rstrip()
      print(line)
    print("You look away and run straight through the wall. It was just an illusion? Then your eyes adjust and you realize your mistake. You are standing in front of a very hungry DRAGON! It swallows you whole.")
    lose = open("lose.txt")
    for line in lose:
      line = line.rstrip()
      print(line)
    #Play again
    again = input("Play again? (Y/N)")
    if again[0].upper() == "N":
      break
    elif again[0].upper() == "Y":
      north = True
      south = True
      east = True
      west = True
      machete = False
      rope = False
      x = 0
      y = 0 
  elif x == 3 and y == 2:
    win = open("win.txt")
    for line in win:
      line = line.rstrip()
      print(line)
    print("YOU ESCAPED! Now what will you do adventurer?")
    #Play again
    again = input("Play again? (Y/N)")
    if again[0].upper() == "N":
      break
    elif again[0].upper() == "Y":
      title = open("title.txt")
      for line in title:   
        line = line.rstrip()
        print(line)
      print("This is an adventure game. Your goal is to escape. Use cardinal directions to move around. (North, South, East, West) Type exit to quit.")
      north = True
      south = True
      east = True
      west = True
      machete = False
      rope = False 
      x = 0
      y = 0