#Name: Decimal to Fraction
#Author: Owen Maguire
#Date: 4/12/22
#Desc: Turn decimals into fractions 

#math library
import math


#decimals to fractions
def DF():
  print("Decimals to Fractions. \n")
  decimal = input("Please enter a decimal (0.___):  ")
  num = decimal.split(".")[1]
  den = 1
  for x in num:
    den = den * 10
  num = int(num)
  den = int(den)
  gcf = math.gcd(num, den)
  numerator = num / gcf
  denominator = den / gcf
  numerator = int(numerator)
  denominator = int(denominator)
  print(numerator, "/", denominator, sep = "")
  return ""

#fractions to decimals
def FD():
  print("Fractions to Decimals. \n")
  fraction = input("Please enter a fraction (x/y):  ")
  numbers = fraction.split("/")
  half1 = int(numbers[0])
  half2 = int(numbers[1])
  division = half1 / half2
  quotient = round(division, 10)
  print(quotient)
  return ""

print("This program will convert decimals to fractions and fractions to decimals. \n")


while(True):
  choice = input("Fractions --> Decimals  or  Decimals --> Fractions  (FD/DF): \n")

#Decide between conversions
  if choice.upper() == "FD":
    print(FD())
    break
  elif choice.upper() == "DF":
    print(DF())
    break
  else:
    print("Not an option, try again.")

#Repeat program
  again = input(" Convert again? (Y/N)")
  if again[0].upper() == "N":
    break 
    
#Some parts of this program are broken fyi
