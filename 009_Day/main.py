import os
from art import logo

print(logo)

# Global Variables
bid_dict = {}  # Dictionary to store bids
max_bid = 0  # Variable to store maximum bid
winner = None  # Variable to store winner, initialized to None

name = input("What is your name? ")
bid_amount = int(input("What is your bid? $"))
bid_dict[name] = bid_amount
user_input = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

if user_input == 'yes':
    while user_input == 'yes':
        name = input("What is your name? ")
        bid_amount = int(input("What is your bid? $"))
        bid_dict[name] = bid_amount
        user_input = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

for key in bid_dict:
    temp = bid_dict[key]
    if temp > max_bid:
        winner = key
        max_bid = temp

if winner is not None:
    print(f"The winner is {winner} with a bid of ${bid_dict[winner]}.")
else:
    print("No bids were received.")
