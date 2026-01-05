#check if leap year or not
def is_leap_year(year):
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        return True
    else:
        return False

print(is_leap_year(1900))
print(is_leap_year(2020))
