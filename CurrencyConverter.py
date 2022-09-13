#Author: Owen Maguire
#Name: Currency Converter
#Date: 3/7/22
#Desc: Convert US Dollars to other currencies
#Location: Beaverton High School, Oregon


def pesos():
  peso = dollars * 20.71 
  print("$",dollars,"=", round(peso, 2))
  return ""

def pounds():
  pound = dollars * 0.76 
  print("$",dollars,"=", round(pound, 2))
  return ""
  
def euros():
  euro = dollars * 1.1 
  print("$",dollars,"=", round(euro, 2))
  return ""

def canadian():
  canada = dollars * 1.27
  print("$",dollars,"=", round(canada, 2))
  return ""

def yens():
  yen = dollars * 118.44
  print("$",dollars,"=", round(yen, 2))
  return ""
  

#Inf loop
while(True):
#Variables
  dollars = 0
  currency = 0
  money = ["pesos","pounds", "euros", "canadian", "yen"]
  
#user input
  while(dollars > 500 or dollars <1):
    try:
      dollars = int(input("Please enter the amount of money you want to convert in US Dollars ($1-500): \n"))
      print("\n")
    except ValueError:
        print("Please input a number only...")
    
  while(currency not in money):
    currency = input("Please pick a currency (Pesos, Pounds, Euros, Canadian, Yen)")

#Decide which currency to convert to
  if currency.lower() == "pesos":
    print(pesos())
  elif currency.lower() == "pounds":
    print(pounds())
  elif currency.lower() == "euros":
    print(euros())
  elif currency.lower() == "canadian":
    print(canadian())
  elif currency.lower() == "yen":
    print(yens())

#Repeat Program
  again = input("Again? (Y/N)")
  if again[0].upper() == "N":
    break