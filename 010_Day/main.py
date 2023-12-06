# Calculator App for Day 10 of the Python Programming Class
from art import logo


def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return(n1 - n2)

def multiply(n1 , n2):
    return(n1 * n2)

def divide(n1 , n2):
    return(n1 / n2)

Operations ={
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,

}
def calulator():
    print(logo)

    num1 = float(input("What's the first number? :"))
    for key in Operations:
            print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = Operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input("type 'y' to continue calculating with {answer}, or type 'n' to exit.:") == "y":
            num1 = answer
        else:
            should_continue = False
            calulator()

calulator()
            
