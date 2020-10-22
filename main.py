import os
import random

# Clears the terminal screen, and displays a title bar.
def displayTitleBar():
    os.system("clear")
    print("------- Match engine simulator -------\n")

# Simulates a match between two teams and displays the result
def playMatch(firstTeam, secondTeam):
    a = int(input("\n" + firstTeam + " level: "))
    b = int(input(secondTeam + " level: "))
    c = random.randint(0, a + b)
    print("random", c)
    if c > a:
        print("\n" + secondTeam + " won")
    else:
        print("\n" + firstTeam + " won")
    
# Displays the available list of commands/actions
def printCommands():
    print("Available commands:")
    print("[1] Play match")
    print("[2] Change team names")
    print("[q] Quit program\n")


# MAIN PROGRAM
command = ""
firstTeam = "First team"
secondTeam = "Second team"
while command != "q":
    displayTitleBar()
    printCommands()
    
    command = input("Please input command: ")

    if command == '1':
        playMatch(firstTeam, secondTeam)
    elif command == '2':
        firstTeam = input("First team name: ")
        secondTeam = input("Second team name: ")
    elif command == "q":
        displayTitleBar()
        print("Program closed")
    else:
        print("Command unknown")
    input("\nPress ENTER button to continue...")