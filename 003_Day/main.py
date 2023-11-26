print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
userInput_leftOrright = input("Left or Right? ")

if(userInput_leftOrright == "Right"):
    print("Fall into a hole. Game Over.")

elif(userInput_leftOrright == "Left"):
    userInput_swimOrWait = input("swim or wait ")

    if(userInput_swimOrWait == "swim" or userInput_swimOrWait != "wait"):
        print("attacked by trout. Game Over.")
    
    elif(userInput_swimOrWait == "wait"):
        userInput_redOrBlueOryellow = input("Which door? (color) ")
            
        if(userInput_redOrBlueOryellow == "Red"):
            print("Burned by fire. Game Over.")
        elif(userInput_redOrBlueOryellow == "Blue"):
            print("Eaten by beasts. Game Over.")
        elif(userInput_redOrBlueOryellow == "Yellow"):
            print("You Win!")
        else:
            print("Game Over!")
    



else:
    print("Invalid Input. Please try again by restarting the program.")



