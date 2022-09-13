"""
Name: LoopGPA
Author: Owen Maguire
Date: 10/6/21
Description: Get user grades and calculate the GPA (Loop until user quits)
"""

#Infinite Loop
count = 0
while(True):
  count += 1
  
    # Intro
  print("Enter your letter or number grades and this program will calculate your GPA.\n")

  #Variables
  period = 0
  sum = 0
  valid = "ABCDFINX01234" # valid inputs
  grade = " "
  again = " "
  print("Please enter your grade for period (X to exit):")
  while(grade[0].upper() != "X" and period < 8): # Repeat program loop

    # Get user grades
    period += 1
    print("Period ", period, ": ", sep="",end="")
    while(grade[0].upper() not in valid):
      grade = input()
      if(grade.upper() not in valid):
        print("Invalid grade")
        
              
    #End of "Get valid grades" loop

      # Determine how much to add to sum  
    if (grade.upper() == "X" ):
      break
    elif(grade.upper() == "A" or grade == "4"):
      sum += 4
    elif(grade.upper() == "B" or grade == "3" ):
      sum += 3
    elif(grade.upper() == "C" or grade == "2" ):
      sum += 2
    elif(grade.upper() == "D" or grade == "1" ):
      sum += 1
    elif(grade.upper() == "F" or grade == "0" or grade == "N" or grade == "I"):
      pass # prevents += 0
    else:
      period -= 1 #subtract 1 to repeat period


    grade = " "
        # Calculate
  gpa = sum / period

      # Output
  print("Your GPA is", round(gpa, 2))
  print()

  if(period == 8):
    again = input("Again? (Y/N)")
  elif(again[0].upper == "N"):
    break


  # program won't break, I don't know how to fix it