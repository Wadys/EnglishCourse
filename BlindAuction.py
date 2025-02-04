# Requirements:
# Create a program that simulates Blind Auction. 
# [https://en.wikipedia.org/wiki/First-price_sealed-bid_auction] 

# 1. Print Logo - Blind Auction
# 2. Ask user name
# 3. Input Bid
# 4. If there is another user, type YES, then the program asks for next bidder by cleaning everything from console
# 5. Finally, If there is not another bidder return the highest bidder with bid amount

# Sample Output:
# LOGO                                                                                        
# What is your name?: Elshad
# What is your bid amount?: $100
# Are there any other bidder?(Y/N)Y
# ---clear---
# What is your name?: Jane
# What is your bid amount?: $120
# Are there any other bidder?(Y/N)NLo
# The winner is Jane with a bid of $120
# Hint
# Create dictionary for bidder and their bid.


# Define Dictionary
blind_bid = dict() 
#     name,bid
# Print Logo
from AsciiArt import blindauction_logo as logo
from os import system as s

print(logo)
# Loop
next_user = "Y"
while next_user == "Y":
#Ask user Name
    user = input("What is your name? > ")
#Input Bid
    bid = input("What is your bid amount? > ")
#Upade Dictionary
    blind_bid[user] = int(bid)
# Ask if there is another user
    next_user = input("Is there another bidder (Y/N)> ").capitalize()
#     Clear Screan
    s('cls')
# Print Highest Bid
highest_user = ""
highest_value = -1
for key, value in blind_bid.items():
    if value > highest_value:
        highest_user = key
        highest_value = blind_bid[key]
print(f"The winner is {highest_user} with a bid of ${highest_value}")
print(blind_bid)