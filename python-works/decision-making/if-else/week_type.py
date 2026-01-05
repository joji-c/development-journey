day = int(input("enter the day 1-7: "))
if day in range(1,6):
    print("WEEK DAY")
elif day in range(6,8):
    print("WEEK END")
else:
    print("Invalid Input")
