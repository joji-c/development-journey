age = int(input("enetr your age: "))
if age in range(0,5):
    print("your ticket fare is Free")
elif age in range(5,19):
    print("your ticket fare is INR 10")
elif age in range(19,61):
    print("your ticket fare is INR 20")
elif age > 60:
    print("your ticket fare is INR 15")

