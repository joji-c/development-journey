arr=[1,5,7,9,12,15,16,19,20]

#even numbers and its count
print("Even numbers:",end=" ")
even_count=0
for i in range(0,len(arr)):
    if arr[i]%2==0:
        even_count+=1
        print(arr[i],end=" ")
print()
print("Even number count:",even_count)

#odd numbers and its count
print("Odd numbers:",end=" ")
odd_count=0
for i in range(0,len(arr)):
    if arr[i]%2!=0:
        odd_count+=1
        print(arr[i],end=" ")
print()
print("Odd number count:",odd_count)
