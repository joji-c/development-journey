years=[2021,1999,1920,2024,1852,1991,2000,2023,2016,2009]
print("Leap years are: ",end="")
for i in range(0,len(years)):
    if (years[i]%100==0 and years[i]%400==0) or (years[i]%100!=0 and years[i]%4==0):
        print(years[i],end=" ")
