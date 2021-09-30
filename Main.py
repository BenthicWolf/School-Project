
from random import choice
from functions import *
from Converter import convert


def Main():

    while True:
        if UserAuth() == False:
            pass
        else:
            break

    Deal_Cards(Player)
    Deal_Cards(Dealer)

    print(f"Your cards are the {convert(Player.Card1)}")

    while True:
        if Choice() == False:
            pass
        else:
            break


class Player:
    def __init__(self, Card1, Card2):
        Card1 = 0
        Card2 = 0


class Dealer:
    def __init__(self, Card1, Card2):
        Card1 = 0
        Card2 = 0


print("\n\nYou are playing: Blackjack (21)\n")
print(".\n"*2)

Main()
