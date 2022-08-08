"""

Filename: version2.py
Author: Lisa
Date: July 2022
Description: This is a programme to test out a mystery prize box feature for a game company

"""
                     
import random

#description: takes parameters of a list and a string (prize) and adds the prize to the list
def prizes(a_list, different_prizes):
        print("The prize you've got is... {}!".format(different_prizes))
        a_list.append(different_prizes)
        return a_list
    
#Lists of prizes for different mystery boxes
FIFTY_COINS_PRIZES = ["10 coins", "20 coins", "35 coins", "80 coins", "100 coins",
               "5 gems", "10 gems", "20 gems", "Axe (level 1 weapon)",
               "Wooden Club (level 1 weapon)", "Panda skin", "Dinosaur skin",
               "Zebra skin", "Giraffe skin", "1 extra life"]
ONE_HUNDRED_COINS_PRIZES = ["80 coins", "150 coins", "200 coins", "15 gems", "25 gems",
                     "30 gems", "Gun (level 2 weapon)", "Electric stick (level 2 weapon)",
                     "Rifle (level 3 weapon)", "Bomb (level 3 weapon)", "Robot skin",
                     "Alien skin", "Fairy skin", "2 extra lives", "3 extra lives"]
TWO_HUNDRED_COINS_PRIZES = ["165 coins", "300 coins", "45 gems", "80 gems",
                     "Crossbow (level 2 weapon)", "Bomb (level 3 weapon)",
                     "Claws (level 3 weapon)", "Longspear (Level 3 weapon)",
                     "Wings (Special equipment)", "Speed booster (Special equipment)",
                     "Monster Bear skin", "Hunter skin", "Soldier skin", "3 extra lives",
                     "5 extra lives"]

#Lists of valid answers
VALID_PRICES = ["50", "100", "200"]
VALID_CHOICES = ["y", "yes", "n", "no"]
#Storing for print out message at the end
user_prizes = []
coins_spent = 0

#Intro
print("""
Welcome to the MYSTERY PRIZE BOX!

Here you have the chance to get ALL game equipment you want
Weapons, skins, gems, lives, coins... We have it all!

There are 3 different priced mystery boxes:
50 coins
100 coins
200 coins

The more the mystery box costs, the better the prizes are!
""")

valid = True

while valid:
    
    #Repeating question until answer is valid
    user_choice = input("What priced mystery box would you like to buy (50/100/200): $")
    while not (user_choice.strip() in VALID_PRICES):
        print("You did not enter a valid price...Please try again")
        user_choice = input("What priced mystery box would you like to buy (50/100/200): $")
        
  
    #Generate random prize from lists
    if user_choice.strip() == "50":
        user_prizes = prizes(user_prizes, random.choice(FIFTY_COINS_PRIZES))
        coins_spent += 50
 
    elif user_choice.strip() == "100":
        user_prizes = prizes(user_prizes, random.choice(ONE_HUNDRED_COINS_PRIZES))
        coins_spent += 100

    elif user_choice.strip() == "200":
        user_prizes = prizes(user_prizes, random.choice(TWO_HUNDRED_COINS_PRIZES))
        coins_spent += 200

    #Repeating question until answer is valid
    #Another one or no
    another_one = input("Would you like to buy another mystery box? (y/n): ")
    while not (another_one.strip().lower() in VALID_CHOICES):
        print("You did not enter a valid choice...Please try again")
        another_one = input("Would you like to buy another mystery box? (y/n): ")

    if another_one.strip().lower() == "n" or another_one.strip().lower() == "no":
        valid = False
        
print("""
The prizes you've won today are {}! CONGRATULATIONS
You have spent {} coins """.format(', '.join(user_prizes), coins_spent))
