# Day 11 100 Days of Python Programming Project
# Project: Blackjack

# Import Statements
from art import logo
import random

# Variables Used 
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # for all the cards available 
gameLogic = True

# This function will create a random array of size two that will link to a specfic card feom the card array 
def randomGenerator ():
    randomInt_1 = random.randint(1,13)
    randomInt_2 = random.randint(1,13)
    randomArray = [cards[randomInt_1],cards[randomInt_2]]
    return randomArray

def anotherCardGenerator():
    randomInt = random.randint(1,13)
    return cards[randomInt]

# This function will create a summation of all variables from the list 
def sumGenerator (tempArray):
    sum = 0
    for element in tempArray:
        sum += element
    return sum

# This function will check if the user or computer has a blackjack
def blackJackChecker(userTempArray, computerTempArray):
    sum = 0
    
    for element in userTempArray:
        sum += element
    if sum == 21:
        return 1
    
    sum = 0

    for element in computerTempArray:
        sum += element
    if sum == 21:
        return 2
    
    if sum != 21:
        return 0
    
    
# This function will check if the cards provided has an ACE
def AceChecker (tempArray):
    return 11 in tempArray

def comparisonChecker (userSum , computerSum):
    if userSum > computerSum:
        return 1
    if computerSum > userSum:
        return 2
    if computerSum == userSum:
        return 3
    else :
        return 0
    
user_Cards = randomGenerator() 
computer_Cards = randomGenerator()
user_SumCards = sumGenerator(user_Cards)
computer_SumCards = sumGenerator(computer_Cards) 

# Flow chart number 0: Do you want to play the game?
if(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y"):
    print(logo) # Flow chart number 0 - ouptput
    while gameLogic == True:
        
            print(f" Your cards: {user_Cards}, current score: {user_SumCards}")
            print(f" Computer - Your cards: {computer_Cards}, current score: {computer_SumCards}")

            # Flow chart statment number 1: Does the user or computer have a blackjack?
            if(blackJackChecker(user_Cards , computer_Cards) == 0):
                # Flow chart statment number 2: Is the user over the number 21
                if user_SumCards > 21:
                    if(AceChecker(user_Cards) == False): 
                        print("You have gotten beaten, Computer WINS 😭") # Flow chart number 2 - output
                        gameLogic = False
                    if(AceChecker(user_Cards) == True):
                        user_index = user_Cards.index(11)
                        user_Cards[user_index] = 1
                        user_SumCards = sumGenerator[user_Cards]
                        if(user_SumCards > 21): 
                            print("You have gotten beaten, Computer WINS 😭") # Flow chart number 2 - output
                            gameLogic = False 
                # Flow chart statement number 3: Does the user want another card?
                user_anotherCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if(user_anotherCard == 'y'):
                    user_Cards.append(anotherCardGenerator()) 
                    user_SumCards = sumGenerator(user_Cards)
                    continue # Flow chart number 3 - output
                elif (user_anotherCard == 'n'):
                    if computer_SumCards <= 17:
                        computer_Cards.append(anotherCardGenerator())  # Flow chart number 3 - output
                        computer_SumCards = sumGenerator(computer_Cards)

                    # Flow Chart number 4: Has the computer went over 21? 
                    if computer_SumCards > 21: 
                        print("You have beat the computer, User WINS! 🏆") # Flow chart number 4 - output
                        gameLogic = False 
                    else:
                        if(comparisonChecker(user_SumCards , computer_SumCards) == 1): # Flow chart number 4 - output
                            print("You have beat the computer, User WINS! 🏆")
                            gameLogic = False
                        if(comparisonChecker(user_SumCards , computer_SumCards) == 2): # Flow chart number 4 - output
                            print("You have gotten beaten, Computer WINS 😭")
                            gameLogic = False
                        if(comparisonChecker(user_SumCards , computer_SumCards) == 3): # Flow chart number 4 - output
                            print("DRAW --- 😘")
                            gameLogic = False 
                        if(comparisonChecker(user_SumCards , computer_SumCards) == 0): # Flow chart number 4 - output
                            print("Something went wrong: ERROR")
                            gameLogic = False
                else:
                    print("Invalid Response!")
                                
            elif blackJackChecker(user_Cards, computer_Cards) == 1:
                print("You have gotten a Black-Jack, You WIN! 🏆")  # Flow chart number 1 - output
                gameLogic = False 

            elif blackJackChecker(user_Cards, computer_Cards) == 2:
                print("Sorry, the computer has gotten a Black-Jack, You Lose! 😭") # Flow chart number 2 - output
                gameLogic = False
    gameLogic = False
else:
    print("Thank you for playing!")  # Flow chart number 0 - output


    


