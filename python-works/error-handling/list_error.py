lst=["10","20","hello","300","hai","4 00"]
num=[]
for el in lst:
    try:
        num.append(int(el))
    except Exception as e:
        continue
print(max(num))
print(min(num))
print(sum(num))
print(sorted(num))