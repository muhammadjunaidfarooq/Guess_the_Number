# Program to generate random number & compare it with user input

import random

target = random.randint(1, 5)

while True:
    userChoice = input("Guess the target or Quit(q): ").lower()
    if userChoice == "q":
        break
    userChoice = int(userChoice)  
    if (userChoice == target):
        print("Success : Correct Guess!!.")
        break
    elif (userChoice < target):
        print("Your number is too small. Taker a bigger bigger..")
    else:
        print("Your number is too bigger. Taker a smaller bigger..")

print("---GAME OVER---")

print(target)