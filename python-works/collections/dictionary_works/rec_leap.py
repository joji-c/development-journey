year=[2005,2004,2008,2010,2024,2028,2024,2005]
leap={}
for ch in year:
    if (ch%100==0 and ch%400==0) or (ch%100!=0 and ch%4==0):
        if ch in leap:
            leap[ch]+=1
        else:
            leap[ch]=1
     
for k,v in leap.items():
    if v>1:
        print(k,end=" ")
