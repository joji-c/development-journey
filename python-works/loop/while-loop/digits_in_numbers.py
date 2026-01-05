#find the number of digits in the given number
num = int(input("enter a number: "))#123
count = 0 #0, 1, 2, 3
while(num != 0): #123, 12, 1, 0 so stop
    # digit = num%10 #123%10=3, 12%10=2, 1%10=1
    count += 1 #1, 2, 3
    num = num // 10 #12, 1, 0
print(count) #thus count = 3
