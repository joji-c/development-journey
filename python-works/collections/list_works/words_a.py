def word(strin):
    list1=[]
    for i in strin:
        if "a" in str(i.casefold()) :
            list1.append(i)
    return list1


strin=["Apple","dog","cat","pen"]
print(word(strin))