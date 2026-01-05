source="technician"
target="ten"
sp=0
tp=0
match=0
while sp<len(source) and tp<len(target):
    if source[sp]==target[tp]:
        sp+=1
        tp+=1
        match+=1
    else:
        sp+=1
print(match==len(target))

