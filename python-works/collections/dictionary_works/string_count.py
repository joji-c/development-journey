string1="hello world"
wrdc={}
for s in string1:
    if s in wrdc:
        wrdc[s]+=1
    else:
        wrdc[s]=1
print(wrdc)
