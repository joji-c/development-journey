#recursive numbers
arr=[10,11,12,13,13,13,8,10,9]
rec=[]
for a in arr:
    if arr.count(a)>1 and a not in rec:
        rec.append(a)
print("recursive:",rec)

#non recurive numbers
nonrec=[]
for a in arr:
    if arr.count(a)==1 :
        nonrec.append(a)
print("non recursive:",nonrec)
