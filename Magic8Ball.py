#Title:Magic8Ball
#Author: Owen Maguire
#Date: 1/20/22
#Desc: A Magic 8 Ball program
#Location: Beaverton High School, Oregon

#variables
reply1 = "It is certain"
reply2 = "Without a doubt"
reply3 = "You may rely on it"
reply4 = "Yes definitely"
reply5 = "It is decidedly so"
reply6 = "As I see it, yes"
reply7 = "Most likely"
reply8 = "Yes"
reply9 = "Outlook is good"
reply10 = "Signs point to yes"
reply11 = "Reply hazy try again"
reply12 = "Better not tell you now"
reply13 = "Ask again later"
reply14 = "Cannot predict now"
reply15 = "Concentrate and ask again"
reply16 = "Don’t count on it"
reply17 = "Outlook is not so good"
reply18 = "My sources say no"
reply19 = "Very doubtful"
reply20 = "My reply is no"

#question
x = input("Please ask your question:  ")
print("\n")

import random
num = random.randint(1,20)

if num == 1:
  print(reply1)
elif num == 2:
  print(reply2)
elif num == 3:
  print(reply3)
elif num == 4:
  print(reply4)
elif num == 5:
  print(reply5)
elif num == 6:
  print(reply6)
elif num == 7:
  print(reply7)
elif num == 8:
  print(reply8)
elif num == 9:
  print(reply9)
elif num == 10:
  print(reply10)
elif num == 11:
  print(reply11)
elif num == 12:
  print(reply12)
elif num == 13:
  print(reply13)
elif num == 14:
  print(reply14)
elif num == 15:
  print(reply15)
elif num == 16:
  print(reply16)
elif num == 17:
  print(reply17)
elif num == 18:
  print(reply18)
elif num == 19:
  print(reply19)
elif num == 20:
  print(reply20)