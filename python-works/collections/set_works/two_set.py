a={1,2,3,4,5}
b={4,5,6,7,8}
common=a.intersection(b)
diff=a.difference(b)
uni=a.union(b)
sym=uni.difference(common)# we can also use --- sym=a.symmetric_difference(b)
print("elements common in a and b:",common)
print("elements in a but not in b:",diff)
print("symmetric difference:",sym)
















































