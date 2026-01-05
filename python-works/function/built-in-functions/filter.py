lst=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda n:n%2==0,lst))
print(even)

odd=list(filter(lambda n:n%2!=0,lst))
print(odd)

num_gt_five=list(filter(lambda n:n>5,lst))
print(num_gt_five)
