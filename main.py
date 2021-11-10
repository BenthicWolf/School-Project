import sys
import json

from random import randint


class Person:
    def __init__(self):
        self.Cards = []
        self.bet = 0
        self.balance = 100
        self.Uname = None
        self.Upass = None
        self.Score = None

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
        return total

    def Deal_Cards(self):
        self.Get_Card()
        self.Get_Card()

    def Get_Card(self):
        self.Cards.append(randint(1, 52))

    def convert(self, card):
        card -= 1
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

        if card // 13 > 0:
            suit = suits[(card//13)]
        else:
            suit = suits[0]

        card -= (card//13)*13
        card += 1

        if card == 1:
            card = "Ace"
        if card == 11:
            card = "Jack"
        if card == 12:
            card = "Queen"
        if card == 13:
            card = "King"

        return str(card)+" of "+suit

    # True means carry on with code, False means the loop repeats
    def userauth(self):
        print("Please login to an authorised user account.\n")
        self.Uname = str(input("Input a valid username here: "))
        self.Upass = str(input("Input a valid password here: "))

        File = open("users.json", "r")
        Valid_Users = json.load(File)

        if self.Uname in Valid_Users.keys() and Valid_Users[self.Uname] == self.Upass:
            print("\nSuccessfuly authorised user account\n\n")
            File.close()
            return True
        else:
            print("\nFailure to authorise user account\n\n")
            File.close()
            return False
    


class Game:
    def __init__(self):
        self.dealer = Person()
        self.player = Person()

        print("\n\nYou are playing: Blackjack (21)\n")

        if self.player.Uname is None:
            while not self.player.userauth():
                pass

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
        print(f"""Your cards are the {self.player.convert(self.player.Cards[0])}, and the {self.player.convert(self.player.Cards[1])}.
    The dealer's faceup card is the {self.dealer.convert(self.dealer.Cards[0])}""")
        print(f"Your current balance is: {self.player.balance}")

    def main(self):
        game.bet_amount()

        self.player.Deal_Cards()
        self.dealer.Deal_Cards()
        self.print_cards()

        #make this a seperate function + thing above
        if self.player.total() == 21:
            print(f"Your total gives you a natural 21.")
            if self.dealer.total() == 21:
                print(f"The dealer reveals their facedown card as: {self.dealer.Cards[1]}, giving them also a total of 21.")
                self.settle(False, False)
                break
                #return True or False idk which
            else:
                print(f"The dealer reveals their facedown card as: {self.dealer.Cards[1]}, giving them a total of {self.dealer.total()}.")

        pOver = not self.Choice()
        if not pOver:
            dOver = not self.dealer_turn()
        else:
            dOver = False

        self.settle(pOver, dOver)

        if game.player.balance == 0:
            print("You have lost all your money, as such this game instance will end. However, player balances are reset upon log in, but don't let that make you forgot your shame.")
            sys.exit()

    # True means player standing, False means player went over
    def Choice(self):
        while True:
            print("\nDo you want to hit or stand?")
            decision = str(input("Please enter one of the options: ")).lower()

            if decision == "hit":
                self.player.Get_Card()
                print(
                    f"\nYour new card is: {self.player.convert(self.player.Cards[-1])}")
                print(f"You're new total is: {self.player.total()}")
                if self.player.total() > 21:
                    print("You're over!")
                    return False
                else:
                    print("You're not over!")
            elif decision == "stand":
                break
            else:
                print("That isnt an option, please check your spelling\n")
                continue
        return True

    # True means the dealer's turn is finished, False means the dealer has gone bust
    def dealer_turn(self):
        dealer = self.dealer
        print(
            f"\nThe dealer reveals their facedown card: {dealer.convert(dealer.Cards[1])}")

        while True:
            total = dealer.total()

            print(f"The dealers current total is: {total}")

            if total > 21:
                print("The dealer is bust")
                return False

            elif total >= 17:
                break

            else:
                dealer.Get_Card()
                print(
                    f"\nThe dealer takes a card, their new card is the: {dealer.convert(dealer.Cards[-1])}")
                print()

        return True

    def settle(self, pOver, dOver):
        player = self.player
        ptotal = player.total()
        dtotal = self.dealer.total()

        if (dOver or ptotal > dtotal) and not pOver:
            print("Congratulations, you win!")

            File = open("scores.json", "r")
            scores = json.load(File)
            score = scores[player.Uname]
            File.close()

            player.balance += (player.bet)*2

            file = open("scores.json", "w")

            if score < player.balance:
                scores[player.Uname] = player.balance
                json.dump(scores, file)
                file.close()
                print(
                    f"Your bet has been doubled! Your current balance is: {player.balance}, this beats highest score for this user, which is: {score}! Keep playing if you want to further this record!")

            elif score >= player.balance:
                file.close()
                print(
                    f"Your bet has been doubled! Your current balance is: {player.balance}, however the highest score for this user is: {score}! Keep playing to try to beat this score!")

        elif (not dOver and pOver) or dtotal > ptotal:
            print("You lose!")
            print(
                f"Your balance hasn't been returned, your current balance is: {player.balance}")

        else:
            player.balance += player.bet
            print(f"""You have the same total as the dealer, so you draw. Your bet has been returned,
            your current balance is:{player.balance}""")


game = Game()
game.run()
