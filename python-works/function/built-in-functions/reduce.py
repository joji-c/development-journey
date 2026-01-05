from functools import reduce
lst=[1,2,3,4,5,6,7,8,9,10]
total=reduce(lambda n1,n2:n1+n2,lst)
print(total)

product=reduce(lambda n1,n2:n1*n2,lst)
print(product)

min_num=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(min_num)

max_num=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max_num)
