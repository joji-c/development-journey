#find the sum of cubes of digits from a given number
num = int(input("enter a number: ")) #123
sum = 0 #0, 27, 35, 36
while(num!=0): #123, 12, 1, 0 so stop
    digit=num%10 #3, 2, 1
    cube=digit**3 #27, 8, 1
    sum=sum+cube #27, 35 , 36
    num=num//10 #12, 1, 0
print(sum) #sum = 36
