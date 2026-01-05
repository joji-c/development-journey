age = int(input("enter age: "))
if age >= 18:
    test = input("test passed yes|no :")
    if test == "yes":
        print("license approved")
    elif test == "no":
        print("test not cleared")
    else:
        print("Invalid input")
else:
    print("not eligible due to age")
