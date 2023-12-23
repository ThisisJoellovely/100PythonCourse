from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

user_menu = Menu()
user_MoneyMachine = MoneyMachine()
user_CoffeMaker = CoffeeMaker()
is_on = True 


while (is_on):
    options = user_menu.get_items()
    choice = input(f"What would you like? {options}): ")
    if choice == "off":
        is_on = false
    elif choice == "report":
        user_CoffeMaker.report()
        user_MoneyMachine.report()
    else:
        drink = user_menu.find_drink(choice)
        if user_CoffeMaker.is_resource_sufficient(drink) and user_MoneyMachine.make_payment(drink.cost): user_CoffeMaker.make_coffee(drink)