
def UserAuth():
    print("Please login to an authorised user account.\n")
    Uname = str(input("Input a valid username here: "))
    Upass = str(input("Input a valid password here: "))

    Valid_Users = open("Users.txt", "r")

    if f"{Uname} : {Upass}" in Valid_Users.read():
        print("\nSuccessfuly authorised user account\n\n")
        return "Succeeded"
    else:
        print("\nFailure to authorise user account\n\n")
        return "Failed"

    Valid_Users.close()


def Deal_Cards():
    pass


def Choice():
    pass


def Get_Card():
    pass


def Dealer_Turn():
    pass


def Settle():
    pass
