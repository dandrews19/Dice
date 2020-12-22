# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Lab 11

import random

# creates a class to describe a dice, based on the inut of the user for the number of sides, and stores the amount of
# sides and what the dice rolled
class Die(object):

    # assigns the dice a number of sides based on input and initializes roll value to 0
    def __init__(self, numSides = 6):
        self.sides = numSides
        self.rollValue = 0

    # simulates dice rolling by picking a random number between 1 and the amount of sides user wants on the dice
    def roll(self, numSides = 6):
        number = random.randrange(1, (int(numSides) + 1))
        self.rollValue = number
        return self.rollValue

    # displays the number of sides of the dice and what it rolled, stores it into a message and returns it
    def __str__(self):
        msg = "Die has " + str(self.sides) + " sides and rolled a " + str(self.rollValue)
        return msg

# calculates the sum of the two die that were rolled and prints it
def calculateSum(die1, die2):

    print("The sum of Dice 1 and Dice 2 is", (die1 + die2))

# gets user input on how many sides they want (defaults to 6), how many times they want to roll the die, and prints
# out the results of all the rolls
def main():
    sides1 = input("Use the default number of sides for first die (y/n)? ")
    sides1 = sides1.strip()
    totalSides1 = 6
    totalSides2 = 6
    while sides1 != "Y" and sides1 != "y" and sides1 != "N" and sides1 != "n":
        sides1 = input("Use the default number of sides for first die (y/n)? ")
    if sides1 == "N" or sides1 == "n":
        totalSides1 = input("How many sides? ")
        while totalSides1.isdigit() == False:
            totalSides1 = input("How many sides? ")
    sides2 = input("Use the default number of sides for second die (y/n)? ")
    sides2 = sides2.strip()
    while sides2 != "Y" and sides2 != "y" and sides2 != "N" and sides2 != "n":
        sides2 = input("Use the default number of sides for second die (y/n)? ")
    if sides2 == "N" or sides2 == "n":
        totalSides2 = input("How many sides? ")
        while totalSides2.isdigit() == False:
            totalSides2 = input("How many sides? ")
    numRolls = input("How many times do you want to roll the die? ")
    while numRolls.isdigit() == False:
        numRolls = input("How many times do you want to roll the die? ")
    i = 0
    while i < int(numRolls):
        die1 = Die(numSides= int(totalSides1))
        die2 = Die(numSides= int(totalSides2))
        die1Roll = die1.roll(int(totalSides1))
        die2Roll = die2.roll(int(totalSides2))
        print(die1)
        print(die2)
        calculateSum(die1= int(die1Roll), die2= int(die2Roll))
        i += 1


main()
