#disp the numb of odd and even num within limit
num = int(input("enter number: "))
odd_count=0
even_count=0
for i in range(1,num+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("count of even numbers:",even_count)
print("count of odd numbers:",odd_count)


