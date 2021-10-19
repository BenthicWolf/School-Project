from functions import dealer_turn, userauth, Deal_Cards, Choice, convert, settle


class Person:
    def __init__(self):
        self.Cards = []
        self.bet = 0
        self.balance = 100
        self.name = ""

    def discard_hand(self):
        self.Cards = []
    
    def is_over(self):
        print(f"Your current total is: {self.total()}")

        if self.total() > 21:
            return True
        else:
           return False
    
    def total(self):
        total = 0
        for card in self.Cards:
            card -= ((card-1)//13)*13
            if card > 10:
                card = 10
            total += card
        print(total)
        return total


def main():

    print(player.balance)

    while not userauth(player):
        pass

    Deal_Cards(player)
    Deal_Cards(dealer)

    print(
        f"""Your cards are the {convert(player.Cards[0])}, and the {convert(player.Cards[1])}.
The dealer's faceup card is the {convert(dealer.Cards[0])}""")

    while True:
        bet = int(input("Enter a bet amount: "))

        if bet > player.balance:
            print("That is not a valid bet amount\n")
        else:
            player.bet = bet
            player.balance -= bet
            print(
                f"Bet of {bet} added, an equal amount has been removed from your balance")
            break

    pOver = not Choice(player)
    if not pOver:
        dOver = not dealer_turn(dealer)

    settle(player, dealer, pOver, dOver)



player = Person()
dealer = Person()


print("\n\nYou are playing: Blackjack (21)\n")

while not main():
    print("\n\nNew Game Launched\n\n")
    player.discard_hand()
    dealer.discard_hand()
