#Name: Number Guess
#Author: Owen Maguire
#Date: 10/11/21
#Desc: Generate a random number and have the user guess the number with the program saying "higher" or "lower" if the guess is off.
#Location: Beaverton High School, Oregon

import random # random number generator

while(True):

  print("This is a number guessing game. A number from 1-100 has already been chosen. Try to guess the number within 6 attempts or you FAIL! \n")

  rnum = random.randint(1, 100)
  attempt = 6
  guess = " "

  while(attempt > 0  and guess != rnum):
    print("You have", attempt, "guesses remaining.\n")
    try:
      guess = int(input("Guess (1-100): "))
      attempt -= 1
    except:
      print("That's not a valid number.\n")
      attempt == attempt
      

  #check if guess is correct, larger, or smaller than rnum
  #prompt with, "Correct!", "too high", or "too low"
  # if attempts = 0 tell them they are out of guesses and they have lost

    if(guess == rnum):
      print("CORRECT! You guessed the number in", 6- attempt, "guess(es)!\n" )
    elif(guess < rnum):
      print("Your guess was smaller than the number.\n")
    elif(guess > rnum):
      print("Your guess was larger than the number.\n")

    if(attempt == 0 ):
      print("You lost. The number was", rnum, ".\n")
    

    # A way out
  again = input(" Play again? (Y/N)")
  if again[0].upper() == "N":
    break 