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
        self.Get_Card()
        self.Get_Card()

    def Get_Card(self):
        self.Cards.append(randint(1, 52))

class Game:
    def __init__(self):
        self.player = Person()
        self.dealer = Person()

        print("\n\nYou are playing: Blackjack (21)\n")

        if self.player.Uname is None:
         while not userauth(self.player):
                pass
        
        self.player.Deal_Cards()
        self.dealer.Deal_Cards()
    
    def bet_amount(self):
        while True:
            bet = int(input("Enter a bet amount: "))

            if bet > self.player.balance:
                print("That is not a valid bet amount\n")
            else:
                self.player.bet = bet
                self.player.balance -= bet
                print(
                    f"Bet of {bet} added, an equal amount has been  removed from your balance")
                break
    
    def run(self):
        while not self.main():
            print("\n\nNew Game Launched\n\n")
            self.player.discard_hand()
            self.dealer.discard_hand()

    def print_cards(self):
        print(f"""Your cards are the {convert(self.player.Cards[0])}, and the {convert(self.player.Cards[1])}.
    The dealer's faceup card is the {convert(self.dealer.Cards[0])}""")
        print(f"Your current balance is: {self.player.balance}")

    def main(self):

        self.print_cards()

        game.bet_amount()

        pOver = not Choice(self.player)
        if not pOver:
            dOver = not dealer_turn(self.dealer)
        else:
            dOver = False

        settle(self.player, self.dealer, pOver, dOver)

        if game.player.balance == 0:
            print("You have lost all your money, as such this game instance will end. However, player balances are reset upon log in, but don't let that make you forgot your shame.")
            sys.exit()


game = Game()
game.run()

