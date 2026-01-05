#read start and stop and disp them nums in btw
start=int(input("enter the start: "))
stop=int(input("enter the stop: "))
if start<stop:
    for num in range(start,stop+1):
        print(num)
else:
    for num in range(start,stop,-1):
        print(num)