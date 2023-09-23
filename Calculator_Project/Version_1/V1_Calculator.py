number1 = int(input("Please enter your first number: "))
number2 = int(input("Please enter your second number: "))

operation = input("Please put the operation you wish to use in the form of the symbol: ")

if operation == "+":
    print("Your 2 numbers added together is: ", number1+number2)
elif operation == "-":
    print("Your 2 numbers subtracted is: ", number1-number2)
elif operation == "/":
    print("Your 2 numbers diveded is: ", number1/number2)
elif operation == "*":
    print("Your 2 numbers multipled is: ", number1*number2)
elif operation == "**":
    print("Your numbers to the power off is: ", number1**number2)
elif operation == "//":
    print("Your 2 numbers Floor divided is: ", number1//number2)
elif operation == "%":
    print("Your 2 numbers modulus is: ", number1%number2)
else:
    print("INVALID Operation Choosen")