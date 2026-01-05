orders=["chai","biriyani","chai","coffee","dosa"]
#def append(value)
orders.append("friedrice")#here the given value is added as the last element in the list
print("appended:",orders)

#def insert(index,value)
orders.insert(2,"upma")#here the value is added to the specified index
print("inserted:",orders)

#def pop(index)    here the index value is -1 by default
print(orders.pop())#here the last elemnt of the list is removed and the removed elemnt is returned
orders.pop(2)#here the object at index 2 is removed
print("popped:",orders)

#def remove(value)
orders.remove("dosa")
print("removed:",orders)#here the obj that is specified will be removed

#def index(value)
print("index:",orders.index("biriyani")) #this returns the index of the specifies objects first occurance

#def count(value)
freq=orders.count("chai")#this returns the number of occurances of the given object in the list
print("count:",freq)

#def reverse()
orders.reverse() #here the given list is reversed
print(orders)

#def sort()  here the reverse parameter is false by default which means ascending order
orders.sort()#sorting in ascending order reverse=False
print(orders)
orders.sort(reverse=True)#sorted in descending order
print(orders)

#def copy()    here a new obj of same value is made so that changes done doent affect each other
jc_food=orders.copy()#here we make a new list that is the copy of the given list
jc_food[2]="burger"
print("orginal:",orders) #here the change made in the copy doesnt affect the original
print("copied:",jc_food) 

