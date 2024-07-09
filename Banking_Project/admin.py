import Signup_Login
import csv

def adminLogin():
    print("Welcome")
    state, admin = Signup_Login.login()
    if state and len(admin) == 2:
        print("Login Successful")
        adminMainMenu(admin)
    else:
        print("Login Failed")
        adminLogin()

def adminMainMenu(admin):
    print("Please choose an option")
    print("1. View All Accounts")
    print("2. Edit Email Of An Account")
    print("3. Edit Password of an Account")
    print("4. Edit Balance Of an Account")
    print("5. Edit Admin Details")
    print("6. Logout")
    choose = input()
    if choose == "1":
        viewAll()
    elif choose == "2":
        editEmail()
    elif choose == "3":
        editPassword()
    elif choose == "4":
        editBalance()
    elif choose == "5":
        editAdminDetails()
    elif choose == "6":
        logout()
    else:
        print("Invalid Option")
        adminMainMenu(admin)

def viewAll():
    pass

def editEmail():
    pass

def editPassword():
    pass

def editBalance():
    pass

def editAdminDetails():
    pass

def logout():
    pass

