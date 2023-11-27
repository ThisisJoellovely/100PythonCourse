import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
userInput =  int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
gameLogic = True
win_List = [[1,0],[0,2],[2,1]]
random_Computer_Input = random.randint(0,2)
check_List = [userInput,random_Computer_Input]


print("User chose:")
if(userInput == 0):
    print(rock)
if(userInput == 1):
    print(paper)
if(userInput == 2):
    print(scissors)

print("Computer chose:")
if(random_Computer_Input == 0):
    print(rock)
if(random_Computer_Input == 1):
    print(paper)
if(random_Computer_Input == 2):
    print(scissors)



if(check_List[0] == win_List[0][0] and check_List[1] == win_List[0][1]):
    print("User Won This Round")
elif(check_List[0] == win_List[1][0] and check_List[1] == win_List[1][1]):
    print("User Won This Round")
elif(check_List[0] == win_List[2][0] and check_List[1] == win_List[2][1]):
    print("User Won This Round")
else:
    print("Computer Won This Round")









