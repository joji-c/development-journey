db_password = "blabla"
db_otp = 123
# conside this to be the saved password and given otp

password = input("enter your password: ")
if db_password == password:
    otp=int(input("enter the otp: "))
    if db_otp == otp:
        print("login successfull")
    else:
        print("Incorrect otp")
else:
    print("Incorrect password")

