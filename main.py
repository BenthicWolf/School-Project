import sys
import json

from random import randint

# This is a list of values that would allow for doubling-down.
doubles = [9, 10, 11]

# This is the class that contains player variables and functions that only act on 1 player.any
class Person:
    
    # This declares all the variables permanently used.
    def __init__(self):
        self.Cards = []
        self.Decks = [[], []]
        self.bet = 0
        self.balance = 100
        self.Uname = None
        self.Upass = None
        self.Score = None
        self.sidebet = 0

    # This discards a player's hand/s.
    def discard_hand(self):
        self.Cards = []
        self.Decks = [[], []]

    # This prints an entire deck of cards as text.
    def print_deck(self, deck):
        output = ""

        for card in deck[:-1]:
            if card != "":
                output += self.convert(card) + " and the "
        output += self.convert(deck[-1])

        return output

    # This splits a single hand with 2 aces into two hands.
    def split(self):
        self.Decks[0] = [self.Cards[0]]
        self.Decks[1] = [self.Cards[1]]

    # This checks if a player is over 21.
    def is_over(self):
        print(f"Your current total is: {self.total(self.Cards)}")

        if self.total(self.Cards) > 21:
            return True

        else:
            return False

    # This discards all cards in a hands
    def discard_deck(self):
        self.Decks[0] = self.Decks[1]
        self.Decks[1] = []

    # Returns the highest value of a given deck under 22, unless the value is absolutely over 21, where it then gives the lowest value over 22. This returns the total value of a deck of cards.
    def total(self, cards):
        counter = 0
        total = [0]

        # This for loop runs through and sums all card values
        for card in cards:
            # This removes as many 13's as possible without reaching 0, in order to find the card value
            card = card-1 % 13
            # All picture cards become 10
            if card > 10:
                card = 10

            # This deals with aces either being 1 or 11 by adding a value of a list where 11 has been
            # added, while all previous values are added by 1. 
            # This means you obtain an ordered list of 
            # all possible values from smallest to biggest
            if card == 1:
                total.append(total[-1])
  
                for i in total[:-1]:
                    total[counter] += 1
                    counter += 1
                total[-1] += 11
                counter = 0

            # This adds the card value to each possible total value
            else:
                for i in total:
                    total[counter] += card
                    counter += 1
                counter = 0

        # This runs through the list of possible values backwards (largest->smallest)
        # and returns the greatest value < 22.
        for i in total[::-1]:
            if i <= 21:
                return total[total.index(i)]

        # If all values are over 21, the lowest total is returned
        return total[0]

    # This deals 2 cards to a player at the start of the game.
    def Deal_Cards(self):
        self.Get_Card(self.Cards)
        self.Get_Card(self.Cards)

    # This adds a card (number) to a list of numbers (a hand).
    def Get_Card(self, cards):
        cards.append(randint(1, 52))

    # This takes a card (number) input and outputs the corresponding card out of 52.
    def convert(self, card):
        card -= 1
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

        if card // 13 > 0:
            suit = suits[(card // 13)]

        else:
            suit = suits[0]

        card = card % 13
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

    # True means carry on with code, False means the loop repeats. This handles the user login.
    def userauth(self):
        print("Please login to an authorised user account.\n")
        self.Uname = str(input("Input a valid username here: "))
        self.Upass = str(input("Input a valid password here: "))

        # Opens external file users.json and writes it to a function "Valid_Users"
        File = open("users.json", "r")
        Valid_Users = json.load(File)

        # Checks if the username and password match a pair in users.json
        if self.Uname in Valid_Users.keys() and Valid_Users[
                self.Uname] == self.Upass:
            print("\nSuccessfuly authorised user account\n\n")
            File.close()
            return True

        else:
            print("\nFailure to authorise user account\n\n")
            File.close()
            return False

    # Returns True if face value is the same. This checks whether or not a player's two first cards are equal in value.
    def is_same(self):
        if self.convert(self.Cards[0]).split(" ")[0] == self.convert(
                self.Cards[1]).split(" ")[0]:
            return True

        else:
            return False

    # This handles if the player wants to double down.
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




# This is the Game class and contains functions and variables relative to the game.
class Game:

    # This declares all the variables permanently used.
    def __init__(self):
        self.dealer = Person()
        self.player = Person()

        print("\n\nYou are playing: Blackjack (21)\n")

        if self.player.Uname is None:
            while not self.player.userauth():
                pass
    
    # This asks the user how much they want to bet.
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

    # This runs the main function and resets the player's hands.
    def run(self):
        while not self.main():
            print("\n\nNew Game Launched\n\n")
            self.player.discard_hand()
            self.dealer.discard_hand()

    # This prints all faceups cards at the beginning of the game.
    def print_cards(self):
        print(
            f"""\nYour cards are the {self.player.convert(self.player.Cards[0])}, and the {self.player.convert(self.player.Cards[1])}. The dealer's faceup card is the {self.dealer.convert(self.dealer.Cards[0])}"""
        )

    # This handles if the player has a natural 21.
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

    # True means player standing, False means player went over. This asks the player if they want to take new cards, or stand, or if they're over.
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

    # This handles whether the user wants to place an insurance bet
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

    # True means the dealer's turn is finished, False means the dealer has gone bust. This players out the dealer's turn.
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

            # Ends dealer turn if their total is > 17 or greater than the player's total. 
            elif total >= 17 or total >= self.player.total(self.player.Decks[0]):
                break

            else:
                dealer.Get_Card(dealer.Cards)
                print(
                    f"\nThe dealer takes a card, their new card is the: {dealer.convert(dealer.Cards[-1])}"
                )
                print()

        return True

    # This function takes pOver (whether or not player is Over) and dOver (whether or not the dealer is Over) and returns who has one, or not, and how much the player gets.
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
                    f"Your bet has been doubled! Your current balance is: {int(player.balance)}, however the score for this user is: {score}! Keep playing to try to beat this score!"
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

    # This is the main function where the main sequence of checks and fucntions are run
    def main(self):
        player = self.player
        print(f"Your current balance is: {int(player.balance)}\n")

        game.bet_amount()

        player.Deal_Cards()
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
