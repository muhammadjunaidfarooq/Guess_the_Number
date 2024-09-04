# Program to generate random number & compare it with user input

import random

target = random.randint(1, 10)

while True:
    try: 
        userChoice = input("Guess the target or Quit(q): ").lower()
        if userChoice == "q":
            break
        userChoice = int(userChoice)  
        if (userChoice == target):
            print("Success : Correct Guess!!.")
            break
        elif (userChoice < target):
            print("Your number is too small. Taker a bigger number..")
        else:
            print("Your number is too bigger. Taker a smaller number..")
        
    except ValueError:
        print("ERROR: Please enter a numeric value!")

print("---GAME OVER---")

print(f"Computer Choice {target}")