from random import randint
from Converter import Card_Table


def UserAuth():
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
        pass
    elif decision == "hit":
        Get_Card(player)
        
    elif decision == "stand":
        return True
    else:
        print("That isnt an option, please check your spelling\n")
        return False


def Get_Card(player):
    player.Cards.append(randint(1,52))
    print(f"Your new card is: {convert(player.Cards[-1])}")


def Dealer_Turn():
    pass


def Settle():
    pass

def convert(card):
    
    return Card_Table[card]

def is_over:
    pass
