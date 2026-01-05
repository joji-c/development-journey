word=" a man a plan a canal panama"
rec={}
for ch in word:
    if ch in rec:
        rec[ch]+=1
    else:
        rec[ch]=1
for k,v in rec.items():
    if v>1 and k.isalpha():
        print(k,end=" ")
 