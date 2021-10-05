from functions import UserAuth, Deal_Cards, Choice, convert


def Main():

    while not UserAuth(): pass

    player = Player()
    dealer = Dealer()

    Deal_Cards(player)
    Deal_Cards(dealer)

    print(f"Your cards are the {convert(player.Cards[0])}, {convert(player.Cards[1])}.\nThe dealer's faceup card is {convert(dealer.Cards[0])}")

    while not Choice(player): pass
    


class Player:
    def __init__(self):
        self.Cards = []


class Dealer:
    def __init__(self):
        self.Cards = []




print("\n\nYou are playing: Blackjack (21)\n")
print(".\n" * 2)

Main()
