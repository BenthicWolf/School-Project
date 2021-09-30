from functions import *


def Main():

    result = UserAuth()
    if result == True:
        pass
    else:
        UserAuth()

    Deal_Cards(player)
    
    



class player():
    def __init__(self, Card1, Card2):
        self.Card1 = 0
        self.Card2 = 0


print("\n\nYou are playing: Blackjack (21)\n")
print(".\n" * 2)

Main()
