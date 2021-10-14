from functions import dealer_turn, userauth, Deal_Cards, Choice, convert, is_over, settle


def main():

    player = Person()
    dealer = Person()

    while not userauth(player):
        pass

    Deal_Cards(player)
    Deal_Cards(dealer)

    print(
        f"""Your cards are the {convert(player.Cards[0])}, and the {convert(player.Cards[1])}.
The dealer's faceup card is the {convert(dealer.Cards[0])}""")

    bet = int(input("Enter a bet amount: "))

    if bet > player.balance:
        print("That is not a valid bet")
    else:
        player.bet = bet
        player.balance -= bet
        print(
            f"Bet of {bet} added, an equal amount has been removed from your balance")

    while not Choice(player):
        if is_over(player) == True:
            print("You're over!")
            return False
        else:
            print("You're not over!")

    if dealer_turn(dealer) == False:
        return False

    settle(player, dealer)


class Person:
    def __init__(self):
        self.Cards = []
        self.bet = 0
        self.balance = 100
        self.name = ""


print("\n\nYou are playing: Blackjack (21)\n")

while not main():
    print("\n\nNew Game Launched\n\n")
