# Author: Muhammad Ibrahim
# Date: 1 November 2021
# Description: Use initial velocity, change in height, and launch angle to solve types 1, 2, and 3 projectile motion problems.

import math

# TYPE 1
def type1():
  unknown = input("What are you solving for?\n1. Change in X or Distance\n2. Change in Y or Height\n3. Initial Velocity\n")

  print("\n")
  # Solving for delta x
  if unknown == "1":
    deltaY = float(input("Enter the height or change in Y (m): "))
    Vi = float(input("Enter the initial velocity (m/s): "))

    discriminant = deltaY/-4.9
    if discriminant < 0:
      discriminant = -discriminant

    print("\nChange in X: \n" + str(math.floor(Vi * t * 10000) / 10000) + " meters")
    print("Time in the air: \n" + str(math.floor(math.sqrt(discriminant) * 10000) / 10000) + " seconds")
    print("Final velocity before hitting the ground: \n" + str(math.floor(math.sqrt(discriminant) * -9.8 * 10000) / 10000) + " meters/second")
  
  # Solving for delta y
  elif unknown == "2":
    deltaX = float(input("Enter the distance or change in X (m): "))
    Vi = float(input("Enter the initial velocity (m/s): "))

    print("\nChange in Y:\n" + str(math.floor(-4.9 * (deltaX/Vi)**2 * 10000) / 10000) + " meters")
    print("Time in the air\n" + str(math.floor(deltaX/Vi * 10000) / 10000) + " seconds")
    print("Final velocity before hitting the ground: \n" + str(math.floor(deltaX/Vi * -9.8 * 10000) / 10000) + " meters/second")

  # Solving for initial velocity
  elif unknown == "3":
    deltaX = float(input("Enter the distance or change in X (m): "))
    deltaY = float(input("Enter the change in Y (m): "))

    discriminant = deltaY/-4.9
    if discriminant < 0:
      discriminant = -discriminant
    
    print("\nInitial velocity:\n" + str(math.floor(deltaX/math.sqrt(discriminant) * 10000) / 10000) + " meters")
    print("Time in the air:\n" + str(math.floor(math.sqrt(discriminant) * 10000) / 10000) + " seconds")
    print("Final velocity before hitting the ground: \n" + str(math.floor(math.sqrt(discriminant) * -9.8 * 10000) / 10000) + " meters/second")


  else:
    print("Invalid Input please run the program again...")

# TYPE 2
def type2():
  Vi = float(input("Enter initial velocity (m/s): "))
  Angle = float(input("Enter the launch angle (degrees): "))

  # solve for velocities
  Vix = Vi * math.cos(math.radians(Angle))
  Viy = Vi * math.sin(math.radians(Angle))

  # print the distance the projectile will travel and the time it will take
  hangTime = Viy / 4.9
  print("\nTime in the air: " + str(math.floor(hangTime * 10000) / 10000) + " seconds")
  print("Distance traveled: " + str(math.floor(hangTime * Vix * 10000) / 10000) + " meters")

  # print the apex height and the time the projectile is at the apex height
  print("\nApex height: " + str(math.floor(Viy**2 / 19.6 * 10000) / 10000) + " meters")
  print("Apex height time: " + str(math.floor(hangTime/2 * 10000) / 10000) + " seconds")

  #final velocity just before hitting the ground
  print("\nFinal velocity before hitting the ground: \n" + str(math.floor(math.sqrt(Vix**2 + Viy**2) * 10000) / 10000) + " meters/second")

# TYPE 3
def type3():
  Vi = float(input("Enter initial velocity (m/s): "))
  Angle = float(input("Enter the launch angle (degrees): "))
  launchHeight = float(input("Enter the initial height (m): "))
  finalHeight = float(input("Enter the final height (m): "))
  deltaY = finalHeight - launchHeight

  # solve for velocities
  Vix = Vi * math.cos(math.radians(Angle))
  Viy = Vi * math.sin(math.radians(Angle))

  # quadratic formula
  discriminant = (Viy**2) - (4 * -4.9 * -deltaY)
  if discriminant < 0:
    print("\nThis problem is impossible :(")
    return

  time1 = (-Viy - math.sqrt(discriminant)) / -9.8
  time2 = (-Viy + math.sqrt(discriminant)) / -9.8

  if time1 > time2:
    temp = time1
    time1 = time2
    time2 = temp

  # print the times when the height is finalHeight
  print("\nTimes when height is " + str(finalHeight) + " m: ")
  if time1 >= 0:
    print(str(math.floor(time1 * 10000)/10000) + " seconds")
  if time2 >= 0:
    print(str(math.floor(time2 * 10000)/10000) + " seconds")

  # print the distance the marble will travel when it is at finalHeight
  print("Distances when height is " + str(finalHeight) +" m: ")
  if time1 >= 0:
    print(str(math.floor((time1 * Vix) * 10000)/10000) + " meters")
  if time2 >= 0:
    print(str(math.floor((time2 * Vix) * 10000)/10000) + " meters")

  # print the apex height and the time the projectile is at the apex height
  apexHeight = ((Viy**2 / 19.6) + launchHeight)
  print("\nApex height: " + str(math.floor(apexHeight * 10000) / 10000) + " meters")
  print("Apex height time: "   + str(math.floor(Viy/9.8 * 10000) / 10000) + " seconds")

  #final velocity just before hitting the ground
  print("\nFinal velocity before hitting the ground: \n" + str(math.floor(math.sqrt(Vix**2 + Viy**2) * 10000) / 10000) + " meters/second")

# Ask the user for the type of projectile motion
questionType = input("Which type of projectile motion are you solving for?\n1. Type 1\n2. Type 2\n3. Type 3\n")
print("\n\n")
if questionType == "1":
  type1()
elif questionType == "2":
  type2()
elif questionType == "3":
  type3()
else:
  print("Invalid Input please run the program again...")