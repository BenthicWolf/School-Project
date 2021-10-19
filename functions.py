from random import randint


def userauth(player):
    print("Please login to an authorised user account.\n")
    Uname = str(input("Input a valid username here: "))
    Upass = str(input("Input a valid password here: "))

    Valid_Users = open("Users.txt", "r")

    if f"{Uname} : {Upass}\n" in Valid_Users.read():
        print("\nSuccessfuly authorised user account\n\n")
        Valid_Users.close()
        player.name = Uname
        return True
    else:
        print("\nFailure to authorise user account\n\n")
        Valid_Users.close()
        return False


def Deal_Cards(player):
    player.Cards.append(randint(1, 52))
    player.Cards.append(randint(1, 52))

# True means player stuck, False means player went over
def Choice(player): 
    while True:
        print("\nDo you want to hit or stand?")
        decision = str(input("Please enter one of the options: ")).lower()

        if decision == "hit":
            Get_Card(player)
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

def Get_Card(player):
    player.Cards.append(randint(1, 52))


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
            Get_Card(dealer)
            print(
                f"\nThe dealer takes a card, their new card is the: {convert(dealer.Cards[-1])}")
            print()

    return True


def settle(player, dealer, pOver, dOver):
    ptotal = player.total()
    dtotal = dealer.total()

    if (dOver or ptotal > dtotal) and not pOver:
        print("Congratulations, you win!")

        File = open("Score.txt", "r+")
        score = int(File.read().split(f"{player.name} : ")[1].split('\n')[0]) # witchcraft
        File.close()

        player.balance += (player.bet)*2

        if score < player.balance:
            print(
                f"Your bet has been doubled! Your current balance is : {player.balance}, this beats highest score for this user, which is: {score}! Keep playing if you want to further this record!")

        elif score >= player.balance:
            print(
                f"Your bet has been doubled! Your current balance is : {player.balance}, however the highest score for this user is: {score}! Keep playing to try to beat this score!")

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


