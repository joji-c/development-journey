def first(*str1):
    str2=[]
    for i in range(0,len(str1)):
        str2.append(str1[i][0])
    return str2

print(first("apple","banana","cherry"))
