from random import randint


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
        bet = int(input(f"How much would you like to bet, your current balance is {player.balance}: "))
        
        if bet > player.balance:
            print("That is not a valid bet")
        else:
            player.balance -= bet
            print(f"Bet of {bet} added, an equal amount has been removed from your balance")

    elif decision == "hit":
        Get_Card(player)
        print(f"\nYour new card is: {convert(player.Cards[-1])}")

    elif decision == "stand":
        return True
    else:
        print("That isnt an option, please check your spelling\n")
        return False


def Get_Card(player):
    player.Cards.append(randint(1, 52))
    

def dealer_turn(dealer):
    
    print(f"\nThe dealer reveals their facedown card: {convert(dealer.Cards[1])}")
    
    while True:
        total = 0

        for card in dealer.Cards:
            card -= ((card-1)//13)*13
            total += card + 1
    
        print(f"The dealers current total is: {total}")

        if total > 21:
            print("The dealer is bust")

        elif total >= 17:
            break

        else:
            Get_Card(dealer)
            print(f"\nThe dealer takes a card, their new card is:   {convert(dealer.Cards[-1])}")
            print()

        



def settle(player, dealer):
    ptotal = 0
    dtotal = 0

    for card in player.Cards:
        ptotal += int(card - ((card-1)//13)*13)

    for card in player.Cards:
        dtotal += int(card - ((card-1)//13)*13)

    if ptotal > dtotal:
        pass
    elif ptotal == dtotal:
        pass
    else:
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

    print(f"Your current total is: {total}")

    if total > 21:
        return True
    else:

        return False
