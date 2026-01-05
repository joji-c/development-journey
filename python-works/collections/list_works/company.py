emails=["a@gmail.com","b@yahoo.com","c@gmail.com","d@outlook.com","b@yahoo.com"]
un=[]
dup=[]
for e in emails:
    if e not in un:
        un.append(e)
    else:
        dup.append(e)
print("unique emails:",un)
print("duplicate emails:",dup)


