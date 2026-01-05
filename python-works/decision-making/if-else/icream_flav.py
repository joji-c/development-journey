print("""flavour options(1-4):
    1. chocolate
    2. vanilla
    3. strawberry
    4. butterscotch """)
choice = int(input("enter your flavour choice: "))
if choice == 1:
    print("you chose chocolate flavour")
elif choice == 2:
    print("you chose vanilla flavour")
elif choice == 3:
    print("you chose strawberry flavour")
elif choice == 4:
    print("you chose butterscotch flavour")
else:
    print("invalid flavour")
