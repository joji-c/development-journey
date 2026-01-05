def length(*str1):
    str2=[]
    for i in str1:
        str2.append(len(i))
    return str2

print(length("hello","how","are","you"))