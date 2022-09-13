#Name: Caeser Cipher
#Author: Owen
#Date: 11/2/21
#Desc: Let the user shift the letters of the alphabet a certain amount and then print whatever they want in that cipher.
#Location: Beaverton High School, Oregon


def encrypt():

  #alphabet
  E_alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

  #User Text
  Etext = input("Please enter the text you would like to encrypt:   ").lower()

  #Inputting shift value
  Eshift = int(input("Please enter a shift value (1-25):   "))
  while(Eshift < 1 or Eshift > 25):
    print("Invalid shift value")
    Eshift = int(input("Please enter a shift value (1-25):   "))

  #Shifting text
  for E_ltr in Etext:
    Epos = E_alpha.find(E_ltr)
    if(Epos < 0):
      print(E_ltr, end = "")
    if(E_ltr not in E_alpha):
      pass
    if(E_ltr in E_alpha):
      print(E_alpha[Epos + Eshift], end = "")
   
    
  return "" 


def decrypt():
  #alphabet
  D_alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

  #User Text
  Dtext = input("Please enter the text you would like to decrypt:   ").lower()

  #Inputting shift value
  Dshift_val = input("Do you know the shift value? (Y/N)")

  if Dshift_val[0].upper() == "Y":
    Dshift = int(input("Please enter the shift value (1-25):   "))
    while(Dshift < 1 or Dshift > 25):
      print("Invalid shift value")
      Dshift = int(input("Please enter the shift value (1-25):   ")) 

    #Shifting text
    for D_ltr in Dtext:
      Dpos = D_alpha.find(D_ltr)
      if(Dpos < 0):
          print(D_ltr, end = "")
      if(D_ltr not in D_alpha):
        pass
      if(D_ltr in D_alpha):
        print(D_alpha[Dpos - Dshift], end = "")

  #Unknown Shift Value
  if Dshift_val[0].upper() == "N":
    print("This program will now list all possible outcomes.")
    print()
    for i in range(25):
      for D_ltr in Dtext:
        Dpos = D_alpha.find(D_ltr)
        if(Dpos < 0):
          print(D_ltr, end = "")
        if(D_ltr not in D_alpha):
          pass
        if(D_ltr in D_alpha):
          print(D_alpha[Dpos - i], end = "")
      #spaces out seperate decryptions
      print()
  return "" 

while(True): #infinite loop
  print()

  #intro
  print("This program will either encrypt or decrypt a message with the Caeser Cipher\n")

  #Encryption or decryption?
  cipher_type = input("Encrypt or Decrypt? (E/D)")
  if cipher_type[0].upper() == "E":
    print(encrypt())   
  elif cipher_type[0].upper() == "D":
    print(decrypt())

  #Breaking while loop
  again = input("Run again? (Y/N)")
  if again[0].upper() != "Y":
    break 
