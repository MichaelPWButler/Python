import Calculatorv5_Storage  as calc#importing the moudle that allows the user to storage and view results

# Building a main menu to allow the user to access the calculator or leave the program
def mainMenu():
    decision = input("MAIN MENU \nPlease input a number:\n1. Calculator App\n2. View Stored Calculations\n3. Quit\n")
    if decision == "1": #checking the decision from the user
        calculate()
    elif decision == "2":
        calc.viewStorage()
        mainMenu()
    elif decision == "3":
        quit()
    else:
        print("Please input a valid option")
        mainMenu()

# Error handling for numbers for both the main mneu and the calculation numbers
# Passing in a list allows for an unlimited amount of numbers to be checked
def errorHandle(numbers):
    try:
        for x in numbers: # looping through each item and attempting to convert it into an integer
            x = int(x)
        return True
    except:
        return False

# Getting the 2 numbers from the user for the calculation
def inputNumbers():
    number1 = input("Please input the first number for the calculation: ")
    number2 = input("Please input the second number for the calculation: ")

    if errorHandle([number1,number2]) == False: #checking the inputs from the user
        print("Please input valid numbers")
        mainMenu()
    else:
        return int(number1), int(number2)

# Getting the operation for the calculation from the user
def getOperation():
    operation = input("Please put the operation for your calculation\nEither as a sumbol or word\n E.g + OR add\n")
    return operation

# The function that pulls all the functions together all returns the result for the user
def calculate():
    number1, number2 = inputNumbers()
    operation = getOperation()
    if operation == "+" or operation == "add":
        result = ("Your 2 numbers added together is: %d" %(number1+number2))
    elif operation == "-" or operation == "minus":
        result = ("Your 2 numbers subtracted is: %d" %(number1-number2))
    elif operation == "/" or operation == "divide":
        result = ("Your 2 numbers diveded is: " %(number1/number2))
    elif operation == "*" or operation == "multiply":
        result = ("Your 2 numbers multipled is: %d" %(number1*number2))
    elif operation == "**" or operation == "power":
        result = ("Your numbers to the power off is: %d" %(number1**number2))
    elif operation == "//" or operation == "floor":
        result = ("Your 2 numbers Floor divided is: %d" %(number1//number2))
    elif operation == "%" or operation == "modulus":
        result = ("Your 2 numbers modulus is: %d" %(number1%number2))
    else:
        result = ("INVALID Operation Choosen")
        mainMenu()
    print(result)
    calc.check(result)
    mainMenu()

mainMenu()