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
        viewAll(admin)
    elif choose == "2":
        editEmail(admin)
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

def viewAll(admin):
    with open("storage.txt", "r") as userFile:
        reader = csv.reader(userFile)
        for index, userInfo in enumerate(reader, start=1):
            formatted_info = ', '.join(item.strip() for item in userInfo)
            print(f"{index}. {formatted_info}")
    adminMainMenu(admin)

def editEmail(admin):
    choose = input("Please enter the email you wish to update: ")
    with open("storage.txt", "r") as loginFile:
        reader = csv.reader(loginFile)
        for userInfo in reader:
            if userInfo[0] == choose:
                email1 = input("Please enter the new email: ")
                email2 = input("Please input the email again: ")
                emailCheck = "@" in email1
                if emailCheck and (email1 == email2):
                    with open("storage.txt", "r") as file:
                        lines = file.readlines()
    
                    with open("storage.txt", "w") as file:
                        for line in lines:
                            userInfo = line.strip().split(",")
                            if userInfo[0] == choose:
                                file.write(f"{email1},{userInfo[1]},{userInfo[2]}\n")
                            else:
                                file.write(line)
    adminMainMenu(admin)

def editPassword():
    pass

def editBalance():
    pass

def editAdminDetails():
    pass

def logout():
    pass

