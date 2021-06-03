import os

from art import logo

print(logo)

clear = lambda: os.system('cls')

dict = {}
max_bid = 0
bid_is_finished = False

while bid_is_finished == False:
    name = input("What's your name? ")
    bid = int(input("How much do you bid? "))
    dict[name] = bid
    next = input("finish or continue? ")

    if next == "finish":
        bid_is_finished = True
        print(dict)
    else:
        bid_is_finished = False
        clear()


def find_highest(bids):
    highest = 0
    winner = ""
    for name in bids:
        # bid=bids[name]
        if bids[name] > highest:
            highest = bids[name]
            winner = name
    print(winner, highest)


find_highest(dict)
