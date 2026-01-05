num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
operator = input("enter the operation to be performed ( + , - , * , / ): ")
match operator:
    case "+":
        print("addition result:",num1 + num2)
    case "-":
        print("subtraction result:",num1-num2)
    case "*":
        print("multiplication result:",num1*num2)
    case "/":
        print("division result:",num1/num2)
    case _:
        print("Invalid input")
