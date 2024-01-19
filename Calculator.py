#Let's build a calculator!

#Taking user input
first = input("Enter first number : ")
operator = input("Enter operator (+,-,*,/,%) : ")
second = input("Enter second number : ")

#Declaring datatypes
first = float(first)
second = float(second)

#if else condition to make operations
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")