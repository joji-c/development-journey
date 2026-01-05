num1=int(input("enter num1: "))
num2=int(input("enter num2: "))

try:
    div=num1/num2
    print(div)  #here if no error occurs we get the div value
except Exception as e:
    print(e)   #here if a error occurs we get the error name from exception
finally:
    print("file operation")
    print("database count")
