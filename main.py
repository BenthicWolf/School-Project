import sys

from random import randint
from functions import dealer_turn, userauth, Choice, convert, settle


class Person:
    def __init__(self):
        self.Cards = []
        self.bet = 0
        self.balance = 100
        self.Uname = None
        self.Upass = None

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
    
    def Deal_Cards(self):
        self.Cards.append(randint(1, 52))
        self.Cards.append(randint(1, 52))


def main():

    if player.Uname is None:
        while not userauth(player):
            pass

    player.Deal_Cards()
    dealer.Deal_Cards()

    print(
        f"""Your cards are the {convert(player.Cards[0])}, and the {convert(player.Cards[1])}.
The dealer's faceup card is the {convert(dealer.Cards[0])}""")
    print(f"Your current balance is: {player.balance}")

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
    else:
        dOver = False

    settle(player, dealer, pOver, dOver)

    if player.balance == 0:
        print("You have lost all your money, as such this game instance will end. However, player balances are reset upon log in, but don't let that make you forgot your shame.")
        sys.exit()



player = Person()
dealer = Person()


print("\n\nYou are playing: Blackjack (21)\n")

while not main():
    print("\n\nNew Game Launched\n\n")
    player.discard_hand()
    dealer.discard_hand()
