#common divisors of two numbers
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
smallnum = min(num1,num2)
for i in range(1,smallnum+1):
    if num1%i==0 and num2%i==0:
        print(i)

#for three num divisoes
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
smallnum = min(num1,num2,num3)
for i in range(1,smallnum+1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        print(i)