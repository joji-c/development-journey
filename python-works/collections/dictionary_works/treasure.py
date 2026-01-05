treasure={"box1":"gold",
          "box2":"silver",
          "box3":"diamond",
          "box4":"platinum"}

#print dictionaryy
print(treasure["box3"])

#add new key value pair
treasure["box5"]="iron"
print(treasure)

#check if box6 exist if not add it as copper
if "box6" not in treasure:
    treasure["box6"]="copper"
print(treasure)

#def pop()
treasure.pop("box4")#removes the key value pair of the specified key
print(treasure)

#iteration
for k in treasure:  #in dictionary if we use --in-- we get its key
    print(k,treasure[k])
for k in treasure:  #in dictionary if we use --in-- we get its key
    print(k)

#def keys()
all_keys=treasure.keys()   #gives all the keys in a given dictionary
print(all_keys)
        #or
for k in treasure.keys():
    print("keys:",k)


#def values()
all_values=treasure.values()  #gives all the values in a given dictionary
print(all_values)
        #or
for v in treasure.values():
    print("values:",v)

#def items()
all_items=treasure.items()
print(all_items)
        #or
for k,v in treasure.items():
    print(k,v)

#def get()
print(treasure.get("box10"))#here if box10 does not exist then we get a none value
print(treasure.get("box10","empty box"))#here instead of none we get empty box as the return for a invalid input
print(treasure["box10"])# here if given key is invalid then we will get a error and stop the code

