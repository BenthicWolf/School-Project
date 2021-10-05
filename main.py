from functions import dealer_turn, userauth, Deal_Cards, Choice, convert, is_over


def main():

    while not userauth():
        pass

    player = Person()
    dealer = Person()

    Deal_Cards(player)
    Deal_Cards(dealer)

    print(
        f"""Your cards are the {convert(player.Cards[0])}, and the {convert(player.Cards[1])}.
The dealer's faceup card is the {convert(dealer.Cards[0])}""")

    while not Choice(player):
        if is_over(player) == True:
            print("You're over!")
        else:
            print("You're not over!")

    dealer_turn(dealer)


class Person:
    def __init__(self):
        self.Cards = []


print("\n\nYou are playing: Blackjack (21)\n")

main()
