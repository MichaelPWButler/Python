import Signup_Login

def mainMenuUser():
    print("Welcome")
    print("Please press the number corresponding to the action you wish to do")
    user = input("1.Login\n2.Sign Up\n3.Exit\n")
    if user == "1":
        userLogin()
    elif user == "2":
        Signup_Login.signUp()
    elif user == "3":
        pass
    else:
        print("INVALID OPTION")
        mainMenuUser()

def userLogin():
    state, user = Signup_Login.login()
    if state:
        print("Login Successful")
        main(user)
    else:
        print("Login Failed")
        userLogin()

def main(user):
    print("Welcome To the banking application")
    print("Please select an option")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Logout")
    choice = input()
    if choice == "1":
        viewBalance(user)
    elif choice == "2":
        depositMoney(user)
    elif choice == "3":
        withdrawMoney(user)
    elif choice == "4":
        logout(user)
    else:
        print("Inavlid Input")
        main(user)

def viewBalance(user):
    print(f"Current balance: {user[2]}")
    main(user)

def depositMoney(user):
    add = input("Please input the amount of money you wish to add to the account: ")
    if numberCheck(add):
        user[2] = str(int(user[2]) + int(add))
        main(user)
    else:
        depositMoney(user)

def withdrawMoney(user):
    minus = input("Please input the amount of money you wish to withdraw from the account: ")
    if numberCheck(minus):
        if int(user[2]) >= int(minus):
            user[2] = str(int(user[2]) - int(minus))
        else:
            print("Insufficient funds")
        main(user)
    else:
        withdrawMoney(user)


def numberCheck(num):
    try:
        int(num)
        return True
    except:
        print("Invalid input")
        return False

def logout(user):
    with open("storage.txt", "r") as file:
        lines = file.readlines()
    
    with open("storage.txt", "w") as file:
        for line in lines:
            userInfo = line.strip().split(",")
            if userInfo[0] == user[0]:
                file.write(f"{user[0]},{user[1]},{user[2]}\n")
            else:
                file.write(line)
    print("Logged out and data updated.")