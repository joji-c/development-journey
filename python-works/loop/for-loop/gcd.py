# greatest common divisor of two num
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
smallnum = min(num1,num2)
for i in range(1,smallnum+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)