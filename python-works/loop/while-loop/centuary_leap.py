#disp only centuary leap from 1800 - 2025
i = 1800
while(i<=2025):
    if(i%100==0 and i%400==0):
        print(i)
    i+=1
