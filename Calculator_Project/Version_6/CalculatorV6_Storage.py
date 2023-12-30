def check(result, calculation): # checking to see if the user want to add the result to the storage
    decision = input("Would you like to store the result of this caclulation?\nY- YES\nN- NO\n")
    if decision.upper() == "N":
        pass
    elif decision.upper() == "Y":
        storeResult(result, calculation)
    else:
        print("Invalid Input")
        check()

def storeResult(result, calc): #adding the result to the text file
    f = open("storageV6.txt", "a")
    f.write(str(calc) + "=" + str(result) + "\n")
    f.close()
    

def viewStorage(): # printing out all of the lines in the storage text file
    f = open("storageV6.txt", "r")
    print("**************************")
    for x in f:
        print(x)
    print("**************************")
    f.close()
