#find the armstrong num ,its lenght nums as the digits expo and its sum will be equal to the given number
num = int(input("enter a number: ")) #153
num_cpy = num #req as num will became 0 after first loop
num_cpy2 = num
count = 0 #1, 2, 3
sum = 0 #27, 152, 153
while(num!=0):#153, 15, 1,0 so stop
    digit=num%10 #3, 5, 1
    count=count+1 #1, 2, 3
    num=num//10 #15, 1, 0
while(num_cpy!=0): #153, 15, 1, 0 so stop
    digit=num_cpy%10 #3, 5, 1
    expo=digit**count #27, 125 ,1
    sum=sum+expo #27, 152, 153
    num_cpy=num_cpy//10 #15, 1, 0
print("sum:",sum) # sum= 153 which was the given number thus an armstrong number
if num_cpy2 == sum:
    print("it is a armstrong number")
else:
    print("its not a armstrong number")
