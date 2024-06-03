# This will act as the main menu huib for the application
import user
def mainMenu():
    print("Welcome To The baking App")
    print("Please press the number corresponding to the action you wish to do")
    userMenu = input("1.User Account\n2.Admin Account\n3.Exit\n")
    if userMenu == "1":
        user.mainMenuUser()
        mainMenu()
    elif userMenu == "2":
        print("Admin")
    elif userMenu == "3":
        print("Thank you for using the banking application , bye")
    else:
        print("INVALID OPTION")
        mainMenu()

mainMenu()