num1 = int(input("enter a num1: "))
num2 = int(input("enter a num2: "))
i=1
while(i<=num1 and i<=num2):
    if num1%i==0 and num2%i==0:
        print(i)
    i+=1
