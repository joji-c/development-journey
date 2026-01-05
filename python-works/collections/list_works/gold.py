gold_rate=[11185,11185,11185,11235,11135,11225,11290]

#avg rate
total=0
for i in range(0,len(gold_rate)):
    total+=gold_rate[i]
avg=round(total/len(gold_rate),2)
print("average:",avg)

#max,min
print("max:",max(gold_rate))
print("min:",min(gold_rate))

#lenght
print("length:",len(gold_rate))

#highest difference
change=0
for i in range(1,len(gold_rate)):
    diff = abs (gold_rate[i-1] -(gold_rate[i]))
    if diff>change:
        change=diff
print("max difference:",round(change,2))

#lowest difference
change=1000000
for i in range(1,len(gold_rate)):
    diff = abs (gold_rate[i-1] -(gold_rate[i]))
    if diff<change:
        change=diff
print("min difference:",round(change,2))

