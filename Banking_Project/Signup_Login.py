def login():
    loginEmail = input("Please enter your email:")
    loginPassword = input("Please enter your password:")
    loginFile = open("storage.txt", "r")
    for lines in loginFile:
        userInfo = lines.split(",")
        if userInfo[0] == loginEmail and userInfo[1] == loginPassword:
            state = True
    loginFile.close()
    return(state, userInfo)
    

def signUp():
    signupEmail = input("Please enter the email for your account:")
    signupPassword1 = input("Please input your password:")
    signupPassword2 = input("Please input your password again:")
    for letters in signupEmail:
        if letters == "@":
            emailCheck = True
            break
        else:
            emailCheck = False
    if emailCheck == True and (signupPassword1 == signupPassword2) and len(signupPassword1) >= 8:
        signUpFile = open("storage.txt", "a")
        signUpFile.write("\n"+signupEmail+","+signupPassword1+","+ "0")
        print("Account Added Succssefully")
        signUpFile.close()
    elif emailCheck == True and (signupPassword1 != signupPassword2 or len(signupPassword1) < 8):
        print("Invalid Password")
    else:
        print("Invalid Email")
