#disp sum of even nums till limit
num = int(input("enter number: "))
sum = 0
for i in range(1,num+1):
    if i%2==0:
        sum+=i
print(sum)