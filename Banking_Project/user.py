import Signup
def userLogin():
    state, user = Signup.login()
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
    choice = input()
    if choice == "1":
        viewBalance(user)
    elif choice == "2":
        depositMoney(user)
    elif choice == "3":
        withdrawMoney(user)
    else:
        print("Inavlid Input")
        main()

def viewBalance(user):
    print(user[2])
    main(user)

def depositMoney(user):
    add = input("Please input the amount of money you wish to add to the account")
    if numberCheck(add) == True:
        user[2] = user[2] + int(add)
        main(user)
    else:
        depositMoney(user)

def withdrawMoney(user):
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

userLogin()