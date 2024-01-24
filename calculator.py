operation = input("Enter an operation(+ - * / mod ^): ")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))


if operation == "+":
    result = number1 + number2
    print(result)
elif operation == "-":
    result = number1 - number2
    print(result)
elif operation == "*":
    result = number1 * number2
    print(result)
elif operation == "/":
    result = number1 / number2 if number2 !=0 else 'error'
    print(result)
elif operation == "mod":
    result = number1 % number2
    print(result)
elif operation == "^":
    result = number1 ** number2 
    print(result)
else:
    result = "invalid"


# Engineering Calculator 


    

    




