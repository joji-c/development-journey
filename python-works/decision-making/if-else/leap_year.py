year = int(input("eneter year: "))
if (year%100 == 0 and year%400 == 0) or (year%100 != 0 and year%4 == 0):
    print("its a leap year")
else:
    print("not a leap year")

"""
in this we divide the year into centuary year an year than ends with two zeroes and non centuary year then 
we check if both are leap year or not for centuary year we divide with 400 and for non centuary year we divide wth
 4 and if their remainde is zero then its a leap year.
"""
