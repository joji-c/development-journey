words=["hello","hai","hello","is"]
rec=[]
nonrec=[]
for w in words:
    if words.count(w)>1 and w not in rec:
        rec.append(w)
    elif words.count(w)==1:
        nonrec.append(w)

print("recursive:",rec)
print("non recursive:",nonrec)
