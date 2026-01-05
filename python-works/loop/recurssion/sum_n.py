def sum_n(num):
    if num==0:
        return 0
    return num%10 + sum_n(num//10) 

print(sum_n(543))
"""
sum_of_n(543) = 3 + sum_of_n(54)  3+9=12
sum_of_n(54) = 4 + sum_of_n(5)    4+5=9
sum_of_n(5) = 5 + sum_of_n(0)     5+0=5
sum_of_n(0) = 0
"""