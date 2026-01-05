numbers=[1,34,45,43,24,26,27]
even=[]
odd=[]
for n in numbers:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
print("even numbers:",even)
print("odd numbers:",odd)
