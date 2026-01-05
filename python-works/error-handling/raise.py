age=int(input("enter age: "))
if age<18:
    raise Exception("Invalid Age")
else:
    print("Eligible for vote")
