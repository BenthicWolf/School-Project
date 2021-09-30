from random import randint


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
    player.Card1 = randint(1, 52)
    player.Card2 = randint(1, 52)


def Choice():
    print("Do you want to place a bet, hit, or stand?")
    decision = str(input("Please enter one of the options: ")).lower()
    if decision == "bet":
        pass
    elif decision == "bet":
        pass
    elif decision == "bet":
        pass
    else:
        print("That isnt an option, please check your spelling\n")
        return False


def Get_Card():
    pass


def Dealer_Turn():
    pass


def Settle():
    pass
