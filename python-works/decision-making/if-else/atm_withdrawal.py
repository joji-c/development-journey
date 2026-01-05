db_pin = 12345
db_balance =56789

pin = int(input("enter the pin: "))
if db_pin == pin:
    withdraw = int(input("enter withdrawal amount: "))
    if withdraw <= db_balance:
        print("withdrawal success")
    else:
        print("insufficient balance")
else:
    print("incorrect pin")
