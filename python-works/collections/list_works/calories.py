daily_calories=[1200,1300,1400,1230,1430,1540,1500]
print(daily_calories[3])#prints the value in index 3
daily_calories[6]=1320#change value in index 6 from 1500 to 1320
print(daily_calories)

#here we use index to iterate
total=0
for i in range(0,7):
    total+=daily_calories[i]
print("Total calories:",total)

#here we directly use the objects to iterate
print("calorie above 1300: ",end="")
for c in daily_calories:
    if c > 1300:
        print(c,end=" ")
print()

#avg calorie consumption
total=0
for i in range(0,7):
    total+=daily_calories[i]
avg=total//len(daily_calories)
print("average calorie:",avg)
