#display common divisor
number = int(input("enetr a number: "))
for i in range(1,number+1):
    if number%i==0:
        print(i)