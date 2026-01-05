mark = int(input("enter marks out of 100: "))
if mark in range(40,90):
    print("Pass")
elif mark in range(90,101):
    print("Distinction")
elif mark in range(1,40):
    print("Fail")
else:
    print("Invalid input")

   