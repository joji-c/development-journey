"""
comprehension is the easy way of making list|set|tuple|dict

list=[return iteration condition]
dict={return iteration condition}

first give the iteration , then condition(if needed) and then the return
but ieration and return is always required

"""
arr=[1,2,3,4,5]

add_5=[num+5 for num in arr]
print(add_5)

even=[num for num in arr if num%2==0]
print(even)

odd=[num for num in arr if num%2!=0]
print(odd)

square={num:num**2 for num in arr}
print(square)