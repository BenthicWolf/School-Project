import sys
import json

from random import randint


doubles = [9, 10, 11]


class Person:
    def __init__(self):
        self.Cards = []
        self.Decks = [[], []]
        self.bet = 0
        self.balance = 100
        self.Uname = None
        self.Upass = None
        self.Score = None
        self.sidebet = 0

    def discard_hand(self):
        self.Cards = []
        self.Decks = [[], []]

    def print_deck(self, deck):
        output = ""
        for card in deck[:-1]:
            if card != "":
                output += self.convert(card) + " and the "
        output += self.convert(deck[-1])
        return output

    def split(self):
        self.Decks[0] = [self.Cards[0]]
        self.Decks[1] = [self.Cards[1]]

    def is_over(self):
        print(f"Your current total is: {self.total(self.Cards)}")

        if self.total(self.Cards) > 21:
            return True
        else:
            return False

    def discard_deck(self):
        self.Decks[0] = self.Decks[1]
        self.Decks[1] = []

    def total(self, cards):
        counter = 0
        total = [0]

        for card in cards:
            card -= ((card - 1) // 13) * 13
            if card > 10:
                card = 10

            if card == 1:
                total.append(total[-1])

                for i in total[:-1]:
                    total[counter] += 1
                    counter += 1
                total[-1] += 11
                counter = 0

            else:
                for i in total:
                    total[counter] += card
                    counter += 1
                counter = 0

        for i in total[::-1]:
            if i <= 21:
                return total[total.index(i)]

        return total[0]

    def Deal_Cards(self):
        self.Get_Card(self.Cards)
        self.Get_Card(self.Cards)

    def Get_Card(self, cards):
        cards.append(randint(1, 52))

    def convert(self, card):
        card -= 1
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

        if card // 13 > 0:
            suit = suits[(card // 13)]
        else:
            suit = suits[0]

        card -= (card // 13) * 13
        card += 1

        if card == 1:
            card = "Ace"
        if card == 11:
            card = "Jack"
        if card == 12:
            card = "Queen"
        if card == 13:
            card = "King"

        return str(card) + " of " + suit

    # True means carry on with code, False means the loop repeats
    def userauth(self):
        print("Please login to an authorised user account.\n")
        self.Uname = str(input("Input a valid username here: "))
        self.Upass = str(input("Input a valid password here: "))

        File = open("users.json", "r")
        Valid_Users = json.load(File)

        if self.Uname in Valid_Users.keys() and Valid_Users[
                self.Uname] == self.Upass:
            print("\nSuccessfuly authorised user account\n\n")
            File.close()
            return True
        else:
            print("\nFailure to authorise user account\n\n")
            File.close()
            return False

    # Returns True if face value is the same
    def is_same(self):
        if self.convert(self.Cards[0]).split(" ")[0] == self.convert(
                self.Cards[1]).split(" ")[0]:
            return True
        else:
            return False

    def double_down(self):
        global pOver

        while True:
            self.balance -= self.bet
            self.bet *= 2

            self.Get_Card(self.Cards)
            print(
                f"\nYour new card is: {self.convert(self.Cards[-1])}")

            if self.total(self.Cards) > 21:
                pOver = True
            else:
                pOver = False
            break


# Game class starts


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
                    f"Bet of {bet} added, an equal amount has been  removed from your balance"
                )
                break

    def run(self):
        while not self.main():
            print("\n\nNew Game Launched\n\n")
            self.player.discard_hand()
            self.dealer.discard_hand()

    def new_hand(self):
        pass

    def print_cards(self):
        print(
            f"""\nYour cards are the {self.player.convert(self.player.Cards[0])}, and the {self.player.convert(self.player.Cards[1])}. The dealer's faceup card is the {self.dealer.convert(self.dealer.Cards[0])}"""
        )

    def is_natural(self, player):
        print(f"Your total gives you a natural 21.")
        if self.dealer.total(self.dealer.Cards) == 21:
            print(
                f"The dealer reveals their facedown card as: {self.dealer.convert(self.dealer.Cards[1])}, giving them also a total of 21."
            )
            self.settle(False, False)

        else:
            print(
                f"The dealer reveals their facedown card as: {self.dealer.convert(self.dealer.Cards[1])}, giving them a total of {self.dealer.total(self.dealer.Cards)}."
            )
            print(
                "Your bet has been returned, you have been given a bonus of half your bet."
            )
            player.balance += (player.bet * 1.5)

    # True means player standing, False means player went over
    def Choice(self):
        while True:
            if self.player.Decks[1] == []:
                print("\nDo you want to hit or stand?")
                decision = str(
                    input("Please enter one of the options: ")).lower()

                if decision == "hit":
                    self.player.Get_Card(self.player.Decks[0])
                    print(
                        f"\nYour new card is: {self.player.convert(self.player.Decks[0][-1])}"
                    )
                    print(
                        f"You're new total is: {self.player.total(self.player.Decks[0])}")
                    if self.player.total(self.player.Decks[0]) > 21:
                        print("You're over!")
                        return False
                    else:
                        print("You're not over!")
                elif decision == "stand":
                    return True
                else:
                    print("That isnt an option, please check your spelling\n")
                    continue

            else:
                print("\nDo you want to hit or stand?")
                decision = str(
                    input("Please enter one of the options: ")).lower()

                if decision == "hit":
                    self.player.Get_Card(self.player.Decks[0])
                    print(
                        f"\nYour new card is: the {self.player.convert(self.player.Decks[0][-1])}\n"
                    )
                    print(
                        f"You're new total is: {self.player.total(self.player.Decks[0])}")
                    if self.player.total(self.player.Decks[0]) > 21:
                        print("You're over!")
                        if self.player.Decks[1] != []:
                            print("\nYour first deck has been discarded")
                            self.player.discard_deck()
                        else:
                            return False
                    else:
                        print("You're not over!")
                elif decision == "stand":
                    return True
                else:
                    print("That isnt an option, please check your spelling\n")
                    continue

    def do_insurance(self):
        decision = input(
            "\nThe dealer's faceup card is an ace, do you want to place an insurance bet? Yes or No: ").lower()
        if decision == "no":
            return False
        elif decision == "yes":
            while True:
                print("\nYou can place a side bet that the dealer's facedown card is a ten, up to half the original bet. If it is, your side bet is doubled.")
                bet = int(input(
                    f"You can place a bet up to: {int(self.player.bet/2)}, you have {self.player.balance} available to bet, how much do you want to bet: "))

                if bet > self.player.bet/2 or bet > self.player.balance:
                    print("\nThat is not a valid bet")
                else:
                    self.player.balance -= bet
                    self.player.sidebet = bet
                    break

            if self.dealer.convert(self.dealer.Cards[1]).split(" ")[0] == "10":
                print(
                    f"\nThe dealer reveals their facedown card: the {self.dealer.convert(self.dealer.Cards[1])}.")
                print(
                    "The dealer's total comes to 21. The player wins their insurance bet.")
                self.player.balance += 2*self.player.sidebet
                return "Exit"
            else:
                print("\nThe dealer checks their facedown card, it was not a 10.")
                return True

    # True means the dealer's turn is finished, False means the dealer has gone bust

    def dealer_turn(self):
        dealer = self.dealer
        print(
            f"\nThe dealer reveals their facedown card: {dealer.convert(dealer.Cards[1])}"
        )

        while True:
            total = dealer.total(dealer.Cards)

            print(f"The dealers current total is: {total}")

            if total > 21:
                print("The dealer is bust")
                return False

            elif total >= 17 or total >= self.player.total(self.player.Decks[0]):
                break

            else:
                dealer.Get_Card(dealer.Cards)
                print(
                    f"\nThe dealer takes a card, their new card is the: {dealer.convert(dealer.Cards[-1])}"
                )
                print()

        return True

    def settle(self, pOver, dOver):
        player = self.player
        ptotal = player.total(player.Decks[0])
        dtotal = self.dealer.total(self.dealer.Cards)

        if (dOver or ptotal > dtotal) and not pOver:
            print("Congratulations, you win!")

            File = open("scores.json", "r")
            scores = json.load(File)
            score = scores[player.Uname]
            File.close()

            player.balance += (player.bet) * 2

            if score < player.balance:
                scores[player.Uname] = player.balance

                file = open("scores.json", "w")
                json.dump(scores, file)
                file.close()

                print(
                    f"Your bet has been doubled! Your current balance is: {int(player.balance)}, this beats highest score for this user, which is: {score}! Keep playing if you want to further this record!"
                )

            elif score >= player.balance:
                print(
                    f"Your bet has been doubled! Your current balance is: {int(player.balance)}, however the highest score for this user is: {score}! Keep playing to try to beat this score!"
                )

        elif (not dOver and pOver) or dtotal > ptotal:
            print("You lose!")
            print(
                f"Your balance hasn't been returned, your current balance is: {int(player.balance)}"
            )

        else:
            player.balance += player.bet
            print(
                f"""You have the same total as the dealer, so you draw. Your bet has been returned,
            your current balance is:{int(player.balance)}""")

    def main(self):
        player = self.player
        print(f"Your current balance is: {int(player.balance)}\n")
        game.bet_amount()

        # player.Deal_Cards()
        player.Cards.append(1)
        player.Cards.append(1)
        self.dealer.Deal_Cards()
        self.print_cards()

        if player.total(player.Cards) == 21:
            self.is_natural(player)
            return None

        if self.dealer.convert(self.dealer.Cards[0]).split(" ")[0] == "Ace":
            if self.do_insurance() == "Exit":
                return None
            else:
                pass

        if player.is_same() == True:
            print(
                "\nYour cards are of the same face. If you want, you can split into two decks")
            while True:
                do_split = str(input("Yes or No: ")).lower()
                if do_split == "yes":
                    player.split()
                    print(
                        f"Your deck has been split in two, into: {player.convert(player.Decks[0][0])} and {player.convert(player.Decks[1][0])}")
                    break
                elif do_split == "no":
                    print("\nDeck not split\n")
                    break
                else:
                    print("That is not a valid option")
        else:
            player.Decks[0] = player.Cards

        if player.total(player.Cards) in doubles:
            global pOver
            global dOver

            print(
                f"\nThe player's card total is {player.total(player.Cards)}, this means you can opt to double down. You will receive 1 more card and will double the bet placed.")

            while True:
                decision = str(
                    input("Do you wish to double down? Yes or No: ")).lower()

                if decision == "yes":
                    player.double_down()
                    break

                elif decision == "no":
                    pOver = not self.Choice()
                    break

                else:
                    print("That is not a valid option\n")
        else:
            pOver = not self.Choice()

        if not pOver:
            dOver = not self.dealer_turn()
        else:
            dOver = False

        self.settle(pOver, dOver)

        if player.balance == 0:
            print(
                "You have lost all your money, as such this game instance will end. However, player balances are reset upon log in, but don't let that make you forgot your shame."
            )
            sys.exit()


game = Game()
game.run()
