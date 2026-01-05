str1=input("enter the string: ")
list1=[]
VOWELS="aeiouAEIOU"
for s in str1:
    if s in VOWELS:
        list1.append(s)
print(list1)
