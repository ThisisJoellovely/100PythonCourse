MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

report = {
    "resources" : {
        "Water": 300,
        "Milk": 200,
        "Coffee": 100,
    },
    "report" : {
        "Money" : 0
    }
}


# Global Variables 
coffee_State = 0

### Returns a integer value that will be used to check what procedure to follow 
def WelcomePrompt():
    UserInput = input("What would you like? (espresso/latte/cappuccino):")

    coffee_State = 0
    if (UserInput == "espresso" or UserInput == "Espresso"):
        coffee_State = 1
        return coffee_State
    elif (UserInput == "latte" or UserInput == "Latte"):
        coffee_State = 2
        return coffee_State
    elif (UserInput == "cappuccino" or UserInput == "Cappuccino"):
        coffee_State = 3
        return coffee_State
    elif (UserInput == "report" or UserInput == "Report"):
        coffee_State = 4
        return coffee_State
    elif (UserInput == "off" or UserInput == "Off"):
        coffee_State = -1
        return coffee_State
    else:
        return coffee_State
    
def PrintReport():
    reportKey = report["resources"]
    for key , value in reportKey:
        if (key == "Water" or key == "Milk"):
            print(f"{key}: {value}ml")
        elif (key == "Coffee"):
            print(f"{key}: {value}g")    
    for key , value in report["report"]:
        print(f"{key}: ${value}")


def CheckResources(coffee_State):

    if(coffee_State == 1):
        UserInput = MENU["espresso"]
    elif(coffee_State == 2):
        UserInput = MENU["latte"]
    elif(coffee_State == 3):
        UserInput = MENU["cappuccino"]
    else:
        print("Invalid Response")
        return -1

    UserInput_Ingredients = UserInput["ingredients"]

    for key , value in report["resources"]:
        if(UserInput_Ingredients[key] < value):
            continue
        else:
            print(f"Sorry there is not enough {key}")
            return -1
        
#def ProcessCoins():

    
#What the coffee machine will do based on the inputs given from the user
while (coffee_State != -1):
    coffee_State = WelcomePrompt()
    if(coffee_State == 0):
        print("Wrong input, please try again!")
        continue
    elif(coffee_State == 4):
        PrintReport()
        continue
    elif(coffee_State == 1 or coffee_State == 2 or coffee_State == 3):
       if (CheckResources(coffee_State) != -1):
           continue
       else: 
           continue
    continue

print("Closed due to maintenance. Sorry for the inconvenience")






