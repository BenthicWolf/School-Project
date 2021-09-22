
from random import randint
from functions import *


def Main():

    if UserAuth() == "Succeeded":
        pass
    else:
        Main()


print("\n\nYou are playing: Blackjack (21)\n")
print(".\n"*2)


Main()
