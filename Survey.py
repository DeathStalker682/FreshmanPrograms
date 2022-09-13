""" 
Name: Dynamic Survey
Author: Owen Maguire
Date: 10/4/21
Description: A survey of seven questions for the user. 
Location: Baeverton Hish School, Oregon
"""


# Intro 
print("Hello, I'm the computer. This program will ask you some questions and respond.")

#Question 1
print("Do you like videogames?", end=" ")
answer1 = input()
if(answer1.lower() == "yes"):
  print("Good.\n")
else:
  print("How could you say such a thing.\n")
    
#Question 2
print("What is your name?", end=" ")
name = input()
if(name.lower() == "owen"):
  print("That's my name too!\n")
elif(name.lower() == "chris"):
  print("That's my dad's name!\n")
elif(name.lower() == "jaime"):
  print("That's my mom's name!\n")
else: print("Nice to meet you ", name, ".\n", sep="")

#Question 3
print("What is your favorite food?", end=" ")
food = input()
if(food.lower() == "cheese"):
  print("I like cheese too!\n")
else:
  print(food,"is tasty.\n")

#Question 4
print("What hobbies do you have?", end=" ")
hobby = input()
if(hobby.lower() == "biking"):
  print("No way! I like to bike as well!\n")
else:
  print(hobby,"seems fun.\n")

#Question 5
print("What is your favorite color?", end=" ")
color = input()
if(color.lower() == "purple"):
  print("Purple is the best color\n")
else:
  print(color,"is an interesting color.\n")

#Question 6
print("What is the answer to 3+7?", end=" ")
number = input()
if(number == "10"):
  print("Correct!\n")
elif(number != "10"):
  print(number,"is incorrect.\n")

#Question 7
print("Which do you pour first, cereal or milk?")
cereal = input()
if(cereal.lower() == "cereal"):
  print("Correct!")
else:
  print("Cereal always goes first.")
