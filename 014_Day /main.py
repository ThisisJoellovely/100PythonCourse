# Day 15 Higher or Lower game 
from art import logo
from art import vs
from game_data import data
import random

# Global Variables
user_RoundsWon = 0
random_1 = 0
random_2 = 0
data_Length = len(data)
currentRound = 0 



def welcomeFunction():
    print(logo)
    print("\n")

# Function will return if the round keeps going by iterating or if it stops by making it return -1
def roundFunciton(currentRound):
    random_1 = random.randint(0,data_Length)
    random_1Map = data[random_1]
    random_2 = random.randint(0,data_Length)
    random_2Map = data[random_2]
    print("\n")
    print("Compare A: " + random_1Map['name'] )
    print(vs)
    print("Compare B: " + random_2Map['name'])

    user_Cinput = input("Who has more followers? Type 'A' or 'B': ")
    random_1FollowCount = int(random_1Map['follower_count'])
    random_2FollowCount = int(random_2Map['follower_count'])
    if(user_Cinput == 'A'):
        if(random_1FollowCount > random_2FollowCount):
            currentRound += 1
            print(f"You're right! Current score: {currentRound}.")
            print(f"{random_1Map['name']}, A {random_1Map['description']}, from {random_1Map['country']}")
            return currentRound
        else:
            currentRound = -1
            print(f"You're Wrong! Current score: {currentRound}.")
            return currentRound

    
    elif(user_Cinput == 'B'):
        if(random_1FollowCount < random_2FollowCount):
            currentRound += 1
            print(f"You're right! Current score: {currentRound}.")
            print(f"{random_1Map['name']}, A {random_1Map['description']}, from {random_1Map['country']}")
            return currentRound
        else:
            print(f"\nSorry you're Wrong! Final Score: {currentRound}.")
            currentRound = -1
            return currentRound

    else:
        print("Wrong Input Please try Again!")
        roundFunciton(currentRound)

# Running my Version of the Higher or Lower Game 
welcomeFunction()
while (currentRound != -1):
    currentRound = roundFunciton(currentRound)

    


