from random import randint
from Converter import Card_Table


def userauth():
    print("Please login to an authorised user account.\n")
    Uname = str(input("Input a valid username here: "))
    Upass = str(input("Input a valid password here: "))

    Valid_Users = open("Users.txt", "r")

    if f"{Uname} : {Upass}" in Valid_Users.read():
        print("\nSuccessfuly authorised user account\n\n")
        Valid_Users.close()
        return True
    else:
        print("\nFailure to authorise user account\n\n")
        Valid_Users.close()
        return False


def Deal_Cards(player):
    player.Cards.append(randint(1, 52))
    player.Cards.append(randint(1, 52))


def Choice(player):
    print("\nDo you want to place a bet, hit, or stand?")
    decision = str(input("Please enter one of the options: ")).lower()

    if decision == "bet":
        return False
    elif decision == "hit":
        Get_Card(player)

    elif decision == "stand":
        return True
    else:
        print("That isnt an option, please check your spelling\n")
        return False


def Get_Card(player):
    player.Cards.append(randint(1, 52))
    print(f"\nYour new card is: {convert(player.Cards[-1])}")


def dealer_turn(dealer):
    pass


def settle():
    pass


def convert(card):
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

    return str(card)+" of "+suit


def is_over(player):
    total = 0

    for card in player.Cards:
        total += int(card - ((card-1)//13)*13)

    print(f"Your new total is: {total}")

    if total > 21:
        return True
    else:

        return False
