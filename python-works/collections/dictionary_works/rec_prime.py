num=[2,4,5,10,13,14,13,11,7,9,7]
pri=[]
p={}
n=max(num)
for i in num:
    for j in range(2,n):
        if i%j==0:
            break
        else:
            pri.append(i)
            break

for ch in pri:
    if ch in p:
        p[ch]+=1
    else:
        p[ch]=1
print("the recuring prime numbers are:",end=" ")
for k,v in p.items():
    if v>1:
        print(k,end=" ")
