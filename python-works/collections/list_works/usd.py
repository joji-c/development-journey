usd_inr_rates=[88.79,88.77,88.63,88.63,88.41,88.23,88.23]
#avg rate
total=0
for i in range(0,len(usd_inr_rates)):
    total+=usd_inr_rates[i]
avg=round(total/len(usd_inr_rates),2)
print(avg)

#max,min
print("max:",max(usd_inr_rates))
print("min:",min(usd_inr_rates))

#lenght
print("length:",len(usd_inr_rates))

#highest difference
change=0
for i in range(1,len(usd_inr_rates)):
    diff = abs(usd_inr_rates[i-1] - usd_inr_rates[i])
    if diff>change:
        change=diff
print("max difference:",round(change,2))
