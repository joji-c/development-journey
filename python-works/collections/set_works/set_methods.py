barath={"tea","coffee","cattoora","gheeroast","masala"}
pathans={"tea","coffee","boost","fried-rice"}

#def union(set)
all=barath.union(pathans) #it shows all the elements excuding the duplicates
print(all)

#def intersection(set)
common=barath.intersection(pathans)#it shows common elements in both sets
print(common)

#def diffference(set)
barath_only=barath.difference(pathans)#shows the elemnets unique to barath from pathans
pathans_only=pathans.difference(barath)#shows elements unique to pathans from barath
print(barath_only)
print(pathans_only)


set_a={1,2,3,4,5}
set_b={1,2,3}
set_c={5,6,7,8}
#def issuperset()
print(set_a.issuperset(set_b))#here as all elements in set b is in set a it is its superset ---- true
print(set_a.issuperset(set_c))#diff elements than set a ----- false

#def issubset()
print(set_b.issubset(set_a))#set a has all elments in set b --- true
print(set_c.issubset(set_a))#set a doesnt have all elements in set c ----false

#def symmetric_difference()
print(set_a.symmetric_difference(set_c))#union - intersection

#def add(value)
set_c.add(4)
print(set_c)

#def update(set)
set_a.update(set_c)
print(set_a)

se={1,2,3,4,5}

#def discard(value)
se.discard(3)
print(se)
se.discard(6)
print(se)#no error

#def remove(value)
se.remove(2)
print(se)
se.remove(7)
print(se)# error
