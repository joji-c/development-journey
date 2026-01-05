#add the digits of a number to get its sum
num = int(input("eneter the number: "))#123
sum = 0 #0, 3, 5, 6
while(num!=0):#123, 12, 1, 0 so stop
    digit = num%10 #3, 2 ,1
    sum = sum + digit #3, 5, 6
    num = num//10 #12, 1, 0
print(sum) #thus sum = 6
