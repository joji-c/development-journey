words=["cat","act","madam","hello","madam"]
rec={}
for ch in words:
    if ch==ch[::-1] :
        if ch in rec:
            rec[ch]+=1
        else:
            rec[ch]=1
for k,v in rec.items():
    if v>1:
        print(k,end=" ")
