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
    if state == True:
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
        main()

def viewBalance(user):
    print(user[2])
    main(user)

def depositMoney(user):
    add = input("Please input the amount of money you wish to add to the account")
    if numberCheck(add) == True:
        user[2] = int(user[2]) + int(add)
        main(user)
    else:
        depositMoney(user)

def withdrawMoney(user): # This needs to be fixed
    minus = input("Please input the amount of money you wish to withdraw to the account")
    if numberCheck(minus) == True:
        user[2] = user[2] - int(minus)
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
    final = open("storage.txt", "w")
    final.write(user[0] + "," + user[1] + ","+ str(user[2]))