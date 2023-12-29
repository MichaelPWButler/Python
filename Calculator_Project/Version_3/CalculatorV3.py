# Number inputs from the user
number1 = input("Please put your first number: ")
number2 = input("Please put your second number: ")

#Operation inputs from the user
operation = input("Please put your operation")

# Check inputs are numbers
try:
    number1 = int(number1)
    number2 = int(number2)
except:
    print("Not Valid Numbers")

# Perform the calculation based on the operation
if operation == "+" or operation == "add":
    print("Your 2 numbers added together is: ", number1+number2)
elif operation == "-" or operation == "minus":
    print("Your 2 numbers subtracted is: ", number1-number2)
elif operation == "/" or operation == "divide":
    print("Your 2 numbers diveded is: ", number1/number2)
elif operation == "*" or operation == "multiply":
    print("Your 2 numbers multipled is: ", number1*number2)
elif operation == "**" or operation == "power":
    print("Your numbers to the power off is: ", number1**number2)
elif operation == "//" or operation == "floor":
    print("Your 2 numbers Floor divided is: ", number1//number2)
elif operation == "%" or operation == "modulus":
    print("Your 2 numbers modulus is: ", number1%number2)
else:
    print("INVALID Operation Choosen")