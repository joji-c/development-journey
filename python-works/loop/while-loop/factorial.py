#find the factorial of the given number
num = int(input("enter a nmumber: "))
i=1
fact =1
while(i<=num):
    fact = fact * i
    i+=1
print(fact)