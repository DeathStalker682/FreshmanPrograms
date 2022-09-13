#Name: Leap Year
#Author: Owen Maguire
#Date: 5/2/22
#Desc: Program that determines whether or not a specific year is a leap year. 
#Location: Beaverton High School, Oregon

def leapyear():
  numbers = False
  while numbers == False:
#User Input
    year = input("Please enter a year (No BCE or letters): ")
#Make sure input is only numbers
    numbers = year.isdecimal()
#Determine if year is a century year
  yearlen = len(year)
  year1 = int(year)
  last = yearlen - 1
  seclast = yearlen - 2
#Determine if year is a leap year
  if year[last] == "0" and year[seclast] == "0":
    rem = year1 % 400
    if rem == 0:
       print("This year is a leap year")
    else:
      print("This year is not a leap year")
    return""
  else:
    rem = year1 % 4
    if rem == 0:
       print("This year is a leap year")
    else:
      print("This year is not a leap year")
    return ""

#Inf Loop
while(True):
  print("This program will determine if a year is a leap year or not. \n")
#Print Function
  print(leapyear())

#Repeat Program
  again = input(" Play again? (Y/N)")
  if again[0].upper() == "N":
    break 