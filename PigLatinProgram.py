#Name: PigLatin
#Author: Owen
#Date: 12/16/21
#Description: Translates text into Piglatin

def translate():
#Translating "qu"
  v_flag = False
  if i[0] == "q" and i[1] ==  "u" or i[0] == "Q" and i[1] ==  "u":
    for ltr in i:
#Punctuation
      if ltr not in vowel and ltr not in consonant and ltr not in y:
        print(ltr)
      pos = i.find(ltr)
      if i[pos] in vowel and pos > 1 and v_flag == False:
#Moves letters of the word around and adds it to a list to print later
        q = (i[pos:] + i[0:pos] +"ay")
        mylist.append(q)
        v_flag = True
#Translating words that start with vowels
  elif i[0] in vowel:
    for ltr in i:
      if ltr not in vowel and ltr not in consonant and ltr not in y:
          print(ltr)
    mylist.append(i +"way")
#Translating words that start with consonants
  elif i[0] in consonant:
    for ltr in i:
      if ltr not in vowel and ltr not in consonant and ltr not in y:
        print(ltr)
      if ltr in vowel and v_flag == False:
        pos = i.find(ltr)
        x = (i[pos:] + i[0:pos] +"ay")
        mylist.append(x)
        v_flag = True
  return ""
  
def y_translate():
#Translating y as a consonant
  while i[0] == "y" or i[0] == "Y":
    print(translate())
    break
  y_pos = i.find("y")
  if y_pos > 0:
#Translating y as a vowel
    for ltr in i:
      if ltr not in vowel and ltr not in consonant and ltr not in y:
        print(ltr)
      pos2 = i.find(ltr)
      if i[pos2] in vowel and pos2 < y_pos:
        print(translate())
        break
      elif ltr == "y" or ltr == "Y":
#Moves letters of the word around and adds it to a list to print later
        x_y = i[y_pos:] + i[0:y_pos] +"ay"
        mylist.append(x_y) 
  return ""

#variables
vowel = "aeiouAEIOU"
consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
y = "yY"
qu = "qu"
Qu = "Qu"


while(True): #Loop until user wants to stop
  mylist = [""]
  print()
#Get user input
  sentence = input("Enter the words you want to translate into piglatin: ")

#use split() to separate each word in the sentence
  words = sentence.split(" ")

#Determining if the program needs to translate y
  for i in words:
    if "y" in i or "Y" in i:
      print(y_translate())
    else: 
      print(translate())

#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
  print(" ".join(mylist)) #turns translated words into a sentence format
  print("\n")

#Repeat program
  again = input("Again? (Y/N)")
  if again[0].upper() == "N":
    break 