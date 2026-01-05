# find the divisors of the given number
num = int(input("enter a number: "))
i=1
while(i<=num):
    if num%i==0: #if i when dividing the num has no remainder then it is the numbers divisor
        print(i)
    i+=1
