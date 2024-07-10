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

def editPassword(admin):
    choose = input("Please enter the email you wish to update: ")
    with open("storage.txt", "r") as loginFile:
        reader = csv.reader(loginFile)
        for userInfo in reader:
            if userInfo[0] == choose:
                password1 = input("Please enter the new email: ")
                password2 = input("Please input the email again: ")
                if len(password1) > 8 and (password1 == password2):
                    with open("storage.txt", "r") as file:
                        lines = file.readlines()
    
                    with open("storage.txt", "w") as file:
                        for line in lines:
                            userInfo = line.strip().split(",")
                            if userInfo[0] == choose:
                                file.write(f"{userInfo[0]},{password1},{userInfo[2]}\n")
                            else:
                                file.write(line)
    adminMainMenu(admin)

def editBalance(admin):
    choose = input("Please enter the email you wish to update: ")
    with open("storage.txt", "r") as loginFile:
        reader = csv.reader(loginFile)
        for userInfo in reader:
            if userInfo[0] == choose:
                newBalance = input("Please enter the new balance: ")
                if len(password1) > 8 and (password1 == password2):
                    with open("storage.txt", "r") as file:
                        lines = file.readlines()
    
                    with open("storage.txt", "w") as file:
                        for line in lines:
                            userInfo = line.strip().split(",")
                            if userInfo[0] == choose:
                                file.write(f"{userInfo[0]},{userInfo[1]},{newBalance}\n")
                            else:
                                file.write(line)
    adminMainMenu(admin)

def editAdminDetails(admin):
    adminEmail = input("Please enter the email for your account: ")
    adminPassword1 = input("Please input your password: ")
    adminPassword2 = input("Please input your password again: ")
    
    emailCheck = "@" in adminEmail

    if emailCheck and (adminPassword1 == adminPassword2) and len(adminPassword2) >= 8:
        admin[0] = adminEmail
        admin[1] = adminPassword1
    elif emailCheck and (adminPassword1 != adminPassword2 or len(adminPassword2) < 8):
        print("Invalid Password")
    else:
        print("Invalid Email")
        
    adminMainMenu(admin)

def logout():
    with open("storage.txt", "r") as file:
            lines = file.readlines()
        
    with open("storage.txt", "w") as file:
        for line in lines:
            userInfo = line.strip().split(",")
            if userInfo[0] == admin[0]:
                file.write(f"{adminEmail},{adminPassword1},\n")
            else:
                file.write(line)

