#sum of odd and even num till limit
num = int(input("enter number: "))
odd_sum=0
even_sum=0
for i in range(1,num+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("sum of even numbers:",even_sum)
print("sum of odd numbers:",odd_sum)