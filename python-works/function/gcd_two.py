def gcd(num1,num2):
    small=min(num1,num2)
    for i in range(1,small+1):
        if num1%i==0 and num2%i==0:
            great=i
    return great


print(gcd(12,24))