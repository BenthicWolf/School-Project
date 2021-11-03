import json
from random import randint


def userauth(player):
    print("Please login to an authorised user account.\n")
    player.Uname = str(input("Input a valid username here: "))
    player.Upass = str(input("Input a valid password here: "))

    Uname = player.Uname
    Upass = player.Upass

    File = open("users.json", "r")
    Valid_Users = json.load(File)

    if Uname in Valid_Users.keys() and Valid_Users[Uname] == Upass:
        print("\nSuccessfuly authorised user account\n\n")
        File.close()
        player.name = Uname
        return True
    else:
        print("\nFailure to authorise user account\n\n")
        File.close()
        return False


# True means player stuck, False means player went over
def Choice(player):
    while True:
        print("\nDo you want to hit or stand?")
        decision = str(input("Please enter one of the options: ")).lower()

        if decision == "hit":
            player.Get_Card()
            print(f"\nYour new card is: {convert(player.Cards[-1])}")
            if player.total() > 21:
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


def dealer_turn(dealer):

    print(
        f"\nThe dealer reveals their facedown card: {convert(dealer.Cards[1])}")

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
                f"\nThe dealer takes a card, their new card is the: {convert(dealer.Cards[-1])}")
            print()

    return True


def settle(player, dealer, pOver, dOver):
    ptotal = player.total()
    dtotal = dealer.total()
    Uname = player.Uname

    if (dOver or ptotal > dtotal) and not pOver:
        print("Congratulations, you win!")

        File = open("scores.json", "r")
        scores = json.load(File)
        score = scores[Uname]
        File.close()
        # int(File.read().split(f"{player.name} : ")[1].split('\n')[0]) # witchcraft

        player.balance += (player.bet)*2

        file = open("Score.json", "w")
        json.dump(scores, file)

        if score < player.balance:
            scores[Uname] = player.balance
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
    if card == 11:
        card = "Jack"
    if card == 12:
        card = "Queen"
    if card == 13:
        card = "King"

    return str(card)+" of "+suit
