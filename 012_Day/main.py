#Number Guessing Game Objectives:
from art import logo 
import random 

# Globabl Variable
randomNumber_variable = 0
movesRemaining = 0
gameLogic = True



def randomNumberFunction(): 
    randomNumber_variable = random.randint(1,100)
    return randomNumber_variable


def introPrintStatement(variable):
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    user_difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
    return user_difficulty

while (gameLogic == True):
    randomNumber_variable = randomNumberFunction() 
    print(logo)

    
    while(True):
        user_difficulty = introPrintStatement(randomNumber_variable)
        if(user_difficulty == "easy"):
            movesRemaining = 10
            break
        if(user_difficulty == "hard"):
            movesRemaining = 5
            break
        else:
            print("Invalid Input. Please try again!\n")
            continue

    while(movesRemaining != 0):
        userInput_answerString = input(f"You have {movesRemaining} attempts remaining to guess the number. ")
        userInput_answerInt = int(userInput_answerString)
        if userInput_answerInt > randomNumber_variable:
            print("\nToo high!\n")
            movesRemaining -= 1
        elif userInput_answerInt < randomNumber_variable:
            print("\nToo low.\n")
            movesRemaining -= 1    
        elif userInput_answerInt == randomNumber_variable:
            print(f"You got it! The answer was {randomNumber_variable}.")
            user_playAgain = input("Do you want to play again? type 'y' to play again or 'n' exit the program! ").lower()
            break
    if (movesRemaining == 0):
        user_playAgain = input("Better Luck NEXT TIME! Do you want to play again? type 'y' to play again or 'n' exit the program! ").lower()
    if (user_playAgain == 'y'):
        continue
    else:
        break
        
    


