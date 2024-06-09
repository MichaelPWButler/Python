import csv

def login():
    loginEmail = input("Please enter your email: ")
    loginPassword = input("Please enter your password: ")
    
    with open("storage.txt", "r") as loginFile:
        reader = csv.reader(loginFile)
        for userInfo in reader:
            if userInfo[0] == loginEmail and userInfo[1] == loginPassword:
                return True, userInfo
    
    return False, None
    

def signUp():
    signupEmail = input("Please enter the email for your account: ")
    signupPassword1 = input("Please input your password: ")
    signupPassword2 = input("Please input your password again: ")
    
    emailCheck = "@" in signupEmail
    
    if emailCheck and (signupPassword1 == signupPassword2) and len(signupPassword1) >= 8:
        with open("storage.txt", "a") as signUpFile:
            signUpFile.write(f"\n{signupEmail},{signupPassword1},0")
        print("Account Added Successfully")
    elif emailCheck and (signupPassword1 != signupPassword2 or len(signupPassword1) < 8):
        print("Invalid Password")
    else:
        print("Invalid Email")