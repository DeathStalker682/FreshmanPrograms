#Name: Lingo
#Author: Owen
#Date: 10/27/21
#Desc: The object of the game is to find a 5 letter word by guessing a word, and in return receiving two kinds of clues. Characters that are fully correct, with respect to identity as well as to position, are enclosed in square brackets []Characters that are present in the word, but in the wrong position are enclosed in parenthesis ().
#Location: Beaverton High School, Oregon

from random import randint

#Functions

def GetWord():
  WordCount = 0

  with open("Words.txt", "r") as file_in:
    for thing in file_in:  #opens Words.txt and counts how many words are in it
      WordCount += 1

  num = randint(1, WordCount)

  with open("Words.txt", "r") as file_in:
    for thing in range(num):  #Picks a random word in Words.txt
      pick = file_in.readline()

  return pick.strip("\r\n") #strips invisible characters
  #End of GetWord() function

while(True): #infinite loop

  SecretWord = GetWord()
  #print(SecretWord) 

  #Intro
  print()

  print("This program will generate a random 5 letter word and you will have to guess it. If the letter is in the word, but not it the right position it will be in ( ). If the letter is in the word and in the correct position it will be in [ ]\n")

  #User input
  guess = input("Guess a random 5 letter word:   ").lower()
  print()

  while(guess != SecretWord):
    
    #limit letters in guess
    while(len(guess) != 5):
      print("Invalid Entry. Please enter a 5 letter word.\n")
      guess = input("Guess a random 5 letter word:   ").lower()
      print()
      
      #loop through letters in guess and give clues
    for ltr in guess:
      pos = SecretWord.find(ltr)
      if(pos < 0):
        print(ltr, end = "")
      elif(SecretWord[pos] == guess[pos]):
          print("["+ltr+"]", end = "")
      else:
        print("("+ltr+")", end = "")

    print("\n")

    #is guess right or wrong
    if(guess != SecretWord):
      guess = input("Guess a random 5 letter word:   ").lower()
    print()
    if(guess == SecretWord):
      print("YOU WIN! The word was ",SecretWord, "!", sep = "")
      break
      
  #breaking loop
  again = input("Play Again? (Y/N)")
  if again[0].upper() != "Y":
    break 