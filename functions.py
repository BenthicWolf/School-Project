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


def Deal_Cards(Player):
    Player.Card1 = randint(1, 52)
    Player.Card2 = randint(1, 52)
    return


def Choice():
    print("Do you want add a bet, hit, or stand?")
    decision = (str(input("Please input one of the options: "))).lower()

    switch(decision){}


def Get_Card():
    pass


def Dealer_Turn():
    pass


def Settle():
    pass
